from django.contrib import admin
from django.urls import *
from .views import*

urlpatterns = [
    path('',home, name='home'),
    path('shop/',shop, name='shop'),
    path('detail/',detail, name='detail'),
    path('contact/',contact, name='contact'),
    path('cart/',cart, name='cart'),
    path('checkout/',checkout, name='checkout'), 
    
]
