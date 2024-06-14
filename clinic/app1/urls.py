from django.contrib import admin
from django.urls import path
from app1 import views
from app1.views import UserRegisterView,UserLoginForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('contact.html',views.contact, name="contact"),
    path('about.html',views.about, name="about"),
    path('blog-single.html',views.blog_single, name="blog-single"),
    path('blog.html',views.blog, name="blog"),
    path('doctors.html',views.doctors, name="doctors"),
    path('services.html',views.services, name="services"),
    path('appointment',views.AppointmentView.as_view(), name="appointment"),
    path('register.html',views.UserRegisterView.as_view(), name="signup"),
    path('login',views.UserLoginView.as_view(), name="login"),
    path('user/out',views.Logout.as_view(),name='logout'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)