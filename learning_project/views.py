from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html')
    else:
        return redirect("user_login")