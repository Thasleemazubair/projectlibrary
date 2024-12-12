"""
URL configuration for libraryproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from libraryapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('admin/',views.admin, name='admin'),
    path('students/',views.students, name='students'),
    path('index/', views.home),
    path('adminclick/',views.admin),
    path('studentclick/',views.students),
    path('aboutusclick/',views.aboutus),
    path('contactusclick/',views.contactus),
    path('adminsignup/',views.admin_signup_view),
    path('studentsignup/', views.student_signup_view),
    path('admin_signup/',views.admin_signup)



]
