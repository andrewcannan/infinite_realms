from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Sub_category


class ProductForm(forms.ModelForm):
    """
    Class extends djangos ModelForm class
    """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=True,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Set choices for select dropdowns and classes
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'category': 'Category *',
            'sub_category': 'Sub-Category *',
            'sku': 'Sku',
            'name': 'Name',
            'description': 'Description',
            'manufacturer': 'Manufacturer',
            'price': 'Price',
            'image': 'Image',
        }
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = [(
            '', '--- Select Category ---')] + friendly_names
        self.fields['sub_category'].choices = []

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            if field not in ['category', 'sub_category', 'image']:
                self.fields[field].label = False
                self.fields[field].widget.attrs[
                    'placeholder'] = placeholder + '*'
            if field in ['category', 'sub_category']:
                self.fields[field].label = placeholder
            if field != 'image':
                self.fields[field].widget.attrs['aria-label'] = placeholder
