from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from apps.food.models import Food

from apps.restaurant.models import Restaurant

# Create your views here.
def  frontpage(request):
    return render(request,'core/frontpage.html')

def contact(request):
    return render(request,'core/contact.html')

def order_food(request):
    newest = Food.objects.all()[0:8]
    excludes = ['sampledelivery', 'sampleuser','Hasib']
    restaurants = Restaurant.objects.exclude(name__in=excludes)
    return render(request,'core/order_food.html', {'newest':newest,'restaurants':restaurants})

def restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    return render(request, 'core/restaurant.html', {'restaurant': restaurant})
def register(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            restaurant = Restaurant.objects.create(name=user.username, created_by=user)
            return redirect('frontpage')
    else:
        form=UserCreationForm()
    return render(request, 'core/register.html', {'form':form})