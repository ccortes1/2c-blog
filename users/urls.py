""" User URLs """

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [
    path(
        route = 'login/',
        view = views.LoginView.as_view(),
        name = 'login'
    ),
    path(
        route = 'signup/',
        view = views.SignUpView.as_view(),
        name = 'signup'
    ),
    path(
        route='profile/',
        view = views.ProfileView.as_view(),
        name = 'profile'
    )
]
