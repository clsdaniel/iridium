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
def trimpath(value):
    marker = value.rfind("/")
    if marker > 0:
        return value[0:marker]
    return ""

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