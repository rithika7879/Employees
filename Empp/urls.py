from django.contrib import admin
from django.urls import path,include
from Empp.views import employees,EmpView,index

from rest_framework.routers import DefaultRouter
from .views import EmpViewSet

router = DefaultRouter()
router.register(r'Employees', EmpViewSet)

urlpatterns = [
    path("data/",index),
    path('Employees/',employees, name= 'Employees',),
    
    path('Empl/',EmpView.as_view(), name= 'Employees'),
    
]+router.urls
