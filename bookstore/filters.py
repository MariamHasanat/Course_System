import django_filters
from .models import *

class CoursesFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = ['code', 'name', 'instructor']