from django.urls import path
from . import views

urlpatterns = [
    # Define your URL patterns here
    # Example:
    path('get-image-txt-list/', views.get_image_txt_list, name='get-image-txt-list'),
]