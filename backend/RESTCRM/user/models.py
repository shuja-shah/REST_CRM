from django.contrib.auth.models import AbstractUser
from django.db import models
from Lists.models import List

from .user_manager import UserManager


class user(AbstractUser):
    
    username = models.CharField(max_length=100 , unique= True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'

class List(models.Model):
    '''Model Responsible for Todo List'''
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    task = models.CharField(max_length=200) 
    is_completed = models.BooleanField(default=False)

    def __str__(self): 
        return self.task + ' | ' + str(self.is_completed)