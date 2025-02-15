from django.contrib import admin 
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('products/', views.product_view, name='products'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:wishlist_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('contact/', views.contact, name='contact'),
]
