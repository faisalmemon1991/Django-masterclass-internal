from django import forms
from django.utils.translation import gettext_lazy as _

from blogapp.models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields = {'content','email','name','website'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
        
        self.fields['content'].widget.attrs['placeholder'] = 'Type your comment....'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['website'].widget.attrs['placeholder'] = 'Website'