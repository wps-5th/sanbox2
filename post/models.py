from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User)
    photo = models.ImageField(upload_to='post', blank=True)
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
