from django.shortcuts import render, redirect
from .models import *

def index(request):
    
    user = Profile.objects.all()
    context = {
        'user' : user
    }
    return render(request, 'users/index.html', context=context)

def login(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        email = data['email']
        photo = request.FILES['photo']
        phone = data['phone']
        age = data['age']
        location = data['location']

        profile = Profile(name=name, photo=photo , email=email,  location=location,phone=phone, age=age)
        profile.save()

        return redirect('user-index')

    return render(request, 'users/add.html')

def edit(request):
    if request.method == "POST":
        data = request.POST
        id = data['id']
        print(id)
        user = Profile.objects.get(id=id)
        print("got is")
        context = {
            'user' : user
        }
        return render(request, 'users/update.html', context=context)
    return redirect('user-index')

def update(request):
    if request.method=="POST":
        data = request.POST
        id = data['id']
        name = data['name']
        email = data['email']
        # photo = request.FILES['photo']
        phone = data['phone']
        age = data['age']
        location = data['location']

        user = Profile.objects.filter(id = id).update(name=name, email=email,  location=location,phone=phone, age=age)
        # user.save()

        return redirect('user-index')
    return render(request, 'users/update.html')

def delete(request):
    if request.method=="POST":
        data = request.POST
        id = data['id']
        user = Profile.objects.filter(id = id).delete()

        return redirect('user-index')   
    return render(request, 'users/index.html')
