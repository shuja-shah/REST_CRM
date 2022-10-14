from django.db import models


class List(models.Model):
    '''Model Responsible for Todo List'''
    task = models.CharField(max_length=200) 
    is_completed = models.BooleanField(default=False)
    
    def __str__(self): 
        return self.task + ' | ' + str(self.is_completed)