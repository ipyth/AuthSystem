# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import login
from views import logout_view


urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
]
