from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.validators import validate_email

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        email = request.POST['email']
        try:
            validate_email(email)
            valid_email = True
        except:
            valid_email = False

        if form.is_valid() and valid_email == True:
            password = form.cleaned_data.get('password')
            re_password = form.cleaned_data.get('password')

            if password == re_password:
                email = form.cleaned_data.get('email')
                user, created = User.objects.get_or_create(username=form.cleaned_data.get('username'), email=email)
                messages.success(request, f'Account created for {email}!')
                user.set_password(password)
                user.save()
                return redirect('main-home')
            else:
                messages.error(request, 'There are problems with your form')
                form = RegistrationForm()
    else:
        form = RegistrationForm()
    return render(request, 'register/register.html', {'form': form})