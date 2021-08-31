from . import views

from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^create/new/$', views.index, name='create'),
]