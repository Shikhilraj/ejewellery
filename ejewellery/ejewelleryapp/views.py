from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib import messages
from ejewellery.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
import uuid

# Create your views here.
def index(request):
    return render(request,'index.html')

def c_register(request):
    if request.method == 'POST':
        a=c_registerform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phonenumber']
            ads=a.cleaned_data['address']
            pin=a.cleaned_data['pincode']
            dob=a.cleaned_data['birthday']
            pas=a.cleaned_data['password']
            cpas=a.cleaned_data['password1']
            if pas==cpas:
                b=c_registermodel(name=nm,email=em,phonenumber=ph,address=ads,pincode=pin,birthday=dob,password=pas)
                b.save()
                return HttpResponse("Registered successfully")
        else:
            return HttpResponse("Enter Valid data")
    return render(request,'customer_register.html')

def c_login(request):
    if request.method == 'POST':
        a=c_loginform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            pas=a.cleaned_data['password']
            b=c_registermodel.objects.all()
            for i in b:
                if em==i.email and pas==i.password:
                    name=i.name
                    email=i.email
                    phonenumber=i.phonenumber
                    address=i.address
                    pincode=i.pincode
                    birthday=i.birthday
                    id=i.id
                    #return HttpResponse("Success")
                    return render(request,'c_profile.html',{'name':name,'email':email,'phonenumber':phonenumber,'address':address,'pincode':pincode,'birthday':birthday,'id':id})
            else:
                return HttpResponse("Username and password mismatch")
        else:
            return HttpResponse("Login Failed")
    return render(request,'c_login.html')

def c_profile(request):
    a=c_registermodel.objects.all()
    return render(request,'c_profile.html')

def c_profile_edit(request,id):
    user = c_registermodel.objects.get(id=id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phonenumber = request.POST('phonenumber')
        user.address = request.POST('address')
        user.pincode = request.POST('pincode')
        user.birthday = request.POST('birthday')
        user.save()
        return redirect(c_login)
    return render(request,'c_profile_edit.html',{'user':user})

def adminregister(request):
    if request.method == 'POST':
            uname =request.POST.get('username')
            em = request.POST.get('email')
            pas= request.POST.get('password')
            pas1=request.POST.get('password1')
            if pas == pas1:
                if User.objects.filter(username=uname).first():
                    messages.success(request,'username already taken')
                    return HttpResponse('username already exist')
                if User.objects.filter(email=em).first():
                    messages.success(request, "email already taken")
                    return HttpResponse("Email already exist")
                user_obj=User(username=uname,email=em)
                user_obj.set_password(pas)
                user_obj.save()
                auth_token=str(uuid.uuid4())
                profile_obj=adminregistermodel.objects.create(user=user_obj,auth_token=auth_token)
                profile_obj.save()
                send_mail_regis(em, auth_token)
                return HttpResponse("Verified successfully")
            return HttpResponse("password mismatch")
    return render(request,'admin_register.html')

def send_mail_regis(email,token):
    subject="your account has been verified"
    message=f'pass the link to verify your account http:/127.0.0.1:8000/verify/{token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def admin_login(request):
    global User;
    if request.method=='POST':
        a=admin_loginform(request.POST)
        username = request.POST.get('username')
        pas = request.POST.get('password')
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'User not found')
            return redirect(admin_login)
        profile_obj=adminregistermodel.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,'profile not verified check your email')
            return redirect(admin_login)
        User=authenticate(username=username,password=pas)

        if User is None:
            messages.success(request,'Wrong password or None')
            return redirect(admin_login)
        # return HttpResponse("Login successfully")
        a=adminregistermodel.objects.filter(user=User)
        return render(request,'admin_profile.html',{'a':a})
    return render(request,'admin_login.html')

def verify(request,auth_token):
    profile_obj=adminregistermodel.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account already verified')
            return redirect(admin_login)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account verified')
        return redirect(admin_login)
    else:
        return HttpResponse("Error")

def admin_profile(request):
    a=adminregistermodel.objects.all()
    return render(request,'admin_profile.html')

def add_design(request):
    if request.method == 'POST':
        a = add_designform(request.POST)
        if a.is_valid():
0
