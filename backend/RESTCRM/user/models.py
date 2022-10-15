from django.contrib.auth.models import AbstractUser
from django.db import models
from Lists.models import List


class user(AbstractUser):
    
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    list = models.OneToOneField(List, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.username
    