from django.shortcuts import render,redirect # for rendering and redirecting Html pages
from django.contrib.auth import logout,login,authenticate # this is for using Built in function of login,logout and authenticate from Django
from django.contrib.auth.models import User # Importing User Table from Database and Similarly anyother Table can also be imported
from django.contrib import messages # for sending messages to Frontend of all types that we want to send from Server
from.backends import CustomAuthBackend # This is for using Custom Authentication that I can use both email and username for authentication


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
# this is the implementation of login functionality 
def user_login(request):
    #Implementing login logic
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        # user = authenticate(username=user_name,password=user_password)
        # Implemented authentication using CustomBackend using both username and email , Importing CustomBackend from Backends.py file 
        user = CustomAuthBackend().authenticate(request, username=user_name, password=user_password)
        if user is not None:
            user.backend = 'core.backends.CustomAuthBackend'
            login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/login')
        
    return render(request,"login.html")

def user_signup(request):
    if request.method=="POST":
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        user_confirm_password = request.POST.get('confirm_password')
        user_name = request.POST.get('username')
        # From here adding some of the Verification in password and username and email
        if user_password == user_confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username Taken")
                return redirect('signup')
            elif User.objects.filter(email=user_email).exists():
                messages.info(request,"Email Taken")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=user_name,email=user_email,password=user_password) # Creating user the Built in function of django
                user.save() # saving the user that is Created After this I can do two process I can send user to login page or let them login from here
                user_login = authenticate(username=user_name,password=user_password) # Authneticating user using Builtint function
                # Here user automaticaly get login to application after Signing up to application
                login(request,user_login)
                return redirect('index')# after login redirecting user  to home page
        else:
            messages.info(request,"Password not matching")
            return redirect('signup')


    else:
        return render(request,"signup.html")

def user_logout(request):
    logout(request)
    return redirect('index')
    
