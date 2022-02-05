from django.db import models

class Tutorial(models.Model):
    name = models.CharField(max_length=100)