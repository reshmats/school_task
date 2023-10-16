from django.contrib.auth import login

from django.shortcuts import render




# Create your views here.
def index(request):
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def form(request):
    return render(request,"form.html")


