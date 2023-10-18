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
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = [(
            '', '--- Select Category ---')] + friendly_names
        self.fields['sub_category'].choices = []
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
