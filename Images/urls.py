from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('display/<int:image_id>/', views.display_image, name='display_image'),
]