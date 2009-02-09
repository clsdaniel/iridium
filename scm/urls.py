from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'(?P<pid>[\d\w]*)/(?P<wid>[\d\w]*)', 'iridium.scm.views.viewRepo'),
    (r'(?P<pid>[\d\w]*)', 'iridium.scm.views.listRepos'),
)
