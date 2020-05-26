from django import forms

from example.models import GiftList


class GiftListForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if 'curse' in name.lower():
            raise forms.ValidationError('You can not use forbidden words')

        # always return the cleaned data, whether you have changed it or not
        return name

    class Meta:
        model = GiftList
        exclude = ('modified', )
        # fields = ('name', )
        # fields = __all__
