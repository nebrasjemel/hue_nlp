import models
from django import forms

__author__ = 'nebrasjemel'


class HueForm(forms.ModelForm):
    class Meta:
        model = models.PhilipsHue
        fields = ['user', 'username', 'ip_address', 'related_account']

class FbForm(forms.ModelForm):
    class Meta:
        model = models.FacebookAccount
        fields = ['user', 'account_id', 'access_token', 'account_name']
