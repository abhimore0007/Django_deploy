from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,loginForm,UserEditForm,AdminEditForm,PasswordChangeForm,Customer_Form
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from .models import Watch,Cart,Customer_Detail
# Create your views here.

#===============For Paypal =========================
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse
#========================================================

def base(request):
    return render(request,'core/index.html')  

def register(request):
    if request.method == 'POST':
        reg=RegisterForm(request.POST)
        if reg.is_valid():
            reg.save()
            messages.success(request,'Registration Successfully !!')
            return redirect('register')
    else:
        reg=RegisterForm()
    return render(request,'core/register_form.html',{'reg':reg})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            log = loginForm(request, request.POST)
            if log.is_valid():
                Name = log.cleaned_data['username']
                Password = log.cleaned_data['password']
                user = authenticate(username=Name, password=Password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            log = loginForm()
        return render(request, 'core/login_form.html', {'log': log})
    else:
        return redirect('login')

def log_out(request):
    logout(request)
    return redirect('base')


def User_Profile(request):
    return render(request,'core/profile.html')
    
    

def User_Change_Password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            CP=PasswordChangeForm(user=request.user,data=request.POST)
            if CP.is_valid():
                CP.save()
                update_session_auth_hash(request,CP.user)
                messages.success(request,'Password Change SuccessFully')
                return redirect('changePassword')
        else:
            CP=PasswordChangeForm(user=request.user)
            return render(request,'core/ChangePasswordForm.html',{'CP':CP})
    else:
        return redirect('login')


def User_Password_forgot_Form(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            Forgot_Pass=SetPasswordForm(user=request.user,data=request.POST)
            if Forgot_Pass.is_valid():
                Forgot_Pass.save()
                update_session_auth_hash(request,Forgot_Pass.user)
                messages.success(request,'Password Change SuccessFully')
                return redirect('Profile')
        else:
            Forgot_Pass=SetPasswordForm(user=request.user)
        return render(request,'core/forgot_Password_Form.html',{'Forgot_Pass':Forgot_Pass})
    else:
        return redirect('Login')
    

def User_categories(request):
    watch_cate=Watch.objects.all()
    return render(request,'core/categories.html',{'watch_cate':watch_cate})

def watch_details(request,id):
    watch_details=Watch.objects.get(pk=id)
    return render(request,'core/watch_details.html',{'watch_details':watch_details})

def Add_To_Cart(request,id):
    if request.user.is_authenticated:
        watch_cart=Watch.objects.get(pk=id)
        user=request.user
        Cart(user=user,product=watch_cart).save()
        return redirect('watchdetails', id)
    else:
        return redirect('login')
    

def view_To_Cart(request):
    if request.user.is_authenticated:
        watch_view=Cart.objects.filter(user=request.user)
        total=0
        delivery_charges=3000
        for viewcart in watch_view:
            total+=(viewcart.product.discounted_price*viewcart.quantity)
        final_price =total+delivery_charges
        return render(request,'core/watch_cart.html',{'watch_view':watch_view,'total':total,'final_price':final_price})
    else:
        return redirect('login')
    

def add_to_quantity(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Cart, pk=id)
        if product.quantity < 4:
            product.quantity += 1
            product.save()
        else:
            messages.error(request, "You cannot add more than 4 units of this product.")
        return redirect('viewCart')
    else:
        return redirect('login')

    

def delete_to_quantity(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Cart, pk=id)
        if product.quantity>1:
            product.quantity -= 1
            product.save()
            return redirect('viewCart')
    else:
        return redirect('login')
    

def delete_the_Cart(request,id):
     if request.user.is_authenticated:
         delect_cart= Cart.objects.get(pk=id)
         delect_cart.delete()
         return redirect('viewCart')
     else:
         return redirect('login')
     
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def AddressPage(request):
    if request.user.is_authenticated:
        address = Customer_Detail.objects.filter(user=request.user)
        return render(request,'core/addresspage.html',{'address':address})
    else:
        return redirect('login')

def Address_Add(request):
    if request.method == 'POST':
        add=Customer_Form(request.POST)
        if add.is_valid():
            user=request.user                # user variable store the current user i.e steveroger
            name= add.cleaned_data['name']
            address= add.cleaned_data['address']
            city= add.cleaned_data['city']
            state= add.cleaned_data['state']
            pincode= add.cleaned_data['pincode'] 
            Customer_Detail(user=user,name=name,address=address,city=city,state=state,pincode=pincode).save()
            return redirect('AddressPage')
    else:
        add =Customer_Form()
        address = Customer_Detail.objects.filter(user=request.user)
    return render(request,'core/Address_Add.html',{'add':add})

def Profile_edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                UC=AdminEditForm(request.POST,instance=request.user)
            else:
                UC = UserEditForm(request.POST,instance=request.user)
            if UC.is_valid():
                    UC.save()
                    messages.success(request,'Data edit Successfully')
        else:
            if request.user.is_superuser == True:
                UC=AdminEditForm(request.POST,instance=request.user)
                user=User.objects.all()
            else:
                UC=UserEditForm(instance=request.user)
        return render(request,'core/profile_Edit.html',{'UC':UC})
    else:
        return redirect('login')
   
         
def delete_Add(request,id):
    if request.method == 'POST':
        de = Customer_Detail.objects.get(pk=id)
        de.delete()
    return redirect('AddressPage')


def Check_Out(request):
    if request.user.is_authenticated:
        watch_view=Cart.objects.filter(user=request.user)
        total=0
        delivery_charges=3000
        for viewcart in watch_view:
            total+=(viewcart.product.discounted_price*viewcart.quantity)
        final_price =total+delivery_charges
        address = Customer_Detail.objects.filter(user=request.user)
        return render(request,'core/checkout.html',{'total':total,'final_price':final_price,'address':address})
    else:
        return redirect('login')
    

def Payment(request):

    watch_view=Cart.objects.filter(user=request.user)
    total=0
    delivery_charges=3000
    for viewcart in watch_view:
        total+=(viewcart.product.discounted_price*viewcart.quantity)
    final_price =total+delivery_charges

     #================= Paypal Code =====================
   
    host = request.get_host()   # Will fecth the domain site is currently hosted on.
   
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,   #This is typically the email address associated with the PayPal account that will receive the payment.
        'amount': final_price,    #: The amount of money to be charged for the transaction. 
        'item_name': 'Watch',       # Describes the item being purchased.
        'invoice': uuid.uuid4(),  #A unique identifier for the invoice. It uses uuid.uuid4() to generate a random UUID.
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",         #The URL where PayPal will send Instant Payment Notifications (IPN) to notify the merchant about payment-related events
        'return_url': f"http://{host}{reverse('paymentsuccess')}",     #The URL where the customer will be redirected after a successful payment. 
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",      #The URL where the customer will be redirected if they choose to cancel the payment. 
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

  #================= Paypal Code  End =====================
    return render(request,'core/payment_page.html',{'paypal':paypal_payment})

def payment_success(request):
    return render(request,'core/payment_success.html')


def payment_failed(request):
    return render(request,'core/payment_failed.html')


    

