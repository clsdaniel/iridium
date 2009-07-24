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

from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string

# with thanks to Peter Hunt (http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/465427)
decorator_with_args = lambda decorator: lambda *args, **kwargs: lambda func: \
                      decorator(func, *args, **kwargs)

# with thanks to Robert Thomson (http://www.djangosnippets.org/snippets/459/)
@decorator_with_args
def template_django(func, template=None):
    def DJANGO_TEMPLATE(request, *args, **kwargs):
        res = func(request, *args, **kwargs)
        if not res:
            res = {}
        if type(res) == dict:
            try:
                return HttpResponse(render_to_string(template, res, RequestContext(request)))
            except:
                #if settings.DEBUG:
                #return HttpResponse("Templating Error", status=500)
                raise
        else:
            return res
    DJANGO_TEMPLATE.__name__ = func.__name__
    DJANGO_TEMPLATE.__doc__ = func.__doc__
    DJANGO_TEMPLATE.__dict__ = func.__dict__
    return DJANGO_TEMPLATE

def render_template(request, template, args={}):
    return HttpResponse(render_to_string(template, args, RequestContext(request)))