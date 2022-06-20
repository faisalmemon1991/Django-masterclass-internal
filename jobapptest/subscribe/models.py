from re import M
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

def validate_comma(value):
    if "," in value:
        raise ValidationError("Invalid Last Name, it contains comma")
    return value

NEWSLETTER_OPTION = [
    ('W', 'Weekly'),
    ('M', 'Monthly'),
]

# Create your models here.
class Subscribe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, validators=[validate_comma])
    email = models.EmailField(max_length=100)
    option = models.CharField(max_length=2, default='M', choices=NEWSLETTER_OPTION)
