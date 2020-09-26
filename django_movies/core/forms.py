from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit
from datetime import date
from core.models import Genre, Movie
from django.core.exceptions import ValidationError
import re

def capitalized_validator(value: str):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class PastMonthField(forms.DateField):
    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

    title = forms.CharField(validators=[capitalized_validator])
    rating = forms.IntegerField(min_value=1, max_value=10)
    released = PastMonthField()
    # genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    # description = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            Row(Column('genre'), Column('rating'), Column('released')),
            'director',
            'description',
            'countries',
            Submit('submit', 'Submit'),
        )

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        cleaned = '. '.join(sentence.capitalize() for sentence in sentences)
        return cleaned

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'comedy' and result['rating'] > 5:
            raise ValidationError('The best comedy is worth a 4.')
        return result