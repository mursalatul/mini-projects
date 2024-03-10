from django.urls import path
from . import views

urlpatterns = [
    path('imgresizer/', views.resizer, name='image resizer'),
    path('imgprocess/', views.imgprocess, name='imgprocess'),
]