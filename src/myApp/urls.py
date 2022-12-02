"""project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    # /myApp/ 주소
    path('', views.index),

    path('apartment/', views.apartment),

    path('home/', views.home),

    path('home/home_1.html/', views.home_1),    

    path('home/home_2.html/', views.home_2),    

    path('home/home_3.html/', views.home_3) ,   

    path('home/home_4.html/', views.home_4)  ,  

    path('home/home_5.html/', views.home_5)   , 

    path('home/home_6.html/', views.home_6)    ,

    path('home/home_7.html/', views.home_7)    ,

    path('home/home_8.html/', views.home_8)    ,

    path('home/home_9.html/', views.home_9)    ,

    path('home/home_10.html/', views.home_10)   , 

    path('home/home_11.html/', views.home_11)    ,

    path('home/home_12.html/', views.home_12)    ,

    path('home/home_13.html/', views.home_13)    ,

    path('home/home_14.html/', views.home_14)    ,

    path('home/home_15.html/', views.home_15)    ,

    path('home/home_16.html/', views.home_16)    ,

    path('home/apartment.html/', views.apartment)    ,

    path('home/apartment/graph_1.html/', views.graph_1)    ,

    path('searchCon/', views.searchCon),
    
    path('search/', views.search),

]
