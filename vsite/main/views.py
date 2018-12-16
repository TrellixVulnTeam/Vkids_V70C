from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from person.models import *
from .models import *

from person.forms import StudentForm
from main.forms import LocationForm,BusForm

from firebase import firebase
from collections import Counter

firebase = firebase.FirebaseApplication('https://vkids-60406.firebaseio.com/', None)
def fireBaseMainUpdate():
    card_key = firebase.get('/Vkids_Data/Card ID', None)
    time = firebase.get('/Vkids_Data/Time', None)

    try:     
        student = Student.objects.get(card_key = card_key)
        student.updateStatus(firebase,time)
    except Student.DoesNotExist:
        pass


#################################################################################################################################################   

#Create your views here.

@login_required(login_url = "/user/login")
def adminDash(request):
    fireBaseMainUpdate()

    admin = Admin.objects.get(user = request.user)
    student_list = admin.getStudentInSchool()
    bus_list = Bus.objects.filter(school = admin.school)

    form = {
        'all_student' : admin.getInBusCount() + admin.getOutBusCount(),
        'in_bus_student' : admin.getOutBusCount(),
        'all_bus' : admin.getBusActive() + admin.getBusStation(),
        'active_bus': admin.getBusActive(), 
        'student_information' : [],
        'bus_information' : [],
    }
    for student in student_list:
        student_dic = {
            'name' : student.getFirstName(),
            'status' : student.getStatus(),
            'status_label' : student.getStatusLabel(),
        }
        form['student_information'].append(student_dic)
    for bus in bus_list:
        bus_dic = {
            'bus_number' : bus.getBusNumber(),
            'status' : bus.getStatus(),
            'status_label' : bus.getStatusLabel(),
        }
        form['bus_information'].append(bus_dic)
    
    return render(request,'admin/main-admin.html',form)

@login_required(login_url = "/user/login")
def adminKids(request):    
    fireBaseMainUpdate()

    admin = Admin.objects.get(user = request.user)
    
    if request.method == 'POST':
        request = StudentForm.addStudentForm(request,admin)
        form = viewStudent(admin)
        return render(request,'admin/kids_data.html',form)

    else:
        form = viewStudent(admin)
        return render(request,'admin/kids_data.html',form)

@login_required(login_url = "/user/login")
def adminBus(request):
    fireBaseMainUpdate()

    admin = Admin.objects.get(user = request.user)
    print(admin.school)
    form = {}
    if request.method == 'POST':
        request = BusForm.addBusForm(request,admin)
        form = viewBus(admin)
        return render(request,'admin/Car_Data.html',form)

    else:
        form = viewBus(admin)
        return render(request,'admin/Car_Data.html',form)

    
        

@login_required(login_url = "/user/login")
def adminStat(request):
    fireBaseMainUpdate()

    return render(request, 'admin/Stat_Data.html')


# @login_required(login_url = "/user/login")
# def test(request):
#     return render(request,'test.html')

#parent site

@login_required(login_url = "/user/login")
def parentDash(request):
    fireBaseMainUpdate()

    parent = Parent.objects.get(user = request.user)
    student_list = Student.objects.filter(parent = parent)

    if request.method == 'POST':
        form = studentListFunc(student_list)
        form = studentInformation(form)
        if len(request.POST.dict()) == 1:
            return render(request,'parent/main-parent.html',form)
        check_number = next(iter(request.POST.dict()))[-1]
        form = studentInformation(form,check_number)

        return render(request,'parent/main-parent.html',form)
    else:    
        form = studentListFunc(student_list)
        form = studentInformation(form)
        return render(request,'parent/main-parent.html',form)

@login_required(login_url = "/user/login")
def parentProfile(request):
    parent = Parent.objects.get(user = request.user)
    student_list = Student.objects.filter(parent = parent)
    children_list = []

    for student in student_list:
        children_list.append(student.getName())
        
    form = {
        'student_list' : children_list,
        'name' : parent.getName(),
        'students' : [],
        'username' : request.user.username,
        'email' : request.user.email,
        'phonenumber' : parent.getPhone(),    
    }
    return render(request,'parent/profile_parent.html',form)

def studentListFunc(student_list):
    i = 1
    form = {"student_id_list" : [] ,'students' : [] }
    for student in student_list:
        form["student_id_list"].append(student.getId())
        bus_dic = {    
            'number' : i,
            'id' : student.getId(),
            'name' : student.getName(),
            'status' : student.getStatus(),

            'status_label' : student.getStatusLabel(),
        }  
        form['students'].append(bus_dic)
        i += 1
    return form



def studentInformation(form,check_number = 1):
    student_id = form["student_id_list"][int(check_number)-1]
    student = Student.objects.get(pk = student_id)
        
    student_information = {
        'status' : student.getStatus(),
        'bag_weight' : student.getBagWeight(),
        'bus': student.getBus(),
        'speed': student.getCurrentSpeed(),

        'status_label' : student.getStatusLabel(),
        }
        
    form['student_information'] = student_information
    return form

def viewStudent(admin):        
    student_form = StudentForm()
    location_form = LocationForm()

    student_list = admin.getStudentInSchool()
    
    form = { 'students' : [] }
    
    for student in student_list:
        student_dic = {
            'bus' : student.getBus(),
            'name' : student.getName(),
            'status' : student.getStatus(),
            'bag_weight' : student.getBagWeight(),
            'phone' : '089-0527782',

            'status_label' : student.getStatusLabel(),
        }
        form['students'].append(student_dic)
        
    form['student_form'] = student_form
    form['location_form'] = location_form
    return form

def viewBus(admin):
    bus_form = BusForm()

    bus_list = Bus.objects.filter(school = admin.school)
    
    form = { 'buses' : [] }

    for bus in bus_list:
        bus_dic = {
                'bus' : bus.getBusNumber(),
                'status' : bus.getStatus(),
                'driver' : bus.getDriverName(),
                'speed': bus.getCurrentSpeed(),
                'massage': 'test',
                'position': 'test',

                'status_label' : bus.getStatusLabel(),
        }  
        form['buses'].append(bus_dic)
    
    form['bus_form'] = bus_form
    return form

