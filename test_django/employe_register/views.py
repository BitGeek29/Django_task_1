from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse

from .models import employeProfile, adminProfile

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #if user.user_type == 'user':
            #    return HttpResponse("Hello, World! User")
            #else:
            return HttpResponse("Hello, World!") #redirect('/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    #if request.user.is_authenticated:
    #    return HttpResponse("Hello, World! authorized")
    if request.method == 'POST' and False:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponse("Hello, World! Sigup Succesful")    
        else:
            return render(request, BASE_DIR / 'employe_register/templates/signup.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')

def simplehome(request):
    return HttpResponse("Hello, World! Homed")


def fetch_Data(request):
    if request.user.is_authenticated:
        if request.user.user_type == 'user':
                dataList = employeProfile.objects.all() 
        else:
                dataList = adminProfile.objects.all() 
        return render(request, BASE_DIR / "employe_register/templates",
        {
            'dataList' : load_data,
        })
    