from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Sub_category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        sub_categories = Sub_category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        sub_friendly_names = [(
            sub_c.id, sub_c.get_friendly_name()) for sub_c in sub_categories]

        self.fields['category'].choices = friendly_names
        self.fields['sub_category'].choices = []
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
