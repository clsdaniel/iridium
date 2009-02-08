from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()
    admins = models.ManyToManyField(User)
    devels = models.ManyToManyField(User)
    
