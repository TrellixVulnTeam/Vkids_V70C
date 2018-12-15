from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from person.models import *
from .models import *

from person.forms import StudentForm
from main.forms import LocationForm 

# from firebase import firebase

# firebase = firebase.FirebaseApplication('https://vkids-60406.firebaseio.com/', None)
# result = firebase.get('/message', None)
# print(result)

# Create your views here.

@login_required(login_url = "/user/login")
def adminDash(request):
    admin = Admin.objects.get(user = request.user)

    form = {
        'all_student' : admin.getInBusCount() + admin.getOutBusCount(),
        'in_bus_student' : admin.getOutBusCount(),
        'not_in_bus_student' : admin.getInBusCount(),
        'all_bus' : admin.getBusActive() + admin.getBusStation(),
        'active_bus': admin.getBusActive(), 
        'not_active_bus' : admin.getBusStation(),
    }
    return render(request,'admin/main-admin.html',form)

@login_required(login_url = "/user/login")
def adminKids(request):
    
    admin = Admin.objects.get(user = request.user)
    
    if request.method == 'POST':
        request = StudentForm.addStudentForm(request,admin)
        return render(request,'test.html')

    else:
        
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

        return render(request,'admin/kids_data.html',form)

@login_required(login_url = "/user/login")
def adminBus(request):
    admin = Admin.objects.get(user = request.user)
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
        
    return render(request,'admin/Car_Data.html',form)

@login_required(login_url = "/user/login")
def adminStat(request):
    return render(request, 'admin/Stat_Data.html')


@login_required(login_url = "/user/login")
def test(request):
    return render(request,'test.html')

#parent site

@login_required(login_url = "/user/login")
def parentDash(request):
    return render(request,'parent/main-parent.html')
 