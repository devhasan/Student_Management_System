from django import forms
from . import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        # fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'course', 'photo' ]
        fields = '__all__'
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        
        help_texts = {
            'first_name': 'Enter your First Name',
            'last_name': 'Enter your Last Name',
            'email': 'Enter your valid Email Address',
        }
        
        