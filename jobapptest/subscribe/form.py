from django import forms


class SubscribeForm(forms.Form):
    # name = forms.CharField(label='Your name', max_length=100)
    # email = forms.EmailField(label='Your email', max_length=100)

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)