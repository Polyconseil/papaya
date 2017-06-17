# -*- coding: utf-8 -*-

from django import forms
from papaya.conf import settings
from django.utils.translation import ugettext as _

REALM_CHOICES = settings.PAPAYA_CONSUMER_REALMS


class LoginBasicForm(forms.Form):
    openid_identifier = forms.URLField(widget=forms.TextInput(attrs={'size': 40}))


class LoginSelectForm(forms.Form):
    username = forms.CharField(label=_('Username'))
    password = forms.ChoiceField(choices=REALM_CHOICES, label=_('Company'))

    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data['openid_identifier'] = cleaned_data['password'] + cleaned_data['username']
        return cleaned_data


if REALM_CHOICES:
    LoginForm = LoginSelectForm
else:
    LoginForm = LoginBasicForm
