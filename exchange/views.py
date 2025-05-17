from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Skill

def home(request):
    skills = Skill.objects.all()
    return render(request, 'exchange/home.html', {'skills': skills})

def signup_view(request):
    if request.method == 'POST':
        User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        return redirect('login')
    return render(request, 'exchange/signup.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'exchange/login.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'exchange/dashboard.html', {'skills': skills})

def post_skill(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        Skill.objects.create(
            user=request.user,
            skill_offered=request.POST['skill_offered'],
            skill_needed=request.POST['skill_needed'],
            description=request.POST['description']
        )
        return redirect('dashboard')
    return render(request, 'exchange/post_skill.html')
