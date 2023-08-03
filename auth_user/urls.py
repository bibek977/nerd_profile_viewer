from django.urls import path
from .views import *


urlpatterns = [
    path('', user_login, name = 'user_login'),
    path('sign_up/', user_sign_up, name='user_sign_up'),
    path('user_logout/', user_logout, name="user_logout"),
    path('user_change_pass',user_change_pass,name="user_change_pass"),
    path('user_set_pass/',user_set_pass,name="user_set_pass"),

]
