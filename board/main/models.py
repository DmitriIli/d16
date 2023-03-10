from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime
from django.urls import reverse, reverse_lazy
from django.core.cache import cache


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class Ads(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(
        max_length=64, default=f'заголовок статьи от {datetime.now()}')
    text = models.CharField(
        max_length=512, default=f'текст статьи от {datetime.now()}')
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    upload = models.FileField(upload_to='media/', blank=True)


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    time_create = models.DateField(auto_now_add=True)
    text = models.CharField(
        max_length=256, default=f'текст отклика от {datetime.now()}')
