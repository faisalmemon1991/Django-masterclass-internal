from .models import Uploads  
from django import forms

class UploadForm(forms.ModelForm):  
    class Meta:    
        model = Uploads  
        fields = '__all__'  