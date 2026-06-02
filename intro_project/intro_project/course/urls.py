
from django.urls import path
from .views import *

urlpatterns = [
    path("method/",  greet),
    path("name/",  get_name),


]
