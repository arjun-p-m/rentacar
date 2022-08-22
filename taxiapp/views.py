from django.shortcuts import redirect, render
from adminapp.models import Car, BookTaxi
from .forms import CarForm

# Create your views here.
def home(request):
    context = {}
    context['data1'] = Car.objects.filter(vendor=request.user.id).count()
    context['data2'] = BookTaxi.objects.filter(taxi__vendor=request.user.id).count()
    return render(request, 'taxi/home.html',context)

def add_taxi(request):
    if request.method == 'GET':
        context = {}
        context['form'] = CarForm()
        return render(request, 'taxi/addcar.html',context)
    elif request.method == 'POST':
        form =  CarForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.vendor = request.user
            obj.mode = 'taxi'
            obj.save()
            return redirect('taxi_create')
        else:
            context = {}
            context['form'] = form
            return render(request, 'taxi/addcar.html',context)

def manage(request):
    context = {}
    context['data1'] = Car.objects.filter(vendor=request.user.id).count()
    context['data'] = Car.objects.filter(vendor=request.user.id)
    return render(request, 'taxi/manage.html',context)

def del_car(request,id):
    obj = Car.objects.get(pk=id)
    obj.delete()
    return redirect('taxi_manage')

def edit_car(request,id):
    car = Car.objects.get(pk=id)
    if request.method == 'GET':
        context = {}
        context['form'] = CarForm(instance=car)
        return render(request, 'taxi/edit.html',context)
    elif request.method == 'POST':
        form =  CarForm(request.POST,request.FILES,instance=car)
        if form.is_valid():
            form.save()
            return redirect('taxi_manage')
        else:
            context = {}
            context['form'] = form
            return render(request, 'taxi/edit.html',context)

def bookings(request):
    context = {}
    context['data1'] = Car.objects.filter(vendor=request.user.id).count()
    context['data'] = BookTaxi.objects.filter(taxi__vendor=request.user.id)
    return render(request, 'taxi/booking.html',context)

def confirm(request,id):
    obj = BookTaxi.objects.get(pk=id)
    obj.status = 1
    obj.save()
    return redirect('book_taxi')

def deconfirm(request,id):
    obj = BookTaxi.objects.get(pk=id)
    obj.status = 2
    obj.save()
    return redirect('book_taxi')