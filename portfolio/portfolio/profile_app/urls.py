from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home, name='home'),

    path('contact/', views.contact, name='contact'),
    path('grade/<int:marks>/',views.grade,name='grade'),
    path('students/',views.students,name='students'),
    path('user_form/',views.user_form,name='user_form'),

]