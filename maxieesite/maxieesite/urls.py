from django.conf.urls import patterns, include, url
from helloworld.views import hello, current_datetime, hours_ahead

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$',hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
)

#^: require that the pattern matches the start of the string.
#$: require that the pattern matches the end of the string.
