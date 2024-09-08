"""
URL configuration for myproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from testingApp.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get/',get),
    path('api/post/CV',upload_CV),
    path('api/post/publications',upload_publications),
    path('api/post/personalDetails',create_personal_details),
    path('api/post/profile',upload_profile_image),
    path('api/post/specialization',create_specialization_details),
    path('api/post/subject',create_subject_details),
    path('api/post/research',create_research_details),
    path('api/post/consultancy',create_consultancy_details),
    

]