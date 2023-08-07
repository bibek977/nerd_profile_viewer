from django.shortcuts import render, redirect

def home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
        
    return render(request, 'blog/index.html')