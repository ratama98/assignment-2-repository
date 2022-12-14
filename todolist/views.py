from urllib import request
from django.shortcuts import render
from todolist.models import Task
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.db import models

# Create your views here.
class NewTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

@login_required(login_url='/todolist/login/')
def show_html(request):
    data_todolist = Task.objects.filter(user=request.user)
    
    context = {
        "list": data_todolist ,
    }

    return render(request, "todolist.html", context)

def delete(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_html')

def show_json(request):
    data = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def add(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')

        task = Task(user=user, title=title, description=description)
        task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def add_task(request):
    form = NewTask()

    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.title = request.POST.get('title')
            task.description = request.POST.get('description')
            task.save()
        return redirect('todolist:show_html')

    context = {"form": form}
    return render(request, "add_task.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form.password1 = request.POST.get("password1")
        form.password2 = request.POST.get("password2")
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
        else:
            messages.info(request, 'Username atau Password salah!')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            return redirect('todolist:show_html')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')