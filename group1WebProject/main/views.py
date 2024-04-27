from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from users.forms import LoginUserForm

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
def unauthorized(request):
    return render(request, 'main/unauthorized_access.html')

def about(request):
    return HttpResponse("<h1>about</h1>")

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_content = {'title': 'Авторизация'}
