
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.server),
    url(r'^xrds/$', views.idpXrds),
    url(r'^processTrustResult/$', views.processTrustResult),
    url(r'^endpoint/$', views.endpoint),
    url(r'^trust/$', views.trustPage),
    url(r'^(?P<user>\w+)', views.idPage),
]
