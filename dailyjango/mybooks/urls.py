# -*- coding: utf-8 -*-
"""
author : xiaoge
company: LogInsight
email_ : duchao@loginsight.cn
file: urls.py
time   : 16/3/25 下午12:24  
"""
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^hello/',views.hello),
]