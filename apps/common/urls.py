from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, url, include
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api-token-auth/', authtoken_views.obtain_auth_token),
)

urlpatterns += patterns(
    'django.views.static',
    url(r'^static/(.*)$', 'serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(.*)$', 'serve', {'document_root': settings.MEDIA_ROOT}),
)
