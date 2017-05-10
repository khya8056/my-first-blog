from django.conf.urls import url,include
from . import views
from django.contrib import admin
app_name='home'
urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^bar$', views.bar, name='bar'),
    url(r'^beam$', views.beam, name='beam'),
    url(r'^vault$', views.vault, name='vault'),
    url(r'^floor$', views.floor, name='floor'),
    url(r'^extra$', views.extra, name='extra'),
]
