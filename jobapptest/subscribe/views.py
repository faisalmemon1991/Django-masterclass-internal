from django.shortcuts import redirect, render
from django.urls import reverse

from subscribe.form import SubscribeForm
from subscribe.models import Subscribe

# Create your views here.
def thank_you(request):
    context={}
    return render(request,"subscribe/thank_you.html",context)

def subscribe(request):
    subscribe_form = SubscribeForm()
    # email_error_empty=""
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            print("valid form")
            # subscribe_form.save()
            email = subscribe_form.cleaned_data['email']
            first_name = subscribe_form.cleaned_data['first_name']
            last_name = subscribe_form.cleaned_data['last_name']
            print(email)
        # if email=="":
        #     email_error_empty = "No email entered";

            subscribe = Subscribe(first_name = first_name, last_name = last_name, email = email)
            subscribe.save()
            print(f"{subscribe.first_name} - {subscribe.email}")
            return redirect(reverse('thank_you'))
    context={"form":subscribe_form}
    return render(request,"subscribe/subscribe.html",context)
