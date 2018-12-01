from django.shortcuts import render

# Create your views here.
def adminDash(request):
    return render(request,'main-admin.html')