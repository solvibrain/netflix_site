from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate

# Create your views here.
def index(request):
    return render(request,'index.html')


def add_to_list(request):
    pass

def user_login(request):
    return render(request,"login.html")

def user_signup(request):
    return render(request,"signup.html")

def user_logout(request):
    logout(request)
    
