from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']



class LoginForm(forms.Form):
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
    # class Meta:
    #     model = User
    #     fields = ['email', 'password']