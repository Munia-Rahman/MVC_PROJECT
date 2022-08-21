"""
from django import forms
from .models import Item

http://127.0.0.1:8000/
class AddForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('created_by',
        'title', 'image', 'description', 'price', 'pieces', 'instructions', 'labels', 'label_colour', 'slug')
        """