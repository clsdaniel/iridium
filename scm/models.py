from django.db import models
from django.contrib.auth.models import User

from iridium.project.models import Project

# Create your models here.
class Repository(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=255)
    desc = models.TextField()
    scm = models.TextField(max_length=12)
    path = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
    
