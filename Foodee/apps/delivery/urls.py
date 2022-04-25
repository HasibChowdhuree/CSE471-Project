from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('dashboard/', views.delivery_dashboard, name='delivery_dashboard'),
    path('register/',views.register,name='deliveryman_register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='delivery/deliveryman_login.html'), name='delivery_login'),
]