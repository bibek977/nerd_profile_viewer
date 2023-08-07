from django.contrib import admin
from .models import *

@admin.register(Intern)
class Intern_Model(admin.ModelAdmin):
    list_display = ['name' , 'program']