from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='api'),
    path('<int:pk>', get_intern, name="get_intern")
]
