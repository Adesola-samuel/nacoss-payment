from django.db import models
from django.contrib.auth.models import User


class Level(models.Model):
    level = models.CharField(max_length=5)
    description = models.TextField(default='', null=True, blank=True)
    def __str__(self):
        return str(self.level)

class Course(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=6)
    description = models.TextField(default='')
    instructor = models.ForeignKey(User, on_delete= models.SET_NULL, null = True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.code)

class Material(models.Model):
    title = models.CharField(max_length=50)
    material = models.FileField(upload_to='static/course_materials')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    def delete(self, *args, **kwargs):
        self.material.delete()
        super().delete(*args, **kwargs)


class Session(models.Model):
    session = models.CharField(max_length=9)
    def __str__(self):
        return str(self.session)

