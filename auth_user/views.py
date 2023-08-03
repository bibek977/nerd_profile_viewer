from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout

def user_sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            forms = SignUpForm(request.POST)
            if forms.is_valid():
                username = request.POST.get('username')
                messages.success(request, f"{username} User Created")
                forms.save()
                return redirect("user_login")
        else:
            forms = SignUpForm()
        return render(request, 'auth_user/sign_up.html', {'forms': forms})
    else:
        return redirect('home')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            forms = AuthenticationForm(request=request, data = request.POST)
            if forms.is_valid():
                user_name = forms.cleaned_data['username']
                user_password = forms.cleaned_data['password']
                print(user_name,user_password)
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Welcome, {user_name}")
                    # return redirect('/')
                    return render(request, 'home/index.html', {"name" : request.user})
        else:
            forms = AuthenticationForm()
        return render(request, 'auth_user/login.html', {'forms': forms})
    else:
        return redirect('home')

def user_logout(request):
    logout(request)
    return redirect('user_login')

def user_change_pass(request):
    forms = PasswordChangeForm(request.user)
    return render(request, 'auth_user/change_pass.html', {'forms' : forms})