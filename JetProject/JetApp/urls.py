from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('index/',views.index),
    path('',views.Employee_form,name='Employee_insert'),
    path('index.html',views.index),
    path('category/index.html',views.Category),
    path('<int:id>/',views.Employee_form,name='Employee_update'),
    path('delete/<int:id>/',views.Employee_delete,name='Employee_delete'),
    path('list/', views.Employee_list,name='Employee_list'),

]