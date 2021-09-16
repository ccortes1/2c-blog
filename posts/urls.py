""" Post URLs """

# Django
from django.urls import path

# Views
from posts import views

urlpatterns = [
    path(
        route = 'home/',
        view = views.PostsList.as_view(),
        name = 'home'
    ),
    path(
        route = 'create/',
        view = views.CreateBlog.as_view(),
        name = 'CreateBlog'
    ),
    path(
        route = 'update/',
        view = views.UpdatePost.as_view(),
        name = 'update'
    ),
    path(
        route = 'detail/<int:id>/',
        view = views.PostDetailView.as_view(),
        name='detail'
    ),
    path(
        route='detail/<int:id>/comment/',
        view = views.create_coment,
        name = 'CreateComment'
    )
]
