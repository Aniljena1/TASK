from django.urls import path
from celeryapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send),

]