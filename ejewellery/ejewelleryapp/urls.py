from django.urls import path
from .views import *


urlpatterns=[
    path('',index),
    path('customer_register/',c_register),
    path('customer_login/',c_login),
    path('admin_register/',adminregister),
    path('admin_login/',admin_login),
    path('c_profile',c_profile),
    path('c_profile_edit/<int:id>/',c_profile_edit),
    path('send/',send_mail_regis),
    path('verify/<auth_token>',verify)
]