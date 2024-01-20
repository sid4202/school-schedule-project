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


def table(request):
    block = request.POST.get("block", "Undefined")
    grade = request.POST.get("grade", "Undefined")
    letter = request.POST.get("letter", "Undefined")
    combo = grade + letter
    from_sheet = ex.FromSheet(0, combo, 1)
    a = from_sheet.get_everything()
    c = ""
    for b in a:
        c += '<div class="element element-14"></div>\n<p class="text">' + str(b) + '</p>'
    return HttpResponse(c)


def adminpage(request):
    key = request.POST.get("key", "Undefined")
    if (key == "123"):
        return render(request, 'mainpage/adminpage.html')
    return HttpResponseRedirect("/")
