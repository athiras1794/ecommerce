from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
from .models import Account,Category,Addproduct,Cart
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
     prod=Category.objects.all()
     return render(request,'index.html',{'prodct':prod})
    
def login1(request):
    return render(request,'login1.html')
def signup(request):
    return render(request,'signup.html')
def adminlogin(request):
     if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                # print('welcome')
                login(request,user)
                return redirect('admin_home')
            else:
                login(request,user)
                auth.login(request,user)
                # messages.info(request,f'welcome {username}')
                return redirect('user_home')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login1')
     return render(request,'login1.html')

@login_required(login_url='login1')   
def admin_home(request):
    prod=Category.objects.all()
    return render(request,'admin_home.html',{'prodct':prod})
@login_required(login_url='login1')   
def user_home(request):
    prshow=Addproduct.objects.all()
    prod=Category.objects.all()
   
    return render(request,'user_home.html',{'show':prshow,'prodct':prod})

def reg(request):
    if request.method =='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        pswd=request.POST['pass']
        cpswd=request.POST['cpass']
        email=request.POST['email']
        addr=request.POST['add']
        
        number=request.POST['cnum']
    
        img=request.FILES.get('img')
        if pswd==cpswd: 
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'This username already exists!!!!!!')
                return redirect('signup')
            else:
                 user=User.objects.create_user(
                    first_name=fname,
                    last_name=lname,
                    username=uname,
                    password=pswd,
                    email=email)
                 user.save()
                 u=User.objects.get(id=user.id)
                 reg=Account(address=addr,contact=number,img=img,user=u)
                 reg.save()
                 return redirect('index')
        else:
            messages.info(request,'password incorrect')
            return redirect('/')
@login_required(login_url='login1')        
def add_category(request):
    return render(request,'add_category.html')

@login_required(login_url='login1') 
def addcat(request):
    if request.method=='POST':
        cat=request.POST['cate']
        catg=Category(ca=cat)
        catg.save()
        return redirect('addproduct')
    
@login_required(login_url='login1') 
def addproduct(request):
    prod=Category.objects.all()
    return render(request,'addproduct.html',{'prodct':prod})

@login_required(login_url='login1') 
def proadd(request):
    if request.method=='POST':
        pr=request.POST['addp']
        des=request.POST['desc']
        price=request.POST['price']
        img=request.FILES.get('img')
        sel=request.POST['sel']
        cat=Category.objects.get(id=sel)
        cat.save()
        product=Addproduct(product=pr,description=des,price=price,image=img,add=cat)
        product.save()
        return redirect('showprdct')

@login_required(login_url='login1')    
def showprdct(request):
    prod=Category.objects.all()
    pr=Addproduct.objects.all()
    return render(request,'showprdct.html',{'prodct':prod ,'prdct':pr})
def logout1(request):
    auth.logout(request)
    return redirect('index')

@login_required(login_url='login1') 
def delete(request, pk):
    product_exists = Addproduct.objects.filter(pk=pk).exists()
    if product_exists:
        product = Addproduct.objects.get(pk=pk)
        product.delete()
        messages.success(request, 'Product deleted successfully.')
    else:
        messages.error(request, 'Product not found.')
    
    return redirect('showprdct')

@login_required(login_url='login1') 
def user_details(request):
    details=Account.objects.all()
    return render(request,'user_details.html',{'de':details})

@login_required(login_url='login1') 
def delete_user(request, pk):
    user = User.objects.filter(id=pk)
    
    if user is not None:
        user.delete()
        messages.success(request, 'User deleted successfully.')
    else:
        messages.error(request, 'User not found.')
    
    return redirect('user_details') 

@login_required(login_url='login1') 
def cart(request):
    cart_items = Cart.objects.filter(user=request.user).select_related('product')
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'cart.html', {'cartitems':cart_items,'totalprice': total_price})

@login_required(login_url='login1') 
def cart_details(request, pk):
    product = Addproduct.objects.get(id=pk)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required(login_url='login1') 
def removecart(request, pk):
    product = Addproduct.objects.get(id=pk)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()
    
    if cart_item:
        cart_item.delete()
    
    return redirect('cart')

@login_required(login_url='login1') 
def categorized_products(request, category_id):
    categories = Category.objects.filter(id=category_id)
    
    if categories.exists():
        category = categories.first()
        products = Addproduct.objects.filter(add=category)
        return render(request, 'categories.html', {'categories': [category], 'products': products})
    else:
        
        return render(request, 'user_home.html')







