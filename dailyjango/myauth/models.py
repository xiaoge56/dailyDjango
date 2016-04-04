from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
# Create your models here.

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.context_processors import csrf


# class UserForm(ModelForm):
#     class Meta:
#         model = User
#
#
# class UserProfileForm(ModelForm):
#     class Meta:
#         model = user
#         exclude = ['user']


class UserCreateForm(UserCreationForm):

    username = forms.CharField(label="Your Username")
    password1 = forms.CharField(label="Your Password")
    password2 = forms.CharField(label="Confirm Your Password")
    email = forms.EmailField(label = "Email Address")
    first_name = forms.CharField(label = "firstname")
    last_name = forms.CharField(label = "lastname")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "email", )

    def save(self, commit=True):
        user = super(UserCreationForm,self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
            return user

