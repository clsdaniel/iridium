from django.db import models
from iridium.project.models import Project

# Create your models here.
class WikiPage(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(max_length=120)
    title = models.CharField(max_length=255)
    published = models.DateField()
    
    def __unicode__(self):
        return self.name
    
class WikiRevision(models.Model):
    page = models.ForeignKey(WikiPage)
    contents = models.TextField()
    published = models.DateField()
    
    def __unicode__(self):
        return "<Revision %s>" % self.published
    
class WikiFile(models.Model):
    page = models.ForeignKey(WikiPage, related_name='files')
    filename = models.CharField(max_length=255)
    filesize = models.IntegerField()
    filetype = models.CharField(max_length=32)
    filehash = models.CharField(max_length=32)
    has_thumbnail = models.BooleanField()
    
    def __unicode__(self):
        return self.filename
