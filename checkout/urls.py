from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_suscess,
         name='checkout_success')
]
