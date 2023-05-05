from django import forms
from .models import ImageModel

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ("img",)
        # fields = ("name", "url", "img")