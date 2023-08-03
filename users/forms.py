from django.forms import ModelForm
from .models import *
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        # fields = "__all__"
        exclude = ["photo"]

class ValidateForm(forms.Form):
    name = forms.CharField(min_length=5,error_messages={'required' : "Enter 10 digit phone number"})
    email = forms.EmailField(empty_value="bhattaraibibek91@gmail.com")
    photo = forms.ImageField()
    phone = forms.CharField(min_length=10)
    location = forms.CharField(max_length=20,strip=False)
    age = forms.IntegerField(min_value=18)


    # programmer = forms.BooleanField(label="Yes", label_suffix='')