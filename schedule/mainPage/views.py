from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("<h4>МАКСИМ ГОМОСЕК!!</h4>")
    return render(request, 'mainpage/school1561.html')


def studentpage(request):
    return render(request, 'mainpage/studentpage.html')


def adminlogin(request):
    return render(request, 'mainpage/adminlogin.html')


def adminpage(request):
    return render(request, 'mainpage/adminpage.html')
