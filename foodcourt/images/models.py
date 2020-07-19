from django.db import models

from ..posts.models import Post


class Image(models.Model):
    post = models.ForeignKey(to=Post, related_name="images", on_delete=models.CASCADE)
    url = models.ImageField()
