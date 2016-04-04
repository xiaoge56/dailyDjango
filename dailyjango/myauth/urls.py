# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: urls.py
time   : 16/4/4 下午12:06  
"""

from django.conf.urls import include, url
from . import views


urlpatterns = [


    url(r'^$',views.register,name="register"),
    url(r'^registrationok/$',views.registration_ok,name='registration_ok'),
    url(r'^mylogin/$',views.mylogin,name='login'),
    url(r'^logout/$',views.mylogout,name='logout'),

    # url(r'^(?P<question_id>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultView.as_view(), name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'')
]