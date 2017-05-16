from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'kilogram'
urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    #generic view
    #class 라서 @login_required를 쓸 수 없을때 url.py에 해줌 mysite의 url.py에도 똑같이 해줘야함
    url(r'^upload$', views.upload, name = 'upload'),
    #function based view
]
