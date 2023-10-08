from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['reason', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        reason_choices = [
            ('', '--- Select Reason for Contact ---'),
            ('products', 'Inquiries about Products'),
            ('support', 'Customer Support or Technical Assistance'),
            ('feedback', 'Feedback or Suggestions'),
            ('wholesale', 'Wholesale or Bulk Orders'),
            ('privacy', 'Privacy Concerns or Data Requests'),
            ('marketing', 'Marketing or Advertising Inquiries'),
            ('general', 'General Questions or Comments'),
        ]

        self.fields['reason'].choices = reason_choices
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
