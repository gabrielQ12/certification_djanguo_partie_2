from django.db import models

class Blog(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()