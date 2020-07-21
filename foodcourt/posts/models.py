from django.db import models

from ..abstract_models import BaseModel
from ..users.models import User


class Post(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(null=True)
    owner = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"<POST> {self.name} - {self.owner}"
