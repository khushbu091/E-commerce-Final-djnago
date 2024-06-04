from django.shortcuts import render
from .models import User,ItemInfo
from django.db.models import Q
from .forms import ItemInfoForm
import razorpay
from django.views.decorators.csrf import csrf_exempt
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
      
def add_product(request):
    if request.method=="POST":
        form = ItemInfoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        data = ItemInfo.objects.all()
        return render(request,'add_product.html',{'form':form,'data':data})
    form = ItemInfoForm()
    data = ItemInfo.objects.all()
    if data:
        return render(request,'add_product.html',{'form':form,'data':data})
    else:
        return render(request,'add_product.html',{'form':form})
def addtocard(request,pk):
    if request.method == 'POST':
        quantity = request.session.get('quantity', [])
        quantity1 =int(request.POST.get('quantity'))
        quantity.append(quantity1)
        # print("quantity :",quantity)
        request.session['quantity'] = quantity
        cart = request.session.get('cart', [])
        cart.append(pk)
        request.session['cart'] = cart
        form = ItemInfoForm()
        data = ItemInfo.objects.all()
        return render(request,'add_product.html',{'form':form,'data':data})
        # return redirect('home')

def showcart(request):
    cart = request.session.get('cart',[])
    quantity = request.session.get('quantity',[])
    # print("Cart :",cart)
    # print("Quantity :",quantity)
    # print(len(cart))
    alldata = []
    i=0
    j=0
    total=0
    while i < len(cart):
        data = ItemInfo.objects.get(id=cart[i])
        print(quantity[j])
        total = total + (data.item_price)*quantity[j]
        # print(data.id)
        # print(data.iten_name)
        # print(data.item_desc)
        # print(data.item_price)
        # print(data.item_image)
        alldata.append({
            'id':data.id,
            'iten_name':data.iten_name,
            'item_desc':data.item_desc,
            'item_price':data.item_price,
            'item_image':data.item_image,
            'item_quantity':quantity[j]
        })
        i+=1
        j+=1
    # print("Total Amount = ",total)
    # print(alldata)
    return render(request,'showcart.html',{'key':alldata,'amount':total})
def deletecart(request,pk):
    cart = request.session.get('cart',[])
    quantity = request.session.get('quantity',[])
    print("Cart :",cart)
    print("Quantity :",quantity)
    print("pk=",pk)
    x = cart.index(pk)
    # print("Cart index no:",x)
    # y = quantity[x]
    # print("Quantity of that card index:",y)
    cart1=[]
    y = len(cart)   
    i=0
    while i<y:
        if i==x:
            pass
        else:
            cart1.append(cart[i])
        i+=1
    print(cart1)
    request.session['cart']=cart1
    quantity1=[]
    z = len(quantity)
    j=0
    while j<z:
        if j==x:
            pass
        else:
            quantity1.append(quantity[j])
        j+=1
    print(quantity1)
    request.session['quantity']=quantity1
    # ----------------------------------------------------
    cart = request.session.get('cart',[])
    quantity = request.session.get('quantity',[])
    print("Cart :",cart)
    print("Quantity :",quantity)
    # print(len(cart))
    alldata = []
    i=0
    j=0
    total=0
    while i < len(cart):
        data = ItemInfo.objects.get(id=cart[i])
        print(quantity[j])
        total = total + (data.item_price)*quantity[j]
        # print(data.id)
        # print(data.iten_name)
        # print(data.item_desc)
        # print(data.item_price)
        # print(data.item_image)
        alldata.append({
            'id':data.id,
            'iten_name':data.iten_name,
            'item_desc':data.item_desc,
            'item_price':data.item_price,
            'item_image':data.item_image,
            'item_quantity':quantity[j]
        })
        i+=1
        j+=1
    # print("Total Amount = ",total)
    print(alldata)
    return render(request,'showcart.html',{'key':alldata,'amount':total})

def payment(request):
    global payment
    if request.method=="POST":
        # amount in paisa
        amount = int(request.POST.get('amount')) * 100
        
        client = razorpay.Client(auth =("rzp_test_pr99iascS1WRtU" , "UTDIzPGwICnAssu3Q3lk7zUi"))
        # create order
        
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        product = Product.objects.create( amount =amount , order_id = payment['id'])
        cart = request.session.get('cart',[])
        quantity = request.session.get('quantity',[])
        alldata = []
        i=0
        j=0
        total=0
        while i < len(cart):
            data = ItemInfo.objects.get(id=cart[i])
            total = total + (data.item_price)*quantity[j]
            alldata.append({
                'id':data.id,
                'iten_name':data.iten_name,
                'item_desc':data.item_desc,
                'item_price':data.item_price,
                'item_image':data.item_image,
                'item_quantity':quantity[j]
            })
            i+=1
            j+=1
        # print(payment)
        return render(request,'app/cart.html',{'key':alldata,'amount':total,'payment':payment})
    
@csrf_exempt
def payment_status(request):
       if request.method=="POST": 
        response = request.POST
        print(response) #  
        print(payment)

        razorpay_data = {
            'razorpay_order_id': response['razorpay_order_id'],
            'razorpay_payment_id': response['razorpay_payment_id'],
            'razorpay_signature': response['razorpay_signature']
        }

        # client instance
        client = razorpay.Client(auth =("rzp_test_pr99iascS1WRtU" , "UTDIzPGwICnAssu3Q3lk7zUi"))

        try:
            status = client.utility.verify_payment_signature(razorpay_data)
            product = Product.objects.get(order_id=response['razorpay_order_id'])
            product.razorpay_payment_id = response ['razorpay_payment_id']
            product.paid = True
            product.save()
            
            return render(request, 'app/success.html', {'status': True})
        except:
            return render(request, 'app/success.html', {'status': False})