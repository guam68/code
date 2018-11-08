from django.urls import path
from register import views as register_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_views.register, name='register')
]