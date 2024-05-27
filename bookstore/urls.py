from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash),
    path('users/', views.users),
    path('home/', views.home),
    path('course/', views.course),
    path('login/', views.login),
]