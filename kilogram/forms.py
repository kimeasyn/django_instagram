from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Photo

class CreateUserForm(UserCreationForm):
        email = forms.EmailField(required = True)

        class Meta:
            model = User
            fields = ("username", "email", "password1", "password2")

        def save(self, commit=True):
            user = super(CreateUserForm, self).save(commit=False)
            #commit=False:2번 저장하는것을 막기위해 우선 데이터를 가져온 후 저장하려고
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user

class UploadForm(forms.ModelForm):
    #comment = forms.CharField(max_length=255)
    #필드를 써도되고 모델을 연결해도됨
    class Meta:
        model = Photo
        exclude = ('thumnail_image', 'owner')
        #쓸거만 지정해도 되고 안쓸거만 지정해도 됨
