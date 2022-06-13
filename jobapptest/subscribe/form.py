from django import forms

from subscribe.models import Subscribe

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields = '__all__'

# def validate_comma(value):
#     if "," in value:
#         raise forms.ValidationError("Invalid Last Name")
#     return value

# class SubscribeForm(forms.Form):
#     # name = forms.CharField(label='Your name', max_length=100)
#     # email = forms.EmailField(label='Your email', max_length=100)

#     first_name = forms.CharField(max_length=100, required=False, label="Enter first name", help_text="Enter characters only")
#     last_name = forms.CharField(max_length=100, validators=[validate_comma])
#     email = forms.EmailField(max_length=100)

#     def clean_first_name(self):
#         data = self.cleaned_data['first_name']
#         if "," in data:
#             raise forms.ValidationError("Invalid First Name")
#         return data



