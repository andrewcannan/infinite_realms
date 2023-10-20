from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('send_response/<int:contact_id>', views.send_response,
         name='send_response')
]
