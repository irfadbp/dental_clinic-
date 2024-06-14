from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from app1.forms import UserRegisterForm,UserLoginForm
from app1.models import Appointment


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'home.html',)

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']  # here message-name comes from contact.html file's input type name
        message_email = request.POST['message-email']
        message = request.POST['message-subject']

        send_mail(
            message_name, 
            message, 
            message_email, 
            ['nanoman895@gmail.com'], 
        )

        return render(request, 'contact.html', {'message-name':message_name})

    else:
        return render(request, 'contact.html',{})

    
def about(request):
    return render(request,'about.html',{})

def blog(request):
    return render(request,'blog.html',{})

def doctors(request):
    return render(request,'doctors.html',{})

def services(request):
    return render(request,'services.html',{})

def blog_single(request):
    return render(request,'blog-single.html',{})

# class UserRegisterView(View):
#     def get(self, request, *args, **kwargs):
#         form=UserRegisterForm()
#         return render(request,'register.html',{'form':form})
#     def register(request):
#         if request.method == 'POST':
#             form = UserRegisterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             return redirect('registration_success')  # Redirect to a success page
#         else:
#             form =UserRegisterForm()
#         return render(request, 'register.html', {'form': form})


# class UserRegisterView(View):
#     def get(self, request, *args, **kwargs):
#         form=UserRegisterForm()
#         return render(request,'register.html',{'form':form})
#     def Signup(request):
#         if request.method=='POST':
#             uname=request.POST.get('username')
#             email=request.POST.get('email')
#             pass1=request.POST.get('password1')
#             pass2=request.POST.get('password2')
#             if pass1!=pass2:
#                 return messages.error(request,"Your password and confrom password are not Same!!")
#             else:

#                 my_user=User.objects.create_user(uname,email,pass1,pass2)
#                 my_user.save()
#                 return redirect('login')
#             return render (request,'signup')


# class UserRegisterView(View):
#     def get(self, request, *args, **kwargs):
#         form=UserRegister()
#         return render(request,'register.html',{'form':form})
    
#     def post(self, request, *args, **kwargs):
#         form=UserRegister(request.POST)
#         if form.is_valid():
#              User.objects.create_user(**form.cleaned_data)
#              messages.success(request,'registration successful')
#              return redirect('login')
#         else:
#             messages.error(request,'invalid')
#             return redirect('home')
        

class UserRegisterView(View):
    def get(self, request, *args, **kwargs):
        form=UserRegisterForm()
        return render(request,'register.html',{'form':form})
    
    def post(self, request, *args, **kwargs):
        form=UserRegisterForm(request.POST)
        if form.is_valid():
             User.objects.create_user(**form.cleaned_data)
             messages.success(request,'registration successful')
             return redirect('login')
        else:
            messages.error(request,'invalid')
            return redirect('home')
         

class UserLoginView(View):
    def get(self, request, *args, **kwargs):
        form = UserLoginForm()
        return render(request, 'login.html', {'form':form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['pass']
            user = authenticate(username=username,password=password)

        if user:
            login(request,user)  # Corrected the parameter to user
            messages.success(request,'Login successful')
            return redirect('home')
        else:
            messages.error(request,'Invalid email or password')
            return redirect('login')


class Logout(View):
    def get(self,request):
        logout(request)
        messages.success(request,'Logout Successful')
        return redirect('home')

class AppointmentView(View):
    def get(self,request):
        return render(request,'appointment.html',)
    
    def post(self,request):
        fname=request.POST.get('name')
        email=request.POST.get('email')
        date=request.POST.get('date')
        time=request.POST.get('time')
        message=request.POST.get('request')

        appointment = Appointment.objects.create(
            first_name=fname,
            email=email,
            sent_date=date,
            request=message,
        )

        appointment.save()

        messages.add_message(request,messages.success,f"thanks {fname} for making an appointment")
        return HttpResponseRedirect(request.path)
