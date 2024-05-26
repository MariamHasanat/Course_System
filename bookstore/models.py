from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True, null=False, default=None)
    name = models.CharField( max_length=90, null=True)
    email= models.EmailField( max_length=90, null=True)
    password = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.name 


class Course(models.Model):
    code = models.CharField(max_length=10, unique=True, primary_key=True, null=False, default='TEMP_CODE')
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    instructor = models.CharField(max_length=100, null=True)
    schedule = models.ForeignKey('CourseSchedule', on_delete=models.CASCADE, null=True)
    prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False)
    capacity = models.IntegerField(null=True)

    def __str__(self):
        return self.name
    
class CourseSchedule(models.Model):
    id = models.AutoField(primary_key=True, null=False, default=None)
    days = models.CharField(max_length=50, null=True )
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    room_no = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f"{self.days} {self.start_time} - {self.end_time}"
    
class StudentReg(models.Model): 
    id = models.AutoField(primary_key=True, null=False, default=None)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.studentID.name} registered for {self.courseID.name}"