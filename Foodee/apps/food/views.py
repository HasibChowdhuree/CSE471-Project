from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
import random
from .models import Category, Food
from .forms import AddToCartForm
from apps.cart.cart import Cart
# Create your views here.

def food(request, category_slug, food_slug):
    cart = Cart(request)

    food = get_object_or_404(Food, category__slug=category_slug, slug=food_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']

            cart.add(product_id=food.id, quantity=quantity, update_quantity=False)

            messages.success(request, 'Item was added to the cart')

            return redirect('food', category_slug=category_slug, food_slug=food_slug)
    else:
        form = AddToCartForm()

    similar_products = list(food.category.foods.exclude(id=food.id))
    food = get_object_or_404(Food, category__slug=category_slug, slug=food_slug)

    similar_foods = list(food.category.foods.exclude(id=food.id))

    if len(similar_foods) >= 4:
        similar_foods = random.sample(similar_foods, 4)

    return render(request, 'food/food.html', {'food': food, 'similar_foods': similar_foods})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    return render(request, 'food/category.html', {'category': category})
