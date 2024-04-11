from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserLoginForm


# Create your views here.

def home(request):
    return render(request, 'user/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login_view')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register_view.html', context={'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
            return redirect('user:home')
    else:
        form = UserLoginForm()
    return render(request, 'user/login_view.html', context={'form': form})

def profile(request, user_id):
    if request.method == 'POST':
        form = register_view(request.POST)
        if form.is_valid():
            form.save()
            return redirect('goni_bablo:home')
    else:
        user = User.objects.get(id=user_id)
        return render(request, 'registration/profile.html', context={'user':user})
