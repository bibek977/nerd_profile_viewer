from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                forms = AdminProfileForm(request.POST, instance = request.user)
                users = User.objects.all()
            else:
                forms  = UserProfileForm(request.POST, instance = request.user)
            if forms.is_valid():
                messages.success(request,"Profile updated")
                forms.save()
                # return redirect('home')
        else:
            if request.user.is_superuser == True:
                forms = AdminProfileForm(instance = request.user)
                users = User.objects.all()
            else:
                forms = UserProfileForm(instance = request.user)
                users = None
        return render(request, 'home/index.html', {'forms' : forms, 'users' : users})
    else:
        return redirect("user_login")
    

def user_detail(request, name):
    if request.user.is_authenticated:
        user_get = User.objects.get(username = name)
        forms = AdminProfileForm(instance = user_get)
        if request.method == "POST":
            forms = AdminProfileForm(request.POST, instance=user_get)
            forms.save()
            messages.success(request, 'Profile Changed')
            return render(request, 'home/user_detail.html', {'forms' : forms})
        else:
            return render(request, 'home/user_detail.html', {'forms' : forms})
    else:
        return redirect('user_login')
