from django.contrib import admin
from models import *

admin.site.register(WikiPage)
admin.site.register(WikiRevision)
admin.site.register(WikiFile)