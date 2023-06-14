from django import forms
from . models import Product,Category
class AddProduct(forms.ModelForm):
    image=forms.ImageField(label="Product Image")
    class Meta:
        model=Product
        fields="__all__"
class AddCategory(forms.ModelForm):
    
    class Meta:
        model=Category
        fields="__all__"