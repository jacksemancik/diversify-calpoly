from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    page = models.IntegerField()
# Create your models here.
