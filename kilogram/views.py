from django.shortcuts import render
from django.views.generic.base import TemplateView  #template를 그대로 보여줌
# Create your views here.
class IndexView(TemplateView):
    template_name = 'kilogram/index.html'
