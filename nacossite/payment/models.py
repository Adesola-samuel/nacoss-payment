from django.db import models
from django.contrib.auth.models import User
from org.models import Session


class Due(models.Model):
    title = models.CharField(max_length=30)
    amount = models.FloatField()
    description = models.TextField(default='')
    def __str__(self):
        return str(self.title)


class Transaction(models.Model):
    id = models.CharField(max_length=35, primary_key=True )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    due = models.ForeignKey(Due,on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
