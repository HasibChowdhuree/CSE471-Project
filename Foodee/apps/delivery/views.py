from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from apps.order.models import Order
from apps.send.models import Send
from apps.restaurant.models import Restaurant

# Create your views here.
def delivery_dashboard(request):
    orders=Order.objects.all()
    sends=Send.objects.all()
    return render(request, 'delivery/delivery_dashboard.html',{'orders':orders,'sends':sends})

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
    return render(request, 'delivery/deliveryman_register.html', {'form':form})
