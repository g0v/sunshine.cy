# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from people import views

urlpatterns = patterns('',
    url(r'^(?P<name>.+)/property/(?P<index>overview|stock|land|building|car|cash|deposit|bonds|fund|otherbonds|antique|insurance|claim|debt|investment)/$', views.personal_property, name='personal_property'),
)
