from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Class extends djangos ModelForm class
    """
    class Meta:
        model = Contact
        fields = ['reason', 'content']

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes
        """
        super().__init__(*args, **kwargs)

        if self.fields['content']:
            self.fields['content'].widget.attrs['placeholder'] = (
                'Leave your message here.')

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
