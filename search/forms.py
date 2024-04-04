from unittest.util import _MAX_LENGTH
from django import forms


# Simpler version of SearchForm, use on pages like feed or user profile
class SimpleSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput)


# SearchForm to use on search page, with every option available
class FullSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput)
    # TODO: Add filters!!!
    # current_city = forms.ChoiceField()
