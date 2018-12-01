from django.shortcuts import render,redirect
from user.forms import RegistrationForm

# Create your views here.
def login(request):
    return render(request,'login.html')

def selectUser(request):
        return render(request,'user_select.html')

def adminRegister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegistrationForm()
        return render(request,'admin_register.html',{'form':form})

def parentRegister(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegistrationForm()
        return render(request,'parent_register.html',{'form':form})
# def adminRegister(request):
    


