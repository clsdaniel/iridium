from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'(?P<pid>[\d\w]*)/new', 'iridium.issues.views.newIssue'),
    (r'(?P<pid>[\d\w]*)/(?P<sid>[\d\w]*)', 'iridium.issues.views.viewIssue'),
    (r'(?P<pid>[\d\w]*)', 'iridium.issues.views.listIssues'),
)
