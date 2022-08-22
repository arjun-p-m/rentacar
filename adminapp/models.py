from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import IntegerField

# Create your models here.
class User(AbstractUser):
    address = models.TextField(
        max_length=100,
        null=True,
        verbose_name='Address'
    )
    phone = models.BigIntegerField(
        null=True,
        verbose_name='Phone Number'
    )
    company_name = models.CharField(
        max_length=30,
        null=True,
        default='None',
        verbose_name='Company Name'
    )
    user_type = models.CharField(
        max_length=30,
        default='admin'
    )

class Category(models.Model):
    category_name = models.CharField(
        max_length=50,
        verbose_name='Category'
    )
    def __str__(self):
        return self.category_name

class Offer(models.Model):
    discount = models.FloatField(
        verbose_name='Discount Offer'
    )
    status = models.BooleanField(
        default=False
    )
    def __str__(self):
        return str(self.discount)+'% Discount'

class Car(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Car Name'
    )
    description = models.TextField(
        max_length=300,
        verbose_name='Description',
        null=True
    )
    image = models.FileField(
        upload_to='Cars',
        max_length=300
    )
    passanger = models.IntegerField(
        verbose_name='Adult Passanger'
    )
    large_luggage = models.IntegerField(
        verbose_name='Large Luggage'
    )
    small_luggage = models.IntegerField(
        verbose_name='Small Luggage'
    )
    doors = models.IntegerField(
        verbose_name='No of Doors'
    )
    air_condition = models.BooleanField(
        default=False,
        verbose_name='A/C Status'
    )
    rent_amount = models.FloatField(
        verbose_name='Rent Amount'
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE
    )
    status = models.BooleanField(
        default=True
    )
    vendor = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    offer = models.ForeignKey(
        null=True,
        to=Offer,
        on_delete=models.CASCADE
    )
    mode = models.CharField(
        max_length=20,
        default='rent'
    )
    kilometer = models.CharField(
        default='',
        max_length=50,
        verbose_name='Kilometer Details'
    )

    def offer_price(self):
        if self.offer != None:
            return self.rent_amount-(self.rent_amount*self.offer.discount)/100
        else:
            return 0

    def __str__(self):
        return self.name

class Order(models.Model):
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Booking Date'
    )
    pick_up_location = models.CharField(
        max_length=50,
        verbose_name='Pick Up Location'
    )
    pick_date = models.DateField(
        verbose_name='Pick Up Date'
    )
    pick_time = models.TimeField(
        verbose_name='Pick Up Time'
    )
    return_date = models.DateField(
        verbose_name='Return Date'
    )
    return_time = models.TimeField(
        verbose_name='Return Time'
    )
    no_of_days = models.IntegerField(
        default=0
    )
    total = models.FloatField(
        default=0
    )
    status = models.IntegerField(
        default=0
    )
    car = models.ForeignKey(
        to=Car,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )

class UserComplaints(models.Model):
    CTYPE = (
        ('Related to Transaction/Payment','Related to Transaction/Payment'),
        ('Dissatisfaction with recommended action','Dissatisfaction with recommended action'),
        ('Service not delivered to expected standard','Service not delivered to expected standard'),
        ('Delivery delayed or not completed','Delivery delayed or not completed'),
        ('Hardware failed','Hardware failed'),
        ('Poor service','Poor service'),
        ('Other','Other')
    )
    c_type = models.CharField(
        max_length=50,
        choices=CTYPE,
        verbose_name='Complaint type'
    )
    description = models.TextField(
        max_length=100,
        verbose_name='Description',
        null=True
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.IntegerField(default=0)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )


class BookTaxi(models.Model):
    start_from = models.CharField(
        max_length=30,
        verbose_name='From'
    )
    to_location = models.CharField(
        max_length=30,
        verbose_name='To'
    )
    date = models.DateTimeField(
        verbose_name='Date & Time'
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    taxi = models.ForeignKey(
        to=Car,
        on_delete=models.CASCADE
    )
    status = models.IntegerField(
        default=0
    )

