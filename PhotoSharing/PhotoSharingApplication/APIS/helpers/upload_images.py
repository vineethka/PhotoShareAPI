__author__ = 'Suslov'
from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

class ImageForm(forms.Form):
    image = forms.ImageField(
        label='Select a image',
        help_text='max. 42 megabytes'
    )