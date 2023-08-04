from django.contrib import admin
from .models import *

admin.site.register(Profile)

@admin.register(Geeks_Model)
class Geeks_Model_Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'date_created']