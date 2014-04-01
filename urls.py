from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

import views

urlpatterns = patterns('',
    url(r'^math/$', views.index, name='math_index'),
    url(r'^math/(\d+)/$', views.facts, name='math_facts'),
)
