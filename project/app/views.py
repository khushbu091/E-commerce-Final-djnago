from django.shortcuts import render
from .models import User
from django.db.models import Q

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
def register(request):
    return render(request,'register.html')
def registerdata(request):
    name=request.POST.get('name')
    emails=request.POST.get('email')
    contact=request.POST.get('contact')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
   
    data=User.objects.filter(Email=emails)
    print(data)

    if data:
        msg="Emails already exist" 
        return render(request,'register.html',{'key':msg})
    else:
        if password==cpassword:
            User.objects.create(Name=name,
                                     Email=emails,
                                     Contact=contact,
                                     Password=password,
                                     
                                    )
            msg='registrations'

            return render(request,'login.html',{'key':msg})
        else:
            msg="password and Confirm Password not matched"
            return render(request,'register.html',{'key':msg})
        
def login(request):
    return render(request, 'login.html')

def logindata(request):
    emails=request.POST.get('email')
    password=request.POST.get('password')
    user=User.objects.filter(Email=emails)
    if user:
        data=User.objects.get(Email=emails)
        pss=data.Password
        if pss==password:
            context={
                
                'em':data.Email,
                'pass':data.Password,
                'logout':'logout'
            }
            return render(request,'home.html',{'context':context})
        else:
            msg='Enter valid emails'
            return render(request,'login.html',{'key':msg})
    else:
        msg="enter valid emails"
        return render (request,'login.html',{'key':msg})
      
