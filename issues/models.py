# Copyright (c) 2009, Carlos Daniel Ruvalcaba Valenzuela
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice, 
#      this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, 
#      this list of conditions and the following disclaimer in the documentation 
#      and/or other materials provided with the distribution.
#    * Neither the name of the Blackchair Software nor the names of its contributors 
#      may be used to endorse or promote products derived from this software without 
#      specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES 
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT 
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, 
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from django.db import models
from django.contrib.auth.models import User
from iridium.project.models import Project

# Create your models here.
class Issue(models.Model):
    project = models.ForeignKey(Project)
    issuenumber = models.IntegerField()
    title = models.CharField(max_length=255)
    contents = models.TextField()
    issuetype = models.CharField(max_length=50)
    author = models.ForeignKey(User, related_name="issues_authored")
    published = models.DateField()
    assigned = models.ForeignKey(User, related_name="issues_assigned", null=True)
    priority = models.IntegerField()
    status = models.IntegerField()
    
class IssueFile(models.Model):
    issue = models.ForeignKey(Issue, related_name="files")
    filename = models.CharField(max_length=255)
    filedesc = models.CharField(max_length=255)
    filesize = models.IntegerField()
    filetype = models.CharField(max_length=32)
    filehash = models.CharField(max_length=32)
    
class IssueComment(models.Model):
    issue = models.ForeignKey(Issue, related_name="comments")
    title = models.CharField(max_length=255)
    contents = models.TextField()
    author = models.ForeignKey(User)
    published = models.DateField()
    