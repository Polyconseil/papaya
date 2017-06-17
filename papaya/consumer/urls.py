from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.startOpenID),
    url(r'^finish/$', views.finishOpenID),
    url(r'^xrds/$', views.rpXRDS),
]
