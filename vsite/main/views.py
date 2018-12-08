from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url = "/user/login")
def adminDash(request):
    return render(request,'main-admin.html')

@login_required(login_url = "/user/login")
def adminKids(request):
    return render(request,'kids_data.html')

@login_required(login_url = "/user/login")
def adminBus(request):
    return render(request,'Car_Data.html')
    
@login_required(login_url = "/user/login")
def adminStat(request):
    return render(request, 'Stat_Data.html')

def test(request):
        return render(request,'test.html')