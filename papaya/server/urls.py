
from django.conf.urls.defaults import *

urlpatterns = patterns('papaya.server.views',
    (r'^$', 'server'),
    (r'^xrds/$', 'idpXrds'),
    (r'^processTrustResult/$', 'processTrustResult'),
    (r'^endpoint/$', 'endpoint'),
    (r'^trust/$', 'trustPage'),
    (r'^(?P<user>\w+)', 'idPage'),
)
