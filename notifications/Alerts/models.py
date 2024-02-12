from django.db import models


class Notification(models.Model):
    Title = models.CharField(max_length=100)
    Body = models.TextField(max_length=500)
    Viewers = models.ManyToManyField('Viewers.Viewer', blank=True)