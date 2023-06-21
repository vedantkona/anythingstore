from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.home, name ="home"),
    path('register/', views.register, name = "register"),
    path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name = "logout"),
    path('textnote/', views.textnote, name = "textnote"),
    path('audionote/', views.audionote, name = "audionote"),
    path('videonote/', views.videotnote, name = "videonote"),
    path('profile/', views.user_Profile, name = "profile"),
]