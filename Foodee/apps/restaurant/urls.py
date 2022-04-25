from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register-restaurant/',views.register_restaurant,name='register_restaurant'),
    path('restaurant-admin/',views.restaurant_admin,name='restaurant_admin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='restaurant/login.html'), name='restaurant_login'),
    path('add-food/', views.add_food, name='add_food'),
]