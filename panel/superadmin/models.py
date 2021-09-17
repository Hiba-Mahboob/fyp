from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)
    is_university = models.BooleanField(default=False)

class QueryHistory(models.Model):
    query = models.CharField(max_length=255)
    response = models.CharField(max_length=255,default="-")
    queried_by=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.query
