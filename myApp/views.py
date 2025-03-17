
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import CustomAuthenticationForm
from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def shop(request):
    return render(request, 'shop.html')
def register(request):
    return render(request, 'register.html')
def wishlist(request):
    # Add any necessary logic for the wishlist here
    return render(request, 'wishlist.html')

def cart(request):
    # Add any necessary logic for the cart here
    return render(request, 'cart.html')

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('index')  # Redirect to the index page after successful login
        else:
            messages.error(request, 'Invalid email or password.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Add a success message
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')  # Redirect to login page with success message
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})