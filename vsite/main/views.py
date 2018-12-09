from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from person.models import *
from .models import *

# Create your views here.

@login_required(login_url = "/user/login")
def adminDash(request):
    return render(request,'main-admin.html')

@login_required(login_url = "/user/login")
def adminKids(request):
    admin = Admin.objects.get(user = request.user)
    student_list = Student.objects.filter(school = admin.school)
    
    form = { 'students' : [] }
    
    for student in student_list:
        student_dic = {
                'bus' : student.getBus(),
                'name' : student.getName(),
                'status' : student.getStatus(),
                'bag_weight' : student.getBagWeight(),
                'phone' : '089-0527782',
        }
        form['students'].append(student_dic)

    return render(request,'kids_data.html',form)

@login_required(login_url = "/user/login")
def adminBus(request):
    return render(request,'Car_Data.html')

@login_required(login_url = "/user/login")
def adminStat(request):
    return render(request, 'Stat_Data.html')

def test(request):
        return render(request,'test.html')