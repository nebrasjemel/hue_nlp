import Interface.models
from django import forms

__author__ = 'nebrasjemel'


class FbForm(forms.ModelForm):
    class Meta:
        model = Interface.models.FacebookAccount
        fields = ['user', 'account_id', 'access_token', 'account_name']
