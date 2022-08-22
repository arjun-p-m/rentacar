from datetime import datetime
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from adminapp.models import Car, Category, User, Order, Offer, BookTaxi
from .forms import ProfileForm, OrderForm, ComplaintsForm, TaxiBookForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
def home(request):
    if request.method == 'GET':
        context = {}
        obj = Car.objects.filter(status=True,mode='rent')
        context['cat'] = Category.objects.all()
        context['data'] = obj
        return render(request,'user/home.html',context)

def taxt_list(request):
    if request.method == 'GET':
        context = {}
        obj = Car.objects.filter(status=True,mode='taxi')
        context['data'] = obj
        return render(request,'user/taxi.html',context)

def category_filter(request,cat):
    context = {}
    obj = Car.objects.filter(status=True,category__category_name=cat)
    context['data'] = obj
    context['cat'] = Category.objects.all()
    return render(request,'user/home.html',context)

def profile(request):
    if request.method == 'GET':
        context = {}
        context['form'] = ProfileForm(instance=request.user)
        return render(request,'user/profile.html',context)
    elif request.method == 'POST':
        form = ProfileForm(data=request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            context = {}
            context['form'] = form
            return render(request,'user/profile.html',context)

def chnage_password(request):
    if request.method == 'GET':
        context = {}
        context['form'] = PasswordChangeForm(request.user)
        return render(request,'user/password.html',context)
    elif request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            context = {}
            context['form'] = form
            messages.warning(request, 'Not Updated!')
            return render(request,'user/password.html',context)

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def taxi_booking(request,id):
    car = Car.objects.get(pk=id)
    if request.method == 'GET':
        context = {}
        context['form'] = TaxiBookForm()
        context['data'] = car
        return render(request,'user/booktaxi.html',context)
    elif request.method == 'POST':
        form = TaxiBookForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            print(date)
            obj = BookTaxi.objects.filter(taxi=id)
            print(obj)
            if obj.count() != 0:
                for i in obj:
                    if datetime.date(i.date) == datetime.date(date):
                        return HttpResponse('<script>window.alert("Oops Not available on that date..!");window.location.href="/user/taxi/"</script>')
            obj = form.save(commit=False)
            obj.user = request.user
            obj.taxi = car
            obj.save()
            return redirect('home')
        else:
            context = {}
            context['form'] = form
            context['data'] = car
            return render(request,'user/booktaxi.html',context)
            

def user_booking(request,id):
    if request.method == 'GET':
        context = {}
        context['form'] = OrderForm()
        context['data'] = Car.objects.get(pk=id)
        return render(request,'user/booking.html',context)
    elif request.method == 'POST':
        location = request.POST['pick_up_location']
        pdate = request.POST['pick_date']
        ptime = request.POST['pick_time']
        rdate = request.POST['return_date']
        rtime = request.POST['return_time']
        no = request.POST['no_day']
        total = request.POST['total2']
        car = Car.objects.get(pk=id)
        obj = Order(pick_up_location=location,pick_date=pdate,pick_time=ptime,return_date=rdate,return_time=rtime,no_of_days=no,total=total,car=car,user=request.user)
        obj.save()
        return redirect('home')

def history(request):
    context = {}
    obj = Order.objects.filter(user=request.user)
    context['data'] = obj
    context['data2'] = BookTaxi.objects.filter(user=request.user)
    return render(request,'user/history.html',context)

def view_car(request,id):
    context = {}
    obj = Car.objects.get(pk=id)
    context['data'] = obj
    return render(request,'user/car.html',context)

def complaints(request):
    if request.method == 'GET':
        context = {}
        context['form'] = ComplaintsForm()
        return render(request,'user/complaints.html',context)
    elif request.method == 'POST':
        form = ComplaintsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            messages.success(request, 'Complaint successfully posted!')
            return redirect('user_complaints')
        else:
            context = {}
            context['form'] = form
            messages.warning(request, 'Not Posted!')
            return render(request,'user/complaints.html',context)

def check(request):
    if request.method == 'GET':
        start = request.GET['start']
        end = request.GET['end']
        id = request.GET['id']
        obj1 = Order.objects.filter(car=id,pick_date__range=[start,end])
        obj2 = Order.objects.filter(car=id,return_date__range=[start,end])
        if obj1.count()==0 and obj2.count() == 0:
            s = 1
        else:
            s = 0
        return JsonResponse({'success':s})
