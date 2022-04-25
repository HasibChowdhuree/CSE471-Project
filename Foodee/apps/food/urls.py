from django.urls import path

from . import views

urlpatterns = [
    # path('search/', views.search, name='search'),
    path('order-food/<slug:category_slug>/<slug:food_slug>/', views.food, name='food'),
    path('order-food/<slug:category_slug>/', views.category, name='category')
]