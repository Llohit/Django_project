from django.db import models

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
    type = models.CharField(max_length=50)
    description = models.TextField()
    account = models.IntegerField()

class User(models.Model):
    user = models.IntegerField(primary_key=True, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)