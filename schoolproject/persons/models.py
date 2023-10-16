from django import forms
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import EmailInput


# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name




class Person(models.Model):

    name = models.CharField(max_length=124)
    dob = models.DateTimeField(auto_now=False,auto_now_add=False)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=10)
    e_mail = models.EmailField()
    address = models.TextField(blank=True)
    gender=models.CharField(max_length=100)
    materials_provided=models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.name
