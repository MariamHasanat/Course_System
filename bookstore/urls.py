from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('users/', views.users),
    path('course/', views.course),
    path('login/', views.login),
]