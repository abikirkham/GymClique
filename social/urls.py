# social/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('messages/', views.messages, name='messages'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
]

