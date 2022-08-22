from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='vendor_home'),
    path('add/',add_car,name='vendor_add_car'),
    path('manage/',manage,name='vendor_manage'),
    path('delete/<int:id>',del_car,name='delete_car'),
    path('edit/<int:id>',edit_car,name='edit_car'),
    path('bookings/',bookings,name='bookings'),
]