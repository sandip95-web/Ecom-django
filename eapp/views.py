from django.shortcuts import render,redirect,HttpResponse
from . models import Product,Category,Cart
from django.contrib import messages
from . models import Customer_account
from django.http import JsonResponse

# Create your views here.
def home(request):
    if request.session.get('is_authenticated',False):
        products=None
        categories=Category.objects.all()
        category_id=request.GET.get('category')
        
        if category_id:
            products=Product.objects.filter(category=category_id)
        else:
            products=Product.objects.all()
        return render(request,'home.html',{'products':products,'categories':categories})
    else:
        return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def signin(request):
    if request.method=="POST":
        full_name=request.POST.get('name')
        password=request.POST.get('password1')
        mobile_number=request.POST.get('mobile')
        confirm_password=request.POST.get('password2')
        check_account_exist=Customer_account.objects.filter(mobile_number=mobile_number)
        if check_account_exist:
            messages.warning(request,'Mobile Number already taken please user another one')
            return redirect('signin')
        if(password!=confirm_password):
            messages.warning(request,"Confirm password should be same as Password")
            return redirect('signin')
        else:
            customer=Customer_account(full_name=full_name,password=password,mobile_number=mobile_number)
            customer.save()
            messages.success(request,"Successfully Registered")
            return redirect('signin') 
    return render(request,'signin.html')

def login(request):
    if request.method=="POST":
        mobile_number=request.POST.get('mobile')
        password=request.POST.get('password')
        user=Customer_account.objects.filter(mobile_number=mobile_number,password=password).first()
        if user is not None:
            
            request.session['is_authenticated'] = True
            request.session['phone']=mobile_number
            
            messages.success(request,"Welcome to our Eshop")
            return redirect('home')
        else:
            messages.success(request,"Something Went Wrong Please Try again")
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    messages.success(request,"Successfully Logged out")
    request.session['user_id'] =None
    request.session.pop('is_authenticated',None)
    return redirect('login')

def productdetail(request,pk):
    product=Product.objects.get(pk=pk)
    phone=request.session['phone']
    item_in_cart=Cart.objects.filter(product=product.id,phone=phone)
    return render(request,'productdetail.html',{'product':product,'item_in_cart':item_in_cart})
    
def add_to_cart(request,pk):
    phone=request.session['phone']
    print(pk)
    if pk is None:
        # Return an error response or redirect to a custom error page
        return HttpResponse('Invalid product ID')
    product_name=Product.objects.get(id=pk)
    product=Product.objects.filter(id=pk)
    for i in product:
        image=i.image
        price=i.price
        cart=Cart(phone=phone,product=product_name,image=image,price=price)
        cart.save()
    return redirect('cart_to')  

def cart(request):
    totalprice=0
    alltotal=0
    if request.session.get('is_authenticated',False):
        phone=request.session['phone']
        totalitem=len(Cart.objects.filter(phone=phone))
        allcart=Cart.objects.all()
        for i in allcart:
            alltotal+=i.total
        customer=Customer_account.objects.filter(mobile_number=phone)
        
        for i in customer:
            name=i.full_name
            cart=Cart.objects.filter(phone=phone)
            for c in cart:
                if(c.quantity==0):
                    c.total=0
                else:
                    c.total=c.price * c.quantity
                c.save()
            return render(request,'cart.html',{'cart':cart,'name':name,'alltotal':alltotal})
    else:
        messages.warning(request,"You must Be Logged In To view this page")
        return redirect('home')
    
def plus_cart(request):
    if request.session.get('is_authenticated',False):
        phone=request.session['phone']
        product_id=request.GET.get('product_id')
        cart=Cart.objects.get(phone=phone,product=product_id)
        if(cart.quantity<20):
            cart.quantity+=1
        cart.save()
        return redirect('cart_to')
        
    
        

def minus_cart(request):
    if request.session.get('is_authenticated',False):
        phone=request.session['phone']
        product_id=request.GET.get('product_id')
        cart=Cart.objects.get(phone=phone,product=product_id)
        if(cart.quantity>0):
               cart.quantity-=1
        
        
        cart.save()
        return redirect('cart_to')

def remove_cart(request):
    if request.session.get('is_authenticated',False):
        phone=request.session['phone']
        product_id=request.GET.get('product_id')
        cart=Cart.objects.get(phone=phone,product=product_id)   
        cart.delete()
        return redirect('cart_to')