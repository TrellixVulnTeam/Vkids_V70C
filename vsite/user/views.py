from django.shortcuts import render,redirect
from user.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login as builtInLogin, logout as builtInLogout


# Create your views here.

def selectUser(request):
        return render(request,'sign-up-choose.html')

def adminRegister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save(True,False)
            return redirect("/dashboard")
    else:
        form = RegistrationForm()

        return render(request,'admin_register.html',{'form':form})

def parentRegister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(False,True)
            builtInLogin(request, user)
            return redirect("/dashboard")
    else:
        form = RegistrationForm()
        return render(request,'parent_register.html',{'form':form})

def login(request):
     if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
             user = form.get_user()
             builtInLogin(request,user)
             return redirect("/dashboard")
     else:
        form = AuthenticationForm()

     return render(request,'login.html',{'form':form})

def logout(request):
     if request.method == 'POST':
        builtInLogout(request)
        return redirect("/")



