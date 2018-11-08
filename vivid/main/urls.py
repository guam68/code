from django.urls import path
from main import views as main_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', main_views.home, name='main-home'),
    # path('', auth_views.LoginView.as_view(template_name='main/home.html'), name ='main-home'),
]
