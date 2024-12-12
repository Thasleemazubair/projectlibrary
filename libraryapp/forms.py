from django import forms
from django.contrib.auth.management.commands.changepassword import UserModel
from django.contrib.auth.models import User
from django.db import  models
from . import models
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class AdminSignup(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['firstname', 'lastname', 'username', ' password']

class StudentUsedForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['enrollment','branch']




class AdminSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password1','password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone_number = True
        if commit:
            user.save()
        return user

