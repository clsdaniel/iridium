# Python Imports
import datetime
import md5
import os

import simplejson

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

def getWiki(wid):
    if wid.isdigit():
        wiki = WikiPage.objects.get(id=int(wid))
    else:
        wiki = WikiPage.objects.get(name=wid.lower())
    return wiki

@login_required
@template("wiki_list.html")
def viewWiki(request, pid):
    proj = getProject(pid)
        
    pages = proj.wikipage_set.all()
    return dict(section='wiki', pid=pid, title=proj.name, pages=pages)

@login_required
@template("generic_form.html")
def newPage(request, pid):
    if request.method == "POST":
        form = NewPageForm(request.POST)
    else:
        form = NewPageForm()
    
    if form.is_valid():
        proj = getProject(pid)
        data = form.clean()
        title = data['name']
        name = title.replace(' ', "_").replace(":", "_").replace("-", "_").lower()
        wiki = WikiPage(name=name.lower(), title=title, project=proj, published=datetime.datetime.now())
        wiki.save()
        return HttpResponseRedirect('/w/%s/%s/edit' % (pid, name))
        
    return dict(section='wiki', pid=pid, title="New page", form=form)

@login_required
@template("wiki_edit.html")
def editPage(request, pid, wid):
    wiki = getWiki(wid)
    
    if request.method == "POST":
        form = EditPageForm(request.POST)
        
        if form.is_valid():
            data = form.clean()
            published = datetime.datetime.now()
            rev = wiki.wikirevision_set.create(contents=data['contents'], published=published)
            wiki.title = data['title']
            wiki.published = published
            rev.save()
            wiki.save()
            return HttpResponseRedirect('/w/%s/%s' % (pid, wiki.id))
    else:
        try:
            rev = wiki.wikirevision_set.order_by('-id')[0]
            form = EditPageForm(dict(contents=rev.contents, title=wiki.title))
        except: 
            form = EditPageForm(dict(title=wiki.title))
    
    return dict(section='wiki', pid=pid, wid=wid, title="Edit: %s" % wiki.name, form=form)

@login_required
@template("wiki_view.html")
def viewPage(request, pid, wid):
    wiki = getWiki(wid)
    
    try:
        rev = wiki.wikirevision_set.order_by('-id')[0]
    except:
        return HttpResponseRedirect('/w/%s/%i/edit' % (pid, wiki.id))
    
    return dict(section='wiki', pid=pid, wid=wid, title=wiki.title, contents=rev.contents)

@login_required
def uploadFile(request, pid, wid):
    if request.method != "POST":
        return HttpResponseRedirect('/')

    wiki = getWiki(wid)
    
    fd = request.FILES['fileupload']
    outfd = file('static/upload/stage-%s' % fd.name, 'w')
    md5hash = md5.md5()
    
    for chunk in fd.chunks():
        md5hash.update(chunk)
        outfd.write(chunk)
        
    fd.close()
    
    filehash = md5hash.hexdigest()
    os.rename('static/upload/stage-%s' % fd.name, 'static/upload/%s' % filehash)
    
    wfile = wiki.files.create(filename=fd.name, filesize=fd.size, 
                              filetype=fd.content_type,
                              filehash=filehash)
    wfile.save()
    wiki.save()

def getFileType(mime):
    if mime.find('image') != -1:
        return 'image'
    else:
        return 'file'
    
@login_required
def wikiFiles(request, pid, wid):
    wiki = getWiki(wid)
    files = wiki.files.all()
    
    items = dict(items=[dict(name=fd.filename, 
                             hash=fd.filehash, 
                             filetype=getFileType(fd.filetype)) 
                        for fd in files])
    
    return HttpResponse(simplejson.dumps(items))
        

