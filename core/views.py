from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')



def add_to_list(request):
    pass

    """
    A view function that handles user login.

    Parameters:
        request (HttpRequest): The HTTP request object containing the user's login information.

    Returns:
        HttpResponse: The rendered login.html template.

    Raises:
        None
    """
def user_login(request):
    return render(request,"login.html")

def user_signup(request):
    if request.method=="POST":
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_confirm_password = request.POST.get('confirm_password')
        user_name = request.POST.get('username')

        if user_password == user_confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username Taken")
                return redirect('signup')
            elif User.objects.filter(email=user_email).exists():
                messages.info(request,"Email Taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=user_name,email=user_email,password=user_password)
                user.save()
                user_login = authenticate(username=user_name,password=user_password)
                login(request,user_login)
                return redirect('index')
        else:
            messages.info(request,"Password not matching")
            return redirect('signup')


    else:
        return render(request,"signup.html")

def user_logout(request):
    logout(request)
    
