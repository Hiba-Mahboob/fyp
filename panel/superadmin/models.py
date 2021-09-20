from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_member = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)
    is_university = models.BooleanField(default=False)
    is_department = models.BooleanField(default=False)

class UniUni(models.Model):
    uni=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    username=models.CharField(max_length=255,default="-")
    name=models.CharField(max_length=255,default="-")

class DeptUni(models.Model):
    uni=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    username=models.CharField(max_length=255,default="-")
    name=models.CharField(max_length=255,default="-")

class MemberDept(models.Model):
    dept=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    username=models.CharField(max_length=255,default="-")

class StudentUni(models.Model):
    uni=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    username=models.CharField(max_length=255,default="-")
    batch=models.CharField(max_length=255,default="-")
    number=models.CharField(max_length=255,default="-")

    def __str__(self):
        return f"StudentUni('{self.username}','{self.number}')"


class ScheduleMsg(models.Model):
    student=models.CharField(max_length=255)
    msg=models.CharField(max_length=255, default="This message is empty")

class QueryHistory(models.Model):
    query = models.CharField(max_length=255)
    response = models.CharField(max_length=255,default="-")
    status = models.BooleanField(default=False)
    queried_by=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.query
