from django.urls import path
from . views import *


urlpatterns=[
    path("operation/",student_view),
    path("update/<int:id>/",update_student),
    path("delete_by_id/<int:id>/",delete_by_id),
    path("view_all_student/",view_all_student),
    path("view_by_id/<int:id>/",view_by_id),

]