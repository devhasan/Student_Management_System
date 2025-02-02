from django.contrib import admin
from student.models import Student

# Register your models here.
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'address', 'course', 'photo' )

admin.site.register(Student, StudentModelAdmin)