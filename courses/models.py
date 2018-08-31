from django.db import models

# Create your models here.

class Course(models.Model):
    author = models.CharField(max_length=255)
    course_title = models.CharField(max_length=255)
    technology = models.CharField(max_length=100)
    course_logo = models.CharField(max_length=1000)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    lesson_title = models.CharField(max_length=255)
