from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms  

class SignUpForm(UserCreationForm):
    # password2
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username' : 'User Name :'}