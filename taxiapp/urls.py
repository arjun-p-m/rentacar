from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='taxi_home'),
    path('taxi/',add_taxi,name='taxi_create'),
    path('taxi/manage/',manage,name='taxi_manage'),
    path('taxi/delete/<int:id>',del_car,name='delete_taxi'),
    path('taxi/edit/<int:id>',edit_car,name='edit_taxi'),
    path('taxi/bookings/',bookings,name='book_taxi'),
    path('confirm/<int:id>',confirm,name='confirm'),
    path('deconfirm/<int:id>',deconfirm,name='deconfirm'),
]