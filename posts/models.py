from django.contrib.auth.models import User
from django.db import models
from datetime import datetime as dt


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, default='Post title', blank=True)
    main_post = models.CharField(max_length=100000, default="Post")
    created_at = models.DateTimeField(default=dt.now, blank=True)
    username = models.CharField(max_length=100, default='uakks')
