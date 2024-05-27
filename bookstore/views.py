from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import *  
from .forms import * 
from django.contrib.auth import authenticate , login
from django.contrib import messages 
from django.contrib.auth.models import Group

def home(request):
   return render(request, "bookstore/home.html")

def dash(request):
   return render(request, "bookstore/dash.html")

def users(request):
    return render(request, "bookstore/users.html")

def course(request):
    course = Course.objects.all()
    return render(request, "bookstore/course.html", {"course":course})

def login(request):
        if request.method =='POST': 
            print("entered login function ")
            username =request.POST.get('username') 
            password =request.POST.get('password') 
            user= authenticate(request, username=username , password= password) 
            if user is not None: 
                login(request, user) 
                return redirect('home') 
            else:
                messages.info(request, "Credentails error") 
        context= {} 
        return render(request, "bookstore/login.html", context) 

def register(request):
        form=  CreateNewUser() 
        if request.method =='POST':
            form= CreateNewUser(request.POST)
            if form.is_valid():                  
                user=form.save() 
                username= form.cleaned_data.get('username')
                group= Group.objects.get(name="customer") 
                user.groups.add(group) 
                messages.success(request, username +"created succeffuly") 
                return redirect('home')    
        context= {'form':form} 
        return render(request, 'bookstore/login.html', context) 

