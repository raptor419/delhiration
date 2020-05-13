# -*- encoding: utf-8 -*-



from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

class RationCardInput(forms.Form):
    rationcard_rx = forms.CharField(
        required=True, validators=[RegexValidator(r'^[0][0-9]{11}')],
        widget=forms.TextInput(
            attrs={
                "placeholder" : "",                
                "class": "form-control form-control-lg",
            }
        ))


class FPSForm(forms.Form):
    class Meta:
        model = FPS
        fields = ('name', 'price', 'category', )

    def __init__(self, user, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)



