from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Administration Django
    url(r'^admin/', include(admin.site.urls)),

    # Noyau de l'application
    url(r'^', include('Core.urls', namespace="Core")),
)
