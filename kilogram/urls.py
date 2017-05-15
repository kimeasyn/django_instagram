from django.conf.urls import url
from django.contrib import admin
from . import views
app_name = 'kilogram'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    #generic view
    url(r'^upload$', views.upload, name = 'upload'),
    #function based view
]
