from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login', views.login, name='vkids-login'),
    path('signup', views.register, name='vkids-register'),
]
