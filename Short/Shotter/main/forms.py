from django import forms
from .models import CollectUrl


class GoodUrl(forms.ModelForm):
    class Meta:
        model = CollectUrl
        fields = ('url',)