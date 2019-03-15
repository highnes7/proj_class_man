from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    roll_no=models.IntegerField
    dept=models.CharField(max_length=120)
    year=models.CharField(max_length=120)

    def __str__(self):
        return self.user.username

class appl(models.Model):
    regno=models.CharField(max_length=15)
    fdate=models.DateField()
    tdate=models.DateField()
    reason=models.CharField(max_length=300)
    atype=models.CharField(max_length=10)

    def __str__(self):
        return self.atype

class notifications(models.Model):
    notification=models.CharField(max_length=256)

class grievances(models.Model):
    regno=models.CharField(max_length=15)
    subject=models.CharField(max_length=30)
    grievance=models.CharField(max_length=300)