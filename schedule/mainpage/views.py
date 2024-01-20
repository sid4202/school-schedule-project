from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    # return HttpResponse("<h4>МАКСИМ ГОМОСЕК!!</h4>")
    return render(request, 'mainpage/index.html')


def studentpage(request):
    return render(request, 'mainpage/studentpage.html')


def adminlogin(request):
    return render(request, 'mainpage/adminlogin.html')


def table(request):
    block = request.POST.get("block", "Undefined")
    grade = request.POST.get("grade", "Undefined")
    letter = request.POST.get("letter", "Undefined")
    combo = grade + letter
    a = ['dasd', 'adasd', 'dadsw']
    c = ""
    for b in a:
        c += '<div class="element element-14"></div>\n<p class="text">' + b + '</p>'
    return HttpResponse(c)


def adminpage(request):
    key = request.POST.get("key", "Undefined")
    if (key == "123"):
        return render(request, 'mainpage/adminpage.html')
    return HttpResponseRedirect("/")
