from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import PatientForm

@login_required
def user(request):
    return render(request, 'user/user.html')

@login_required
def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'user/user.html')
        else:
            return render(request, 'user/user.html')
    else:
        form = PatientForm()
        return render(request, 'user/addPatient.html', {'form': form})

    