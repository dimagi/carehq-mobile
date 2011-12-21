from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^/$', 'carehq_mobile.views.carehq_mobile', name='carehq_mobile'),

)