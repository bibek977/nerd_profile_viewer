from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *

def home(request):
    if request.user.is_authenticated:
        forms = UserProfileForm(instance = request.user)
        return render(request, 'home/index.html', {'forms' : forms})
    else:
        return redirect("user_login")
    