from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_view, name="login_view"),
    path('logout-view/', logout_view, name="logout_view"),
    path('register/', register_view, name="register_view"),
    path('add_blog/', add_blog, name='add_blog'),
    path('blog_detail/<slug>', blog_detail, name='blog_detail'),
    path('see_blog/', see_blog, name='see_blog'),
    path('update_blog/<slug>', update_blog, name='update_blog'),
    path('delete_blog/<id>', delete_blog, name='delete_blog'),
]