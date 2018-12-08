from django.shortcuts import render,redirect
from user.forms import *

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login as builtInLogin, logout as builtInLogout


# Create your views here.

def selectUser(request):
        return render(request,'sign-up-choose.html')

def adminRegister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        admin_form = AdminForms(request.POST)

        if form.is_valid():
            uf = form.save(True,False)
            ad = admin_form.save(False)
            
            ad.user = uf
            ad.save()

            return redirect("/dashboard/admin")
            
    else:
        form = RegistrationForm()

        return render(request,'admin_register.html',{'form':form})

def parentRegister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(False,True)
            builtInLogin(request, user)
            return redirect("/dashboard/parent")
    else:
        form = RegistrationForm()
        return render(request,'parent_register.html',{'form':form})

def login(request):
     if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
             user = form.get_user()
             builtInLogin(request,user)
             if user.is_boss == True:
                return redirect("/dashboard/admin")
             elif user.is_parent == True:
                return redirect("/dashboard/parent")
     else:
        form = AuthenticationForm()

     return render(request,'login.html',{'form':form})

def logout(request):
     if request.method == 'POST':
        builtInLogout(request)
        return redirect("/")



