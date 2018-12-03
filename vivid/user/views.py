from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import PatientForm, Patient

@login_required
def user(request):
    patients = Patient.objects.all()
    numPatients = patients.count()
    return render(request, 'user/user.html', {'numPatients': numPatients, 'patients': patients})

@login_required
def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return user(request) 
        else:
            return render(request, 'user/user.html')
    else:
        form = PatientForm()
        return render(request, 'user/addPatient.html', {'form': form})

    