from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),
    url(r'^vote_next$', 'app.views.vote_next', name='vote_next'),
    url(r'^vote_keep$', 'app.views.vote_keep', name='vote_keep'),
    url(r'^admin/', include(admin.site.urls)),
)
