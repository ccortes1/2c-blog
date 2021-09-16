""" Posts views """

# Django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DetailView, ListView, UpdateView, FormView
from django.views.generic.base import TemplateView

# Forms
from posts.forms import PostForm, CommentForm

# Models
from posts.models import Post, Category, Comment

class PostsList(ListView):
    template_name = 'posts/home.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 15
    context_object_name = 'posts'
    def get_queryset(self):
        category = self.request.GET.get("search", '')
        if category:
            object_list = self.model.objects.filter(category__name__icontains = category)
        else:
            object_list = self.model.objects.all()
        return object_list

class CreateBlog(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:CreateBlog')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super(CreateBlog, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    template_name = 'posts/update.html'
    model = Post
    fields = ['title', 'category', 'text_body']

class PostDetailView(TemplateView):
    template_name = 'posts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(id=kwargs['id'])
        context['post'] = post
        context['comments'] = Comment.objects.filter(post=post).order_by('-created')
        return context

@login_required
def create_coment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:detail', id=post.id)
    else:
        form = CommentForm()
        return render(request, 'posts/new_comment.html', {'form': form})

