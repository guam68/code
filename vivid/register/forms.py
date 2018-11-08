from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               min_length=6,
                               widget=forms.TextInput(attrs={'class': 'form-input',
                               'placeholder': 'Name',
                               'name': 'name',
                               'id': 'name'}))
    email = forms.CharField(max_length=100,
                            widget=forms.EmailInput(attrs={'class': 'form-input',
                            'placeholder': 'Email',
                            'name': 'email',
                            'id': 'email'}))
    password = forms.CharField(max_length=100,
                               min_length=8, 
                               widget=forms.PasswordInput(attrs={'class': 'form-input',
                               'placeholder': 'Password',
                               'name': 'password',
                               'id': 'password'}))
    re_password = forms.CharField(max_length=100,
                                  min_length=8,
                                  widget=forms.PasswordInput(attrs={'class': 'form-input',
                                  'placeholder': 'Repeat your Password',
                                  'name': 're_password',
                                  'id': 're_password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 're_password']