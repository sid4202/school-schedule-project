from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import ex


def index(request):
    # return HttpResponse("<h4>МАКСИМ ГОМОСЕК!!</h4>")
    return render(request, 'mainpage/index.html')


def studentpage(request):
    return render(request, 'mainpage/studentpage.html')


def adminlogin(request):
    return render(request, 'mainpage/adminlogin.html')


def table(request, c=""):
    block = request.POST.get("block", "Undefined")
    grade = request.POST.get("grade", "Undefined")
    letter = request.POST.get("letter", "Undefined")
    for i in range(5):
        for j in range(8):
            from_sheet = ex.FromSheet(i, grade + letter, j+1)
            a = from_sheet.get_everything()
            day = ""
            if (a[2] == 0):
                day = "Понедельник"
            elif (a[2] == 1):
                day = "Вторник"
            elif (a[2] == 2):
                day = "Среда"
            elif (a[2] == 3):
                day = "Четверг"
            elif (a[2] == 4):
                day = "Пятница"
            c += '<div class="element element-14"></div>\n<p class="text">' + a[1] + " | " + a[0] + " | " + str(day) + " | Номер урока: " + str(a[4]) + '</p>'
        c+= '<h4>.</h4>'
    return HttpResponse(c)


def adminpage(request):
    key = request.POST.get("key", "Undefined")
    if (key == "123"):
        return render(request, 'mainpage/adminpage.html')
    return HttpResponseRedirect("/")
