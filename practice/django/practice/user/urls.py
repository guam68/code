from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('user_login', views.user_login, name='user_login'),
    path('profile', views.profile, name='profile'),
    path('signup_process', views.signup, name='signup'),
    path('signup', views.signup_render, name='signup_render'),
    path('user_logout', views.user_logout, name='user_logout'),
]