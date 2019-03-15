from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class meta():
        model=User
        fields=('first_name','last_name','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class meta():
            model=UserProfileInfo
            fields=('dept','year')




