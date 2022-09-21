
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser) :
    email = models.EmailField(max_length=256,unique=True,blank=False, null=False)
    username=models.CharField(max_length=64, blank=False, unique=False,null=False)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username