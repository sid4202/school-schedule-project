from django.urls import path, include
from . import views

urlpatterns = [
    path('studentpage', views.studentpage),
    path('', views.index)
]