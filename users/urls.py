from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='user-index'),
    path('add/', login, name='user-add'),
    path('edit/', edit, name='user-edit'),
    path('update/', update, name='user-update'),
    path('delete/', delete, name='user-delete'),
]
