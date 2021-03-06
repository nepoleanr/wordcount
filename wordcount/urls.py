"""wordcount URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    path('', views.homePage, name='home'),
    path('about/', views.about, name='about'),
    path('count/', views.count, name='count'), # (path_to_page, filename.func_name, a_name_for_the_path)
    # name='count' -> This means that we could change the name of the path from count/ to abcd/, and it will still work.
]
