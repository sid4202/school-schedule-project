from django.urls import path, include
from . import views

urlpatterns = [
    path('table', views.table),
    path('adminpage', views.adminpage),
    path('studentpage', views.studentpage),
    path('adminlogin', views.adminlogin),
    path('', views.index)
]