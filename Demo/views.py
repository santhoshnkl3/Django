from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse


# Create your views here.
from .forms import Login_Form

def index(request):
    title='Login Form'
    if request.method=='POST':
        form=Login_Form(request.POST)

        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        login(request,user)
        print(user.is_authenticated)
        return HttpResponse("You have been loged in as "+user.username)
    #form=UserLoginForm(None)
    form=Login_Form(None)
    return render(request, "registration/login.html",{'form':form,'title':title})

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)

            login(request,user)
            print(user.is_authenticated)
            return redirect('index')

    else:
        form=UserCreationForm()
    context={'form':form}
    return render(request,'registration/sample.html',context )
