from django.urls import path, include
from . import views
from user.views import logout

app_name = "dashboard"

urlpatterns = [
    path('logout',logout, name='vkids-logout'),

    #admin path
    path('admin',views.adminDash, name='vkids-admin_dashboard'),
    path('admin/bus',views.adminBus, name='vkids-admin_bus'),
    path('admin/kids',views.adminKids, name='vkids-admin_kids'),
    path('admin/statistics', views.adminStat, name='vkids-admin_statistics'),


    path('parent',views.test, name='vkids-parent_dashboard'),
    
]
