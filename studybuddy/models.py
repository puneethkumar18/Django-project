from django.db import models

# Create your models here.

class LogIn(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=12)


class UserType(models.TextChoices):
    ADMIN = "admin","Admin"
    USER = "user","User"


class User(models.Model):
    name  = models.CharField()
    emil = models.EmailField()
    bio = models.TextField()
    usertype = models.CharField(max_length=20,choices=UserType.choices,default=UserType.USER)
