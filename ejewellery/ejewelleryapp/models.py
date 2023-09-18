from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class c_registermodel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phonenumber=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    birthday=models.DateField()
    pincode=models.CharField(max_length=7)
    password=models.CharField(max_length=20)

class adminregistermodel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class add_designmodel(models.Model):
    item=models.CharField(max_length=50)
    product=models.CharField(max_length=50)
    weight=models.IntegerField()
    size=models.IntegerField()
    Prize=models.IntegerField()
    image=models.ImageField(upload_to='ejewellery/static')