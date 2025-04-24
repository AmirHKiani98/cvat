from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    # Example:
    path('process/', views.process_image, name='process'),
]