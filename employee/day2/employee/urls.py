from django.urls import path
from .views import add_employee, get_employee_details,get_emp_by_id,delete_by_id

urlpatterns=[
    path('add_emp/',add_employee),
    path('get_data/',get_employee_details),
    path('get_emp_by_id/<int:id>',get_emp_by_id),
    path('del_emp_by_id/<int:id>',delete_by_id),
]