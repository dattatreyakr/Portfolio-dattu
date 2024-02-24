from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import wrk,userfeedback

# Create your views here.
def home(request):
    wrks=wrk.objects.all()
    return render(request,"index1.html",{'wrks': wrks,'name':'portfolio'})


def log(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password'] 

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'user does not exists')
            return redirect('log')
          
    else:
        return render(request,'login.html')  

def register(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'password not matching')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'password not matching')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('log')
        else:
           messages.info(request,'password not matching')
        return redirect('register')

    else:
        return render(request,'reg.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def userfeed(request):
    if request.method=='POST':
        nm=request.POST['Name']
        ph=request.POST['Contact_Number']
        em=request.POST['Email']
        msg=request.POST['Message']
        feeds=userfeedback(name=nm,phone=ph,email=em,msg=msg)
        feeds.save()
    return redirect('/')