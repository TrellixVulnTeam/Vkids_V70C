from django.urls import path, include
from . import views
# from django.contrib.auth.views import LoginView

app_name = "authentication"

urlpatterns = [
    path('select',views.selectUser,name='vkids-select'),
    path('login', views.login, name='vkids-login'),
    path('select/signup/admin', views.adminRegister, name='vkids-adminRegister'),
    path('select/signup/parent', views.parentRegister, name='vkids-parentRegister'),
]
