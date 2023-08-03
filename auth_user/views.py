from django.shortcuts import render,redirect
from .forms import *

def home(request):
    if request.method == "POST":
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("user_login")
    else:
        forms = SignUpForm()
    return render(request, 'auth_user/login.html', {'forms': forms})

    