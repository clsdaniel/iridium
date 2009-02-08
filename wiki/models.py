from django.db import models
from iridium.project.models import Project

# Create your models here.
class WikiPage(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=255)
    published = models.DateField()
    
class WikiRevision(models.Model):
    page = models.ForeignKey(WikiPage)
    contents = models.TextField()
    published = models.DateField()