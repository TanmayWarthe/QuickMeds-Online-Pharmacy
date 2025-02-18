from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, UserProfile

# Create your views here.
# This is the view for the base.html template
from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')


def product_view(request):
    return render(request, 'product.html')

def login_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if action == 'register':
            # Handle registration
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('login')
            
            name = request.POST.get('name')
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=name
            )
            UserProfile.objects.create(user=user)
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
            
        elif action == 'login':
            # Handle login
            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login successful!')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid credentials')
            except User.DoesNotExist:
                messages.error(request, 'User does not exist')
            
        return redirect('login')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def about_view(request):
    return render(request, 'about.html')