from django.db import models
from django.utils.translation import gettext_lazy as _
import os

def student_directory_name(instance, filename):
    return os.path.join('student/media/', instance.first_name, filename)

class Student(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(unique=True, null=False)
    phone = models.CharField(max_length=11, null=False )
    
    # course = models.TextField()
    class CourseChoices(models.TextChoices):
        EMPTY = "", _("Please select")
        PHYSICS = "Physics", _("Physics")
        CHEMISTRY = "Chemistry", _("Chemistry")
        MATHEMATICS = "Mathematics", _("Mathematics")
        ENGLISH = "English", _("English")
        BANGLS = "Bangla", _("Bangla")
        CSE = "Computer Science", _("CSE")
        
    course = models.CharField(
        max_length=32,
        choices=CourseChoices,
        default=CourseChoices.EMPTY,
    )
    
    address = models.CharField(max_length=256)
    photo = models.ImageField(upload_to=student_directory_name)
    
    def __str__(self):
        return f"{self.first_name}"
    
    