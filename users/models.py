""" Profile model. """

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from utils.models import BasicModel

class User(BasicModel, AbstractUser):
    email = models.EmailField(
        'email address',
        unique = True,
        error_messages = {'unique' : 'A user with that email already exists.'}
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    is_client = models.BooleanField(
        'client',
        default = True,
        help_text = (
            'Help easily distinguish users and perform queries. '
            'Clients are the main type of user.'
        )
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
