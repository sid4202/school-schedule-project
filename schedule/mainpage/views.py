from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("<h4>МАКСИМ ГОМОСЕК!!</h4>")
    return render(request, 'mainpage/index.html')