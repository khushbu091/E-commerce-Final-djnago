from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def shop(request):
    return render(request,'shop.html')
def contact(request):
    return render(request,'contact.html')
def cart(request):
    return render(request,'cart.html')
def detail(request):
    return render(request,'detail.html')
def checkout(request):
    return render(request,'checkout.html')