from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class UserRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'mobile', 'nationality', 'country', 'role']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'required': 'True', 'placeholder': 'First Name',
                       'pattern': '[A-Za-z]{3,50}( [A-Za-z]{1,50})?',
                       'title': 'Name should contain only alphabets and it should have at least 3 letters'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name',
                                                'pattern': '[A-Za-z]{3,50}( [A-Za-z]{1,50})?',
                                                'title': 'Name should contain only alphabets and it should have atleast 3 letters'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'required': 'true',
                                             'placeholder':'Mobile Number','pattern': '[0-9]{10}',
                                             'title': 'Mobile Number Should have 10 digits'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': 'true',
                                            'placeholder':'Email','pattern': '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{3,4}$',
                                            'title': 'Enter a valid email id'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'required': 'true',
                                              'placeholder':'Country','pattern': '[A-Za-z]{4,50}( [A-Za-z]{4,50})?',
                                              'title': 'Country should contain only alphabets and it should have atleast 4 letters'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'required': 'true',
                                                  'placeholder':'Nationality','pattern': '[A-Za-z]{4,50}( [A-Za-z]{4,50})?',
                                                  'title': 'Nationality should contain only alphabets and it should have atleast 4 letters'}),
            'role': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            # 'password1': forms.TextInput(
            #     attrs={'class': 'form-control', 'required': 'true', 'type': 'password',
            #            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d$@$!%*?&]{8,}',
            #            'title': 'Password should have minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character '}),
            # 'password2': forms.TextInput(
            #     attrs={'class': 'form-control', 'required': 'true', 'type': 'password',
            #            'pattern': '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d$@$!%*?&]{8,}',
            #            'title': 'Password should have minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character '})

        }
