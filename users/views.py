""" Users View """

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib.auth import views as auth_views
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, FormView, UpdateView, ListView


# Models
from users.models import User
from posts.models import Post

# Forms
from users.forms import SignUpForm

class SignUpView(FormView):
    template_name= 'users/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_velid(form)


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'


class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'users/profile.html'
    paginate_by = 15
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

