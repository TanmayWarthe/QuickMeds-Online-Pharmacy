from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if action == 'register':
            try:
                # Validate email
                validate_email(email)
                
                # Check if email exists
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already registered')
                    return redirect('login')
                
                # Get and validate name
                name = request.POST.get('name', '').strip()
                if not name:
                    messages.error(request, 'Name is required')
                    return redirect('login')
                
                # Validate password
                if len(password) < 8:
                    messages.error(request, 'Password must be at least 8 characters long')
                    return redirect('login')
                
                # Create user
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password,
                    first_name=name
                )
                
                # Create user profile
                UserProfile.objects.create(user=user)
                
                # Log user in
                login(request, user)
                messages.success(request, f'Welcome {name}! Your account has been created successfully.')
                return redirect('home')
                
            except ValidationError:
                messages.error(request, 'Please enter a valid email address')
            except Exception as e:
                messages.error(request, 'Registration failed. Please try again.')
            
        elif action == 'login':
            try:
                user = User.objects.get(email=email)
                user = authenticate(username=user.username, password=password)
                
                if user is not None:
                    login(request, user)
                    messages.success(request, f'Welcome back {user.first_name}!')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid password')
                    
            except User.DoesNotExist:
                messages.error(request, 'No account found with this email')
            except Exception as e:
                messages.error(request, 'Login failed. Please try again.')
        
        return redirect('login')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'profile.html')


def about_view(request):
    return render(request, 'about.html')

def cart_view(request):
    return render(request, 'cart.html')



