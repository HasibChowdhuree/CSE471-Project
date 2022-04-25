from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from apps.food.models import Food

from .models import Restaurant
from .forms import FoodForm

# Create your views here.
def register_restaurant(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            restaurant = Restaurant.objects.create(name=user.username, created_by=user)
            return redirect('restaurant_admin')
    else:
        form=UserCreationForm()
    return render(request, 'restaurant/register_restaurant.html', {'form':form})

@login_required
def restaurant_admin(request):
    restaurant=request.user.restaurant
    foods=restaurant.foods.all()
    orders=restaurant.orders.all()

    for order in orders:
        order.restaurant_amount = 0
        order.restaurant_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.restaurant == request.user.restaurant:
                if item.restaurant_paid:
                    order.restaurant_paid_amount += item.get_total_price()
                else:
                    order.restaurant_amount += item.get_total_price()
                    order.fully_paid=False

    return render(request,'restaurant/restaurant_admin.html',{'restaurant':restaurant,'foods':foods,'orders':orders})

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)

        if form.is_valid():
            food = form.save(commit=False)
            food.restaurant = request.user.restaurant
            print(food.restaurant.id)
            
            food.slug = slugify(food.title)
            food.save()

            return redirect('restaurant_admin')
    else:
        form = FoodForm()
    
    return render(request, 'restaurant/add_food.html', {'form': form})