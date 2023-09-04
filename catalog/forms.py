from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "is_current_version":
                field.widget.attrs['class'] = 'form-control'
            elif field_name != 'is_published':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm, StyleFormMixin):
    version = forms.ModelChoiceField(queryset=Version.objects.none(), label='Версия продукта', required=False)
    is_published = forms.BooleanField(label='Опубликовано',
                                      required=False,
                                      widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    forbidden_word = ['казино', 'криптовалюта', 'крипта',
                      'биржа', 'дешево', 'бесплатно', 'обман',
                      'полиция', 'радар'
                      ]

    class Meta:
        model = Product
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product = self.instance
        if self.product:
            self.fields['version'].queryset = Version.objects.filter(product=self.product)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_banned_words(self, data):
        for item in self.forbidden_word:
            if item in data.lower():
                raise forms.ValidationError('Ошибка! Вы используете запрещенные слова.')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        self.clean_banned_words(cleaned_data)
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        self.clean_banned_words(cleaned_data)
        return cleaned_data


class VersionForm(forms.ModelForm, StyleFormMixin):
    class Meta:
        model = Version
        fields = "__all__"
