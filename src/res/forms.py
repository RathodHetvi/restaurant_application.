import imp
from django import forms

from .models import Rslist
from .models import Menulist


class RslistModelForm(forms.ModelForm):
    class Meta:
        model = Rslist
        fields =[
            'name',
            'content',
            
        ]
class MenulistModelForm(forms.ModelForm):
    class Meta:
        model = Menulist
        fields =[
            'item',
            'price',
            'menu',
            
        ]