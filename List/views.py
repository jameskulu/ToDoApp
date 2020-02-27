from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):

  tasks = Task.objects.all()
  
  if request.method == 'POST':
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect("/")
  else:
     form = TaskForm() 
  context={'form':form,'tasks':tasks}
  return render(request,'List/index.html',context)

def update(request, id):
  tasks = Task.objects.get(id=id)
  if request.method == 'POST':
    form = TaskForm(request.POST, instance = tasks)
    if form.is_valid():
      form.save()
    return redirect("/")
  else:
    form = TaskForm(instance = tasks)
  context={'tasks':tasks,'form':form}
  return render(request,'List/update.html',context)

def delete(request, id):
  tasks = Task.objects.get(id=id)
  if request.method == 'POST':
      tasks.delete()
      return redirect("/")
  context={'tasks':tasks}
  return render(request,'List/delete.html',context)


