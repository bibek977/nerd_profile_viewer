from django.urls import path
from .views import *

urlpatterns = [
    path("", api_home, name='api_home'),
    # path("<str:name>/", data_by_name),
    path('<int:pk>/', data_by_id)
]
