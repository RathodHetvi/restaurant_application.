from dataclasses import field
from xml.dom import ValidationErr
from django import forms


from .models import Rslist,Cuision,Menulist

class RslistForm(forms.ModelForm):
    name       = forms.CharField(label="Restaurant name",
                    widget=forms.TextInput(attrs={"placeholder": "Retaurant name"}))
    

    content = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows":10,
                "cols":100
            }
            )
        )
    
    
    class Meta:
        model = Rslist
        fields = [
            'name',
            'content',
            'cuision',
            'type',
            
            
        ]
class MenulistForm(forms.ModelForm):
    item       = forms.CharField(label="Item name:",
                    widget=forms.TextInput(attrs={"placeholder": "Item name"}))
    

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows":10,
                "cols":100
            }
            )
        )


    class Meta:
        model = Menulist
        fields = [
            'menu',
            'item',
            'description',
            'ven',
            'cuision_type',
            'price',
            

            
        ]
class CuisionForm(forms.ModelForm):

    cuisine_type  = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Cuision name",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows":10,
                "cols":100
            }
            )
        )


    class Meta:
        model = Cuision
        fields = [
            'cuisine_type',
            

                
        ]

