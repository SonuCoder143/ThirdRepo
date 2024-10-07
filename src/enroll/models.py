from django.db import models

class User(models.Model):
    Name=models.CharField(max_length=100)
    Roll_No=models.IntegerField()
