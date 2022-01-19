from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('quizpage/',views.quizpage,name='quizpage'),
    path('api/',views.getapi,name='getapi')
]