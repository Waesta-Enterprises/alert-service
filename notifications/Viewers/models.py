from django.db import models

class Viewer(models.Model):
    viewer_id = models.CharField(max_length=500)
