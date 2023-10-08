from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        exclude = ('user', 'email', 'created_at',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'content': 'Leave your message here.',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields['reason'].choices = [(
                '', '--- Select Reason for Contact ---'),
                ('products', 'Inquiries about Products'),
                ('support', 'Customer Support or Technical Assistance'),
                ('feedback', 'Feedback or Suggestions'),
                ('wholesale', 'Wholesale or Bulk Orders'),
                ('privacy', 'Privacy Concerns or Data Requests'),
                ('marketing', 'Marketing or Advertising Inquiries'),
                ('general', 'General Questions or Comments'),
            ]
            self.fields['reason'].widget.choices[0]['disabled'] = True
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
            self.fields[field].label = False
