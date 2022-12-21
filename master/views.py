from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def student_home(request):
    template_name = 'student_home.html'
    return render(request, template_name)


@login_required()
def staff_home(request):
    template_name = 'staff_home.html'
    return render(request, template_name)


@login_required()
def editor_home(request):
    template_name = 'editor_home.html'
    return render(request, template_name)


@login_required()
def admin_home(request):
    template_name = 'admin_home.html'
    return render(request, template_name)
