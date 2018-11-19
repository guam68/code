from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Patient(models.Model):
    SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.TextField(max_length=35, blank=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    diagnosis = models.TextField(blank=True)
    contact_name = models.TextField(max_length=25, blank=True) 
    contact_number = models.CharField(max_length=12, blank=True)

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'sex', 'diagnosis', 'contact_name', 'contact_number']