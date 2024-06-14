from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={
            # 'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'FirstName'}),
            # 'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'LastName'}),
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'UserName'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

class UserLoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),
            'password': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
        }