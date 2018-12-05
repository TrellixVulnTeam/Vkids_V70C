from django.urls import path, include
from . import views
from user.views import logout

app_name = "dashboard"

urlpatterns = [
    path('',views.adminDash,name='vkids-dashboard'),
    path('logout',logout, name='vkids-logout'),
]
