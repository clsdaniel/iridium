from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'(?P<pid>[\d\w]*)/(?P<rid>[\d\w]*)/diff/(?P<cid>[\d\w]*)', 'iridium.scm.views.viewDiff'),
    (r'(?P<pid>[\d\w]*)/(?P<rid>[\d\w]*)/t/(?P<tree>[\d\w/]*)', 'iridium.scm.views.viewTree'),
    (r'(?P<pid>[\d\w]*)/(?P<rid>[\d\w]*)/cat/(?P<tree>[\d\w/\.]*)', 'iridium.scm.views.viewFile'),
    (r'(?P<pid>[\d\w]*)/(?P<rid>[\d\w]*)/t', 'iridium.scm.views.viewTree'),
    (r'(?P<pid>[\d\w]*)/(?P<rid>[\d\w]*)', 'iridium.scm.views.viewRepo'),
    (r'(?P<pid>[\d\w]*)', 'iridium.scm.views.listRepos'),
)
