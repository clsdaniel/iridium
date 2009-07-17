# Python Imports
import datetime
import os

from pyvcs.backends import get_backend
from pyvcs.exceptions import *

try:
    import pygments
    from pygments import highlight
    from pygments.lexers import guess_lexer, DiffLexer, PythonLexer
    from pygments.formatters import HtmlFormatter
    HAS_PYGMENTS = True
except:
    HAS_PYGMENTS = False

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

def getRepository(rid):
    if rid.isdigit():
        repo = Repository.objects.get(id=int(rid))
    else:
        repo = Repository.objects.get(title=rid.lower())
    return repo

@login_required
@template('scm_list.html')
def listRepos(request, pid):
    proj = getProject(pid)
    
    if proj.repository_set.count() < 2:
        pass
    repos = proj.repository_set.all()
    
    return dict(section='scm', pid=pid, repos=repos)

@login_required
@template('scm_changelog.html')
def viewRepo(request, pid, rid):
    mrepo = getRepository(rid)
    
    Backend = get_backend(mrepo.scm)
    repo = Backend.Repository(mrepo.path)
    commits = repo.get_recent_commits()
    
    return dict(section='scm', pid=pid, rid=rid, repo=mrepo, commits=commits)

@login_required
@template('scm_diff.html')
def viewDiff(request, pid, rid, cid):
    mrepo = getRepository(rid)
    
    Backend = get_backend(mrepo.scm)
    repo = Backend.Repository(mrepo.path)
    
    com = repo.get_commit_by_id(str(cid))
    diff = com.diff
    
    if HAS_PYGMENTS:
        try:
            lexer = guess_lexer(diff)
        except:
            lexer = DiffLexer()
        diff = highlight(diff, lexer, HtmlFormatter())
    else:
        pass
    
    return dict(section='scm', pid=pid, rid=rid, cid=cid, 
                repo=mrepo, diff=diff, commit=com, HAS_PYGMENTS=HAS_PYGMENTS)

@login_required
@template('scm_tree.html')
def viewTree(request, pid, rid, tree = None):
    if not tree:
        tree = ""
    mrepo = getRepository(rid)
    Backend = get_backend(mrepo.scm)
    repo = Backend.Repository(mrepo.path)
    
    files, folders = repo.list_directory(tree)
    
    return dict(section="scm", pid=pid, rid=rid, tree=tree, repo=mrepo, files=files, folders=folders)
    
@login_required
def viewFile(request, pid, rid, tree = None):
    if not tree:
        tree = ""
    mrepo = getRepository(rid)
    Backend = get_backend(mrepo.scm)
    repo = Backend.Repository(mrepo.path)
    
    return HttpResponse(repo.file_contents(str(tree)), "plain/text")
        