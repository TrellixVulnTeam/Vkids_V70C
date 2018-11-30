from django.shortcuts import render,redirect
from user.forms import RegistrationForm

# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegistrationForm()
        return render(request,'register.html',{'form':form})

