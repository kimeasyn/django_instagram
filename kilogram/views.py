from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView  #template를 그대로 보여줌
from django.views.generic.edit import CreateView    #object 생성하는 view
#from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UploadForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
#login한 사람만 url을 볼 수 있게
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit = False)   #photo 객체를 form 에서 가져오지만 db에는 저장하지 않음
            photo.owner = request.user
            form.save()
            return redirect('kilogram:index')
    form = UploadForm
    return render(request, 'kilogram/upload.html', {'form':form})

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
