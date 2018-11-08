from django.urls import path
from user import views as user_views

urlpatterns = [
    path('', user_views.user, name='user-home'),
]
