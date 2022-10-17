from pydoc import visiblename
from django.contrib import admin
from django.urls import path,include
from Hrtool import  views

urlpatterns = [
    path('',views.home , name="home")
]
