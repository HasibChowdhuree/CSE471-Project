from django.shortcuts import render,redirect
from .forms import SendForm
from .models import Send
from django.contrib import messages

# Create your views here.

def send_food(request):

    if request.method == 'POST':
        form = SendForm(request.POST)

        if form.is_valid():

            try:

                sender_name = form.cleaned_data['receiver_name']
                sender_email = form.cleaned_data['receiver_email']
                sender_phone = form.cleaned_data['receiver_phone']
                sender_address = form.cleaned_data['receiver_address']
                receiver_name = form.cleaned_data['receiver_name']
                receiver_email = form.cleaned_data['receiver_email']
                receiver_phone = form.cleaned_data['receiver_phone']
                receiver_address = form.cleaned_data['receiver_address']

                Send.objects.create(
                    sender_name = sender_name,
                    sender_email = sender_email,
                    sender_phone = sender_phone,
                    sender_address = sender_address,
                    receiver_name = receiver_name,
                    receiver_email = receiver_email,
                    receiver_phone = receiver_phone,
                    receiver_address = receiver_address
                )


                return redirect('frontpage')
            except Exception:
                messages.error(request, 'There was something wrong')
    else:
        form = SendForm()

    return render(request,'send/send.html', {'form': form,})
