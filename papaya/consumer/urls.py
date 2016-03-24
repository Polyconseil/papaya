from django.conf.urls.defaults import *

urlpatterns = patterns('papaya.consumer.views',
    (r'^login/$', 'startOpenID'),
    (r'^finish/$', 'finishOpenID'),
    (r'^xrds/$', 'rpXRDS'),
)
