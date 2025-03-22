from django.db import models

class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False, unique=True)
    type = models.CharField(max_length=50)
    description = models.TextField()
    account = models.IntegerField()
    user = models.IntegerField(null=False)

class User(models.Model):
    user = models.IntegerField(primary_key=True, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)