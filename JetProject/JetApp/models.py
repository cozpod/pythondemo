from tkinter import CASCADE
from turtle import position
from django.db import models
from matplotlib.pyplot import title

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    Name = models.CharField(max_length=100)
    Surname = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    Email = models.EmailField(default=None)
    Display_picture = models.ImageField(upload_to='images',default='image')


 