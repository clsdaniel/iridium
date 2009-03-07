from django import template
import re

bugre = re.compile("#(?P<id>\d+)")
bugalt = re.compile("issue:(?P<id>\d+)")
gittag = re.compile("\[(?P<repo>[\d\w]*):(?P<id>[\d\w]{5,40})\]")
gitalt = re.compile("git:(?P<repo>[\d\w]*):(?P<id>[\d\w]{5,40})")

register = template.Library()

@register.filter
def lookup(value, arg):
    return arg[value]

@register.filter
def firstline(value):
    lines = value.split('\n', 1) 
    if len(lines) == 1:
        return value
    return lines[0]

@register.filter
def traclinks(value, pid):
    pos = 0
    match = bugre.search(value, pos)
    
    def bugreplace(match):
        bid = match.group('id')
        return "<a href='/i/%s/%s'>%s</a>" % (pid, bid, match.group())
    
    value = bugre.sub(bugreplace, value)
    value = bugalt.sub(bugreplace, value)
    
    def gitreplace(match):
        rid = match.group('id')
        repo = match.group('repo')
        return "<a href='/s/%s/%s/diff/%s'>%s</a>" % (pid, repo, rid, match.group())
    value = gittag.sub(gitreplace, value)
    value = gitalt.sub(gitreplace, value)
            
    return value