from django.db import models
from django.contrib.auth.models import User
from iridium.project.models import Project

# Create your models here.
class Issue(models.Model):
    project = models.ForeignKey(Project)
    title = models.CharField(max_length=255)
    contents = models.TextField()
    author = models.ForeignKey(User, related_name="issues_authored")
    published = models.DateField()
    assigned = models.ForeignKey(User, related_name="issues_assigned")
    priority = models.IntegerField()
    status = models.IntegerField()
    
class IssueFile(models.Model):
    issue = models.ForeignKey(Issue)
    filename = models.CharField(max_length=255)
    filedesc = models.CharField(max_length=255)
    filesize = models.IntegerField()
    filetype = models.CharField(max_length=32)
    filehash = models.CharField(max_length=32)
    
class IssueComment(models.Model):
    title = models.CharField(max_length=255)
    contents = models.TextField()
    author = models.ForeignKey(User)
    published = models.DateField()
    