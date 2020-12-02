from django.db import models

# Create your models here.

class Daftar(models.Model):
    lis = models.CharField(max_length=200)