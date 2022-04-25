from django import forms

class SendForm(forms.Form):
    sender_name = forms.CharField(max_length=100)
    receiver_name = forms.CharField(max_length=100)
    sender_email = forms.CharField(max_length=100)
    receiver_email = forms.CharField(max_length=100)
    sender_phone = forms.CharField(max_length=100)
    receiver_phone = forms.CharField(max_length=100)
    sender_address = forms.CharField(max_length=100)
    receiver_address = forms.CharField(max_length=100)