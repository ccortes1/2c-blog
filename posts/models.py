""" Posts and Category model. """

import datetime

# Django
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Utilities
from utils.models import BasicModel

class Post(BasicModel):
    title = models.CharField('Post title', max_length = 200)
    author = models.ForeignKey('users.User', on_delete = models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    text_body = models.TextField(blank=False)
    pub_date = models.DateTimeField('Date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days = 1) <= self.pub_date <= now

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs = {'pk' : self.pk})

class Category(BasicModel):
    name = models.CharField(max_length=50, blank=False)

    class Meta(BasicModel.Meta):
        db_table = "category"

    def __str__(self):
        return self.name

class Comment(BasicModel):
    post = models.ForeignKey('Post', on_delete = models.CASCADE, related_name='comments')
    user = models.ForeignKey('users.User', on_delete = models.CASCADE)
    text = models.CharField('Comment', max_length = 200, blank = False)
