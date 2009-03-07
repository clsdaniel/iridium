from django import template
import re

bugre = re.compile("#(?P<id>\d+)")
bugalt = re.compile("issue:(?P<id>\d+)")
gittag = re.compile("\[(?P<repo>[\d\w]*):(?P<id>[\d\w]{5,32})\]")
gitalt = re.compile("git:(?P<repo>[\d\w]*):(?P<id>[\d\w]{5,32})")

register = template.Library()

@register.filter
def lookup(value, arg):
    return arg[value]

@register.filter
def traclinks(value, pid):
    pos = 0
    match = bugre.search(value, pos)
    
    while match:
        iid = match.group('id')
        srep = match.group()
        value = value.replace(srep, "<a href='/i/%s/%s'>Issue %s</a>" % (pid, iid, iid))
        pos = match.end()
        match = bugre.search(value, pos)
        
    pos = 0
    match = bugalt.search(value, pos)
    
    while match:
        iid = match.group('id')
        srep = match.group()
        value = value.replace(srep, "<a href='/i/%s/%s'>Issue %s</a>" % (pid, iid, iid))
        pos = match.end()
        match = bugalt.search(value, pos)
    
    pos = 0
    match = gittag.search(value, pos)
    
    while match:
        iid = match.group('id')
        repo = match.group('repo')
        srep = match.group()
        value = value.replace(srep, "<a href='/s/%s/%s/%s'>Revision %s</a>" % (pid, repo, iid, iid))
        pos = match.end()
        match = gittag.search(value, pos)
    
    pos = 0
    match = gitalt.search(value, pos)
    
    while match:
        iid = match.group('id')
        repo = match.group('repo')
        srep = match.group()
        value = value.replace(srep, "<a href='/s/%s/%s/%s'>Revision %s</a>" % (pid, repo, iid, iid))
        pos = match.end()
        match = gitalt.search(value, pos)
            
    return value