from django import forms
from .models import Category, Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'name']
