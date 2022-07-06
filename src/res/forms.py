from dataclasses import field
from xml.dom import ValidationErr
from django import forms


from .models import Rslist



class RslistForm(forms.ModelForm):
    name       = forms.CharField(label="",
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
            
        ]
