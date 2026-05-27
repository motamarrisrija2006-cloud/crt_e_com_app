from django.urls import path

from .views import *

urlpatterns = [

    path('add_product/', add_product),

    path('display/', display_products),

    path('add_to_cart/<int:id>/', add_to_cart),

    path('cart/', cart_page),

    path('delete/<int:id>/', delete_product),

    path('update/<int:id>/', update_product),

]