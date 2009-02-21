from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'(?P<pid>[\d\w]*)/new', 'iridium.wiki.views.newPage'),
    (r'(?P<pid>[\d\w]*)/(?P<wid>[\d\w]*)/edit', 'iridium.wiki.views.editPage'),
    (r'(?P<pid>[\d\w]*)/(?P<wid>[\d\w]*)/uploadFile', 'iridium.wiki.views.uploadFile'),
    (r'(?P<pid>[\d\w]*)/(?P<wid>[\d\w]*)', 'iridium.wiki.views.viewPage'),
    (r'(?P<pid>[\d\w]*)', 'iridium.wiki.views.viewWiki'),
)
