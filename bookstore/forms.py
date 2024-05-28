from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'prerequisites']
        widgets = {
            'prerequisites': forms.CheckboxSelectMultiple,
        }

class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class LogInUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

