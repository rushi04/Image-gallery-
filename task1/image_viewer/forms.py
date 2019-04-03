
from django import forms


from .models import Album_Details , Images

class ImageForm(forms.Form):
    image = forms.ImageField()
