from django.shortcuts import redirect, render
from adminapp.models import Car, Order
from .forms import CarForm, OfferForm


# Create your views here.
def home(request):
    context = {}
    context['data1'] = Car.objects.filter(vendor=request.user.id).count()
    context['data2'] = Order.objects.filter(car__vendor=request.user.id).count()
    return render(request, 'vendor/home.html',context)

def add_car(request):
    if request.method == 'GET':
        context = {}
        context['form'] = CarForm()
        return render(request, 'vendor/addcar.html',context)
    elif request.method == 'POST':
        form =  CarForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.vendor = request.user
            obj.save()
            return redirect('vendor_add_car')
        else:
            context = {}
            context['form'] = form
            return render(request, 'vendor/addcar.html',context)

def manage(request):
    context = {}
    context['data'] = Car.objects.filter(vendor=request.user.id)
    return render(request, 'vendor/manage.html',context)

def del_car(request,id):
    obj = Car.objects.get(pk=id)
    obj.delete()
    return redirect('vendor_manage')

def edit_car(request,id):
    car = Car.objects.get(pk=id)
    if request.method == 'GET':
        context = {}
        context['form'] = CarForm(instance=car)
        return render(request, 'vendor/edit.html',context)
    elif request.method == 'POST':
        form =  CarForm(request.POST,request.FILES,instance=car)
        if form.is_valid():
            form.save()
            return redirect('vendor_manage')
        else:
            context = {}
            context['form'] = form
            return render(request, 'vendor/edit.html',context)

def bookings(request):
    context = {}
    context['data'] = Order.objects.filter(car__vendor=request.user.id)
    return render(request, 'vendor/booking.html',context)