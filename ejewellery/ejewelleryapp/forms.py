from django import forms
from .models import *
from django import *
from .views import *
from .models import *

class c_registerform(forms.Form):
    email=forms.EmailField()
    name=forms.CharField(max_length= 50)
    address=forms.CharField(max_length=100)
    pincode=forms.CharField(max_length=7)
    phonenumber=forms.CharField(max_length=10)
    birthday=forms.DateField()
    password=forms.CharField(max_length= 20)
    password1 =forms.CharField(max_length=20)

class c_loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

# class admin_registerform(forms.Form):
#     username = forms.CharField(max_length=50)
#     email = forms.EmailField()
#     password=forms.CharField(max_length=20)
#     password1=forms.CharField(max_length=20)

class admin_loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class add_designform(forms.Form):
    item=forms.CharField(max_length=50)
    product=forms.CharField(max_length=50)
    weight=forms.IntegerField()
    Size=forms.IntegerField()
    Prize=forms.IntegerField()

