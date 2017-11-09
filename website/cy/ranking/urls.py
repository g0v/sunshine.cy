# -*- coding: utf-8 -*-
from django.conf.urls import url
from ranking import views

urlpatterns = [
    url(r'^people/(?P<index>stock|land|building|car|cash|deposit|bonds|fund|otherbonds|antique|insurance|claim|debt|investment)/$', views.ranking_people_by_property, name='ranking_people_by_property'),
    url(r'^property/(?P<index>stock)/$', views.ranking_property, name='ranking_property'),
]
