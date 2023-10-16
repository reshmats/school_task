from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth,messages


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'INVALID CREDENTIALS')
            return redirect('login')

    return render(request,"login.html")




def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                messages.success(request, "User Created")
                return redirect('login')

        else:
            messages.info(request,"Password Not Matching")
            return redirect('register')
        return redirect('/')


    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

