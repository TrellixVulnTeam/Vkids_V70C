from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_boss = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    
