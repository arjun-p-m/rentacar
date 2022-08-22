from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, VendorForm

# Create your views here.
def login_page(request):
    if request.method == 'GET':
        context = {}
        context['form'] = ''
        return render(request,'guest/login.html',context)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("/admin")
            else:
                if user.user_type == 'user':
                    return redirect("/user")
                elif user.user_type == 'vendor':
                    return redirect("vendor_home")
                elif user.user_type == 'taxi':
                    return redirect("taxi_home")
        else:
            context = {}
            context['error'] = 'Invalid User or Admin not approved'
            return render(request,'guest/login.html',context)

def signup_page(request):
    if request.method == 'GET':
        context = {}
        context['form'] = UserForm()
        return render(request,'guest/signup.html',context)
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            pawd = form.cleaned_data['password']
            obj = form.save(commit= False)
            obj.set_password(pawd)
            obj.user_type = 'user'
            obj.save()
            return redirect('login')
        else:
            context = {}
            context['form'] = form
            return render(request,'guest/signup.html',context)

def taxi(request):
    if request.method == 'GET':
        context = {}
        context['form'] = UserForm()
        return render(request,'guest/taxi.html',context)
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            pawd = form.cleaned_data['password']
            obj = form.save(commit= False)
            obj.set_password(pawd)
            obj.user_type = 'taxi'
            obj.is_active = 0
            obj.save()
            return redirect('login')
        else:
            context = {}
            context['form'] = form
            return render(request,'guest/taxi.html',context)

def vendor(request):
    if request.method == 'GET':
        context = {}
        context['form'] = VendorForm()
        return render(request,'guest/vendor.html',context)
    elif request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            pawd = form.cleaned_data['password']
            obj = form.save(commit= False)
            obj.set_password(pawd)
            obj.user_type = 'vendor'
            obj.is_active = 0
            obj.save()
            return redirect('login')
        else:
            context = {}
            context['form'] = form
            return render(request,'guest/vendor.html',context)

def logout_fun(request):
    logout(request)
    return redirect('login')