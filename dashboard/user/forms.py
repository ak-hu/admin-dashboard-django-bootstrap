from django import forms
from django.contrib.auth.forms import AuthenticationForm, User

from .models import *


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class AddUserForm(forms.ModelForm):
    username = forms.CharField(required=True, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, label='Surname', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(required=False, label='Date of Birth',
                          widget=forms.SelectDateWidget(years=range(1960, 2021), attrs={'class': 'form-select'}))

    country = forms.CharField(required=False, label='Country', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(required=False, label='Phone number',
                            widget=forms.NumberInput(attrs={'type': 'text', 'class': 'form-control'}))

    password = forms.CharField(required=True, label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(required=True, label='Repeat password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Main
        fields = ['username', 'first_name', 'last_name', 'email', 'dob', 'country', 'address', 'phone',
                  'password', 'password1']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(label='Date of Birth',
                          widget=forms.SelectDateWidget(years=range(1960, 2021), attrs={'class': 'form-select'}))

    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone number',
                            widget=forms.NumberInput(attrs={'type': 'text', 'class': 'form-control'}))

    password = forms.CharField(label='New password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label='Repeat new password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Main
        fields = ('username', 'first_name', 'last_name', 'email', 'dob', 'country', 'address', 'phone',
                  'password', 'password1')

