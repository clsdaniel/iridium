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