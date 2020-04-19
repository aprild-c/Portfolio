from django.urls import path
from simple_page import views

urlpatterns = [
    path('', views.home, name='simple_page'),
    path('portfolio/', views.portfolio, name='simple_page'),
]