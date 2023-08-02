from django.shortcuts import render, redirect
from .forms import *
# from users.forms import *
from users.models import *
 
def home(request):
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            print("form validate")
            data = request.POST
            name = data['name']
            email = data['email']
            phone = data['phone']
            photo = form.cleaned_data['photo']
            age = data['age']
            location = data['location']
            profile = Profile(name=name, email=email, photo=photo, location=location,phone=phone, age=age)
            profile.save()
            return redirect('forms')
    else:
        form = ProfileForm()
    return render(request, 'forms/login.html', {'forms' : form})