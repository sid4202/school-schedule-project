from django.urls import path, include
from mainPage import views

urlpatterns = [
    path('adminpage', views.adminpage),
    path('studentpage', views.studentpage),
    path('adminlogin', views.adminlogin),
    path('', views.index)
]