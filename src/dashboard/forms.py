from django import forms

from .models import SearchModel


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = [
            'search_query',
            'sort_by',
            'max_price',
            'min_price',
            'is_auction',
            'is_buy_now'
        ]
        widgets = {
            "is_auction": forms.CheckboxInput(),
            "is_buy_now": forms.CheckboxInput()
        }
