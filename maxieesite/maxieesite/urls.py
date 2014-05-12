from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$','helloworld.views.hello'),
)
#^: require that the pattern matches the start of the string.
#$: require that the pattern matches the end of the string.
