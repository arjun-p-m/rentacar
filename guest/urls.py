from django.urls import path
from .views import *

urlpatterns = [
    path('',login_page,name='login'),
    path('signup/',signup_page,name='signup'),
    path('logout/',logout_fun,name='logout'),
    path('reg/vendor/',vendor,name='vendor_signup'),
    path('reg/taxi/',taxi,name='taxi_signup'),
]