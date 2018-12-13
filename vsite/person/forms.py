from django import forms
from django.db import transaction

from .models import Student
from main.forms import LocationForm 
from django.shortcuts import render

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',  
            'key',
            'bus',
        )

    @staticmethod
    def addStudentForm(request,admin):
        student_form = StudentForm(request.POST)
        location_form = LocationForm(request.POST)
        
        if student_form.is_valid and location_form.is_valid:
            student_form = student_form.save(False)
            student_form.school = admin.getSchool()
            location_form = location_form.save()
            student_form.location = location_form 
            student_form.save()
            return request