# Python Imports
import datetime
import md5
import os

# Django Imports
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
from django.forms.util import ErrorList

# Project imports
from iridium.utils.template import template_django as template
from iridium.utils.template import render_template
from iridium.project.models import Project

from models import *
from forms import *

def getProject(pid):
    if pid.isdigit():
        proj = Project.objects.get(id=int(pid))
    else:
        proj = Project.objects.get(name=pid.lower())
    return proj

@login_required
@template("issue_list.html")
def listIssues(request, pid):
    proj = getProject(pid)
    issues = proj.issue_set.all()
    
    return dict(section="issues", pid=pid, title=proj.name, issues=issues,
                di_priority=di_priority, di_status=di_status, di_type=di_type)


@login_required
@template("issue_view.html")
def viewIssue(request, pid, sid):
    proj = getProject(pid)
    try:
        issue = Issue.objects.get(id=int(sid))
    except:
        HttpResponseRedirect('/i/%s' % pid)
    
    return dict(section="issues", pid=pid, sid=sid, issue=issue, comments=issue.comments.all(),
                di_priority=di_priority, di_status=di_status, di_type=di_type)
    

@login_required
@template("generic_form.html")
def newIssue(request, pid):
    if request.method == "POST":
        form = NewIssueForm(request.POST)
    else:
        form = NewIssueForm()
    
    if form.is_valid():
        proj = getProject(pid)
        data = form.clean()
        data['author'] = request.user
        data['published'] = datetime.datetime.now()
        data['priority'] = int(data['priority'])
        data['status'] = int(data['status'])
        data['project'] = proj
        issue = proj.issue_set.create(**data)
        issue.save()
        proj.save()
        return HttpResponseRedirect('/i/%s/%i' % (pid, issue.id))
        
    return dict(section='issues', pid=pid, title="New issue", form=form)

@login_required
def commentIssue(request, pid, sid):
    if request.method != "POST":
        return HttpResponseRedirect("/")
    
    title = request.POST['title']
    contents = request.POST['contents']
    
    issue = Issue.objects.get(id=int(sid))
    comment = issue.comments.create(title=title, contents=contents,
                                    author=request.user, issue=issue,
                                    published=datetime.datetime.now())
    comment.save()
    issue.save()
    
    return HttpResponseRedirect('/i/%s/%i' % (pid, issue.id))