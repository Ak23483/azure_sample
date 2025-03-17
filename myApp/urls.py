from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import login_view

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('register/', views.register_view, name='register'),
    path('login/', login_view, name='login'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
     path('login/', views.login_view, name='login'),

    path('', views.index, name='index'),

]