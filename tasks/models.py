from telnetlib import STATUS
from turtle import update
from venv import create
from django.db import models

# Create your models here.

class Task(models.Model):

    STATUS = (
      ('doing', 'Doing'),
      ('done', 'Done')
    )

    title = models.CharField(max_length=255)
    descripiton = models.TextField()
    done = models.CharField(
      max_length=5, 
      choices=STATUS, 
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    #Retornar nome da tarefa no admin
    def __str__(self):
      return self.title
