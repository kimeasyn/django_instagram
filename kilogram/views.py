from django.shortcuts import render
from django.views.generic.base import TemplateView  #template를 그대로 보여줌
from django.views.generic.edit import CreateView    #object 생성하는 view
#from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'kilogram/index.html'

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    #form_class = UserCreationForm
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')
    #generic view = reverse 대신 reverse_lazy 사용

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
