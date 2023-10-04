from django.urls import path
from . import views

urlpatterns = [
    path('<int:product_id>', views.reviews, name='reviews'),
    path('add_review/<int:product_id>', views.add_review, name='add_review')
]
