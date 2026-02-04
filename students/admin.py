from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    
    list_filter = ('course_name', 'enrollment_date')
    
    list_display = ('first_name', 'last_name', 'course_name', 'enrollment_date')