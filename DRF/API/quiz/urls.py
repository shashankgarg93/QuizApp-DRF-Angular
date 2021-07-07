from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from .views import questions
urlpatterns = [
    path('', questions),

]
