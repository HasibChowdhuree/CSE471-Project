from django.urls import path

from . import views

urlpatterns = [
    path('', views.send_food, name='send_food'),
]