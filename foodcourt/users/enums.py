from django.db import models


class UserType(models.IntegerChoices):
    ADMIN = 1
    BUYER = 10
    SELLER = 20
