from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^das-adminer/', include(admin.site.urls)),
    url(r'^', include('main.urls')),
)
