from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/index.html')
def page2(request):
    return render(request, 'main/page2.html')
def page3(request):
    return render(request, 'main/page3.html')
def about(request):
    return HttpResponse("<h1>about</h1>")
