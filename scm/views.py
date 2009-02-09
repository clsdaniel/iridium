# Python Imports
import datetime
import os
import git

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


def getProject(pid):
    if pid.isdigit():
        proj = Project.objects.get(id=int(pid))
    else:
        proj = Project.objects.get(name=pid.lower())
    return proj

@template('scm_list.html')
def listRepos(request, pid):
    proj = getProject(pid)
    
    if proj.repository_set.count() < 2:
        pass
    repos = proj.repository_set.all()
    
    return dict(section='scm', pid=pid, repos=repos)
