from django.shortcuts import render , redirect
from django.http import HttpResponse 
from .models import *  
from .forms import * 
from django.contrib.auth import authenticate , login
from django.contrib import messages 
from django.contrib.auth.models import *
from django.contrib.auth.decorators import login_required 
from .filters import *

@login_required(login_url='login')
def home(request):
    user= Student.objects.get()
    courses = Course.objects.all()
    searchFilter = CoursesFilter(request.GET, queryset=courses)
    courses = searchFilter.qs
    context = {
        'courses' : courses,
        'searchFilter' : searchFilter,
        'user': user
    }
    return render(request, "bookstore/home.html", context)

@login_required(login_url='login')
def dash(request):
    user= Student.objects.get()
    return render(request, "bookstore/dash.html", {'user':user})

@login_required(login_url='login')
def users(request):
    user= Student.objects.get()
    return render(request, "bookstore/users.html", {'user':user})

@login_required(login_url='login')
def course(request):
    user= Student.objects.get()
    course = Course.objects.all()
    return render(request, "bookstore/course.html", {"course":course, 'user': user})



def login(request):
    if request.method =='POST': 
        # print("entered login function ")
        username =request.POST.get('username') 
        password =request.POST.get('password') 
        user= authenticate(request, username=username , password= password) 
        if user is not None: 
            context = {
                'user' : username,
            }
            return redirect('../home/', context = context)  
        else:
            messages.info(request, "Credentails error") 
    context= {} 
    return render(request, "bookstore/login.html", context) 



def register(request):
        form = CreateNewUser()
        if request.method =='POST':
            form = CreateNewUser(request.POST)
            if form.is_valid():                  
                form.save() 
                return redirect('../home/')    
        context= {'form':form} 
        return render(request, 'bookstore/signup.html', context=context) 

