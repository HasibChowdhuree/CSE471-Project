from django.db import models

# Create your models here.
class Send(models.Model):
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    sender_email = models.CharField(max_length=100)
    receiver_email = models.CharField(max_length=100)
    sender_phone = models.CharField(max_length=100)
    receiver_phone = models.CharField(max_length=100)
    sender_address = models.CharField(max_length=100)
    receiver_address = models.CharField(max_length=100)
    price=models.CharField(max_length=100,default=100)