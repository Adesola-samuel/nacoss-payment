from django.db import models
from django.contrib.auth.models import User
from org.models import Level, Session


class Biodata(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    session_admitted = models.ForeignKey(Session, on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=16)


    class Meta:
        verbose_name_plural = 'Biodata'


