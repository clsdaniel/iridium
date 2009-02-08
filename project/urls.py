from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'(?P<pid>[\d\w]*)', 'iridium.project.views.viewProject'),
)
