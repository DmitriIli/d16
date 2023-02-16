from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.core.cache import cache

from board import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    is_activate = models.BooleanField(default=False)

class Categories(models.Model):
    name = models.CharField(max_length=64)

class Ads(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_created=True)
    title = models.CharField(max_length=64, default=f'заголовок статьи от {datetime.now()}')
    text = models.CharField(max_length=512, default=f'текст статьи от {datetime.now()}')
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    upload = models.FileField(upload_to='media/')


class FeedBack(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    time_create = models.DateField(auto_created=True)
    text = models.CharField(max_length=256, default=f'текст отклика от {datetime.now()}')
