from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    register_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.name
