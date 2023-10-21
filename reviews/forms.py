from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Class extends djangos ModelForm class
    """

    RATING_CHOICES = [(i, str(i)) for i in range(0, 6)]

    rating = forms.ChoiceField(choices=RATING_CHOICES)

    class Meta:
        model = Review
        exclude = ('product', 'user', 'created_at',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'content': 'Place your review here',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rating':
                placeholder = placeholders[field]
                self.fields[field].label = placeholder
                self.fields[field].widget.attrs['aria-label'] = placeholder
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black '
                                                        'rounded-0 '
                                                        'profile-form-input')
        self.fields['rating'].widget.attrs['style'] = ('width: 100px;')
        self.fields['rating'].widget.attrs['aria-label'] = 'Rating'
