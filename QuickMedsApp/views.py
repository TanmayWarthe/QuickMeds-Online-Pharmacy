from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile, Product, WishlistItem
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'base.html')

def home(request):
    try:
        if request.user.is_authenticated:
            wishlist_count = WishlistItem.objects.filter(user=request.user).count()
        else:
            wishlist_count = 0
    except:
        wishlist_count = 0
    return render(request, 'home.html', {'wishlist_count': wishlist_count})

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

@login_required
def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user).select_related('product')
    context = {
        'wishlist_items': wishlist_items,
        'wishlist_count': wishlist_items.count()
    }
    return render(request, 'wishlist.html', context)

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    messages.success(request, 'Product added to wishlist!')
    return redirect('product_detail', pk=product_id)

@login_required
def remove_from_wishlist(request, wishlist_id):
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_id, user=request.user)
    wishlist_item.delete()
    messages.success(request, 'Product removed from wishlist!')
    return redirect('wishlist')

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    # Placeholder for cart functionality
    messages.success(request, 'Product added to cart successfully!')
    return redirect('wishlist')

def contact(request):
    # Placeholder for contact page
    return render(request, 'contact.html')