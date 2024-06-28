# social/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'social/home.html')

@login_required
def dashboard(request):
    if request.method == 'POST':
        # Handle status post
        pass
    return render(request, 'social/dashboard.html')

@login_required
def profile(request):
    return render(request, 'social/profile.html')

@login_required
def messages(request):
    return render(request, 'social/messages.html')
