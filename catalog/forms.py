from django import forms

from catalog.models import Product
from config.settings import WORDS_BLACK_LIST
from utils.utils import text_to_set_without_punctuation


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super().clean()
        for field in ['name', 'description']:
            cleaned_field_data = cleaned_data.get(field)
            common_words: set = text_to_set_without_punctuation(cleaned_field_data) & WORDS_BLACK_LIST
            if len(common_words) > 0:
                raise forms.ValidationError(f'Использованы некорректные слова: {", ".join(common_words)}')
        return cleaned_data
