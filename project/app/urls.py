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
    path('register/',register, name='register'),
    path('registerdata/', registerdata, name='registerdata'),
    path('login/',login, name='login'), 
    path('logindata/', logindata, name='logindata'),
    path('add_product/', add_product, name='add_product'),
    path('showcart/', showcart, name='showcart'),
    path("addtocard/<int:pk>",addtocard,name='addtocard'),
    path("addtocart/",cart,name="cart"),
    path("deletecart/<int:pk>",deletecart,name='deletecart'),
    path("payment/",payment,name='payment'),
    path('payment-status', payment_status, name='payment-status')



    
]
