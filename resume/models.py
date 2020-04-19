from django.db import models
import datetime

class Experience(models.Model):
    date_started = models.CharField(max_length=15)
    date_ended = models.CharField(max_length=15)
    current = models.BooleanField(default=0) # 0 for false, 1 for true
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    description = models.TextField()

class Course(models.Model):
    date_ended = models.CharField(max_length=15)
    school = models.CharField(max_length=50)
    title = models.CharField(max_length=50)

class Extracurricular(models.Model):
    date_started = models.CharField(max_length=15)
    date_ended = models.CharField(max_length=15)
    current = models.BooleanField(default=0)
    title = models.CharField(max_length=50)
    description = models.TextField()

class Skill(models.Model):
    skill = models.CharField(max_length=25)
    level = models.IntegerField()
