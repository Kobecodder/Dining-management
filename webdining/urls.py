from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from dining import views

urlpatterns = patterns('',
     url(r'^dining/', include('dining.urls')),
    # Examples:
    # url(r'^$', 'webdyning.views.home', name='home'),
    # url(r'^webdyning/', include('webdyning.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Login / logout.
    (r'^$', 'django.contrib.auth.views.login'),
    (r'^logout/$', views.logout_page),
)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT,}),
                        )