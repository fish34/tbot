# -*- coding: utf8 -*-

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('^admin/', admin.site.urls),
    path(r'^planet/', include('py_planet.urls', namespace='planet')),
]