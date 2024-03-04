from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_redirect, name='root to index redirect'), # redirect to index/
    path('index/', views.index, name='index page'),
]