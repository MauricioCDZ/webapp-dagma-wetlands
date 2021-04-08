""" from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm





class UserRegisterForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    #subject = forms.CharField(max_length=256)
    #message = forms.CharField(widget=forms.Textarea)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
       
        model = User
        fields = ['name','email', 'password1', 'password2']



from django import forms


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=256)
    message = forms.CharField(widget=forms.Textarea) 
"""
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import  CustomUser

class UserAdminCreationForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = get_user_model()
        #fields = ['email']
        fields = ['name','email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    name = forms.CharField()
    class Meta:
        model = CustomUser
        fields = ['name','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']