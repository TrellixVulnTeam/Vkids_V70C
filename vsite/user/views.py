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
        admin = AdminForm(request.POST)

        if form.is_valid():
            user_form = form.save(True,False)
            admin_fom = admin.save(False)
            admin_fom.user = user_form
            admin_fom.save()
            builtInLogin(request, user_form)

            return redirect("/dashboard/admin")
            
    else:
        form = RegistrationForm()

        return render(request,'admin_register.html',{'form':form})

def parentRegister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        parent = ParentForm(request.POST)

        if form.is_valid():
            user_form = form.save(False,True)
            parent_form = parent.save(False)
            parent_form.user = user_form
            builtInLogin(request, user_form)
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



