from django.urls import path, include
from . import views
from user.views import logout

app_name = "dashboard"

urlpatterns = [
    path('admin',views.adminDash,name='vkids-admin_dashboard'),
    path('logout',logout, name='vkids-logout'),
    path('parent',views.test, name='vkids-parnt_dashboard')
]
