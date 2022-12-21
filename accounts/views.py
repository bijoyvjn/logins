from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import *


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.password1 = request.POST.get('password1')
            data.password2 = request.POST.get('password2')
            data.is_staff = True
            data.save()
            messages.success(request, 'New User Successfully Created', 'alert-success')
            return redirect('login')
        else:
            messages.success(request, 'Invalid Data', 'alert-danger')
    else:
        form = UserRegForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'student':
                return redirect('student_home')
            elif user.role == 'staff':
                return redirect('staff_home')
            elif user.role == 'admin':
                return redirect('admin_home')
            elif user.role == 'editor':
                return redirect('editor_home')
        else:
            context = {'msg': 'Invalid Username or Password'}
            return render(request, "registration/login.html", context)
    else:
        return render(request, "registration/login.html")
