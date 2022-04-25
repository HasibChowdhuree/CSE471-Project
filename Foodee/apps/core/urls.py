from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.frontpage,name='frontpage'),
    path('contact/',views.contact,name='contact'),
    path('order-food/',views.order_food,name='order_food'),
    path('order-food/restaurant/<int:restaurant_id>/', views.restaurant, name='restaurant_page'),
    path('register/',views.register,name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
]