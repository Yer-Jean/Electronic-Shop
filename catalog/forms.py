from django import forms
from django.shortcuts import render

from catalog.models import Product, Version
from config.settings import WORDS_BLACK_LIST
from utils.utils import text_to_set_without_punctuation


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('created_by',)

    def clean(self):
        cleaned_data = super().clean()
        for field in ['name', 'description']:
            cleaned_field_data = cleaned_data.get(field)
            text = text_to_set_without_punctuation(cleaned_field_data)
            if text:
                common_words: set = text & WORDS_BLACK_LIST
            else:
                break
            if len(common_words) > 0:
                raise forms.ValidationError(f'Incorrect words used: {", ".join(common_words)}')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_active(self):
        is_active = self.cleaned_data['is_active']
        product = self.cleaned_data['product']
        # product = self.instance.product  # Получаем связанный продукт
        if is_active:
            # Проверяем, есть ли другие активные версии этого продукта
            active_versions_count = Version.objects.filter(product=product, is_active=True).exclude(
                id=self.instance.id).count()
            if active_versions_count > 0:
                raise forms.ValidationError('Уже есть активная версия этого продукта.')
        return is_active
