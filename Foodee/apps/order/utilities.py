from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from apps.cart.cart import Cart

from .models import Order, OrderItem

def checkout(request, first_name, last_name, email, address, zipcode, place, phone, amount):
    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place, phone=phone, paid_amount=amount)

    for item in Cart(request):
        OrderItem.objects.create(order=order, food=item['food'], restaurant=item['food'].restaurant, price=item['food'].price, quantity=item['quantity'])
    
        order.restaurants.add(item['food'].restaurant)

    return order

# def notify_restaurant(order):
#     from_email = settings.DEFAULT_EMAIL_FROM

#     for restaurant in order.restaurants.all():
#         to_email = restaurant.created_by.email
#         subject = 'New order'
#         text_content = 'You have a new order!'
#         html_content = render_to_string('order/email_notify_restaurant.html', {'order': order, 'restaurant': restaurant})

#         msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
#         msg.attach_alternative(html_content, 'text/html')
#         msg.send()

# def notify_customer(order):
#     from_email = settings.DEFAULT_EMAIL_FROM

#     to_email = order.email
#     subject = 'Order confirmation'
#     text_content = 'Thank you for the order!'
#     html_content = render_to_string('order/email_notify_customer.html', {'order': order})

#     msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()