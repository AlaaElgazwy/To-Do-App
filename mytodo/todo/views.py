from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
# Create your views here.
@login_required(login_url='login')
def index(request):

    tasks=Task.objects.filter(user=request.user)
    
          
    form=TaskForm()
    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            task=form.save(commit=False)
            task.user=request.user
            task.save()
        return redirect('/')
        
    return render(request,'index.html',{'tasks':tasks, 'form':form})
@login_required(login_url='login')
def updateTask(request ,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)

    if request.method == 'POST':
        form =TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')    
    return render(request,'update.html',{'form':form})
@login_required(login_url='login')
def deleteTask(request,pk):    
    task=Task.objects.get(id=pk)
    if request.method=='POST':
       task.delete()

       return redirect('/')
    return render(request,'delete.html',{'task':task})
