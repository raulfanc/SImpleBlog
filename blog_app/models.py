from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    # create display label
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None)  # we using category1 because category was used in the previous example.
    # login user, add user to post
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])



