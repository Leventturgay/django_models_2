from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank=True)


class Teacher(models.Model):
    pass
