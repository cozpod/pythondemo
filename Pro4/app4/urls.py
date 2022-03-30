from django.urls import path
from . import views

urlpatterns = [
    path('',views.Employee_form,name='Employee_insert'),
    # path('singup/',views.Regform,name='Registraion Form'),
    path('<int:id>/',views.Employee_form,name='Employee_update'),
    path('delete/<int:id>/',views.Employee_delete,name='Employee_delete'),
    path('list/', views.Employee_list,name='Employee_list'),

    path('catagory',views.catagory_form,name='category_page'),
    path('<int:id>/',views.catagory_form,name='category_update'),
    path('delete/<int:id>/',views.catagory_delete,name='category_delete'),
    path('categorylist/',views.catagory_list,name='catagory_list'),
    
    path('subcatagory',views.subcatagory,name='subcategory_page'),

]

