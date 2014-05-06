from django.conf.urls import patterns, include, url
from maxieesite import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maxieesite.views.home', name='home'),
    # url(r'^maxieesite/', include('maxieesite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^polls/$', views.index, name = 'index'),

    url(r'^polls/(?P<poll_id>\d+)/$', views.detail, name = 'detail'),

    url(r'^polls/(?P<poll_id>\d+)/results/$', views.results, name='results'),

    url(r'^polls/(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
