from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
class AddNews(forms.Form):
    theme = forms.CharField(label='Mavzu',max_length = 300)
    text = forms.CharField(label='Text',max_length = 1000)
    tag = forms.CharField(label='Hashtag',max_length=50)
    image = forms.ImageField(label='Rasm yuklash')
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length = 150)
    password = forms.CharField(label='Text',max_length = 200)
class PostNews(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
class ProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
