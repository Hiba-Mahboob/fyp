from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)