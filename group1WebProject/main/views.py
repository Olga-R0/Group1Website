from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    return render(request, 'main/main.html')
def singin(request):
    return render(request, 'main/singin.html')
def page2(request):
    return render(request, 'main/page2.html')
def page3(request):
    return render(request, 'main/page3.html')
def page4(request):
    return render(request, 'main/page4.html')
def about(request):
    return HttpResponse("<h1>about</h1>")
