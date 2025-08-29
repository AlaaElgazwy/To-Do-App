from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm

# Create your views here.
def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    return render(request,'register.html',{'form':form})    
def loginUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
        return redirect('/')
    return render(request,'login.html')
def logoutUser(request):
    logout(request)
    return redirect('login')
    
