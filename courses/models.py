from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse

# Create your models here.

class Course(models.Model):
    author = models.CharField(max_length=255)
    course_title = models.CharField(max_length=255)
    technology = models.CharField(max_length=100)
    course_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.course_title + ' - ' + self.author

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    lesson_title = models.CharField(max_length=255)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.lesson_title
