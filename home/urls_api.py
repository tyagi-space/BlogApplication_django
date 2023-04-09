
from django.urls import path
from .views_api import *
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('login/',LoginView),
    path('register/',RegisterView),
]