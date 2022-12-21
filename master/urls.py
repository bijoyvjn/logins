from django.urls import path
from .views import *

urlpatterns = [
    path('', student_home, name='student_home'),
    path('staff_home', staff_home, name='staff_home'),
    path('editor_home', editor_home, name='editor_home'),
    path('admin_home', admin_home, name='admin_home'),
]
