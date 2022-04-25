from django.forms import ModelForm
from apps.food.models import Food


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['category', 'image', 'title', 'description', 'price']