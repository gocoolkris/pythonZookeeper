from django.conf.urls import patterns, include, url
from django.contrib import admin
import zapp

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyzoo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
  #  url(r'^$',zapp.views.search,name='home'),
    url(r'^zapp/', include('zapp.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
