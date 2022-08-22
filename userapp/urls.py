from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('filter/<str:cat>',category_filter,name='filter'),
    path('profile/',profile,name='profile'),
    path('change/',chnage_password,name='change_password'),
    path('booking/<int:id>',user_booking,name='user_booking'),
    path('history/',history,name='history'),
    path('car/<int:id>',view_car,name='view_car'),
    path('complaints/',complaints,name='user_complaints'),
    path('taxi/',taxt_list,name='user_taxi'),
    path('taxi/booking/<int:id>',taxi_booking,name='taxi_booking'),
    path('check/',check,name='check')
]