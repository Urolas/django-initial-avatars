# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import path
from .views import avatar

urlpatterns = [
    path('<int:id>/', avatar, name='avatar'),
    path('<int:id>/<int:size>/', avatar, name='avatar'),
]
