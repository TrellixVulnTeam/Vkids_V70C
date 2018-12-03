from django.urls import path, include
from . import views
from user.views import logout


urlpatterns = [
    path('',views.adminDash,name='vkids-dashboard'),
    path('logout',logout, name='vkids-logout'),
]
