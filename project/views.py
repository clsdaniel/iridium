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
from models import *

@template("project_view.html")
def viewProject(request, pid):
    if pid.isdigit():
        proj = Project.objects.get(id=int(pid))
    else:
        proj = Project.objects.get(name=pid.lower())
        
    return dict(pid=pid, name=proj.name, desc=proj.desc)