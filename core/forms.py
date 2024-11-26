from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Customer_Detail


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirm Password'}))
    class Meta:
        model =User
        fields = ['username','first_name','last_name','email','password1','password2']
        labels ={'email':'Email'}
        widgets= {'username':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Username'}),
                  'email':forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}),
                  }

class loginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))


class UserEditForm(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class AdminEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'

class Customer_Form(forms.ModelForm):
    class Meta:
        model = Customer_Detail
        fields=['name','address','city','state','pincode']
        labels ={'name':'Full Name'}
        widgets= {'name':forms.TextInput(attrs={'class':'form-control'}),
                  'address':forms.TextInput(attrs={'class':'form-control'}),
                  'city':forms.TextInput(attrs={'class':'form-control'}),
                  'state':forms.Select(attrs={'class':'form-control'}),
                  'pincode':forms.NumberInput(attrs={'class':'form-control'}),
                  }