"""project11_insertionformdatabyselect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('insert_webpage/',insert_webpage,name='insert_webpage'),
    path('insert_access/',insert_access,name='insert_access'),
    path('retrieve_checkbox_topic/',retrieve_checkbox_topic,name='retrieve_checkbox_topic'),
    path('retrieve_select_topic/',retrieve_select_topic,name='retrieve_select_topic'),
    path('retrieve_access_select/',retrieve_access_select,name='retrieve_access_select'),
    path('update_webpage/',update_webpage,name='update_webpage'),
    path('update_access/',update_access,name='update_access'),
    path('delete_topic/',delete_topic,name='delete_topic'),
    path('delete_webpage/',delete_webpage,name='delete_webpage'),
]
