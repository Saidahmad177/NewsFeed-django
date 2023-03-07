from django import forms
from django.contrib.auth.models import User
from firstapp.models import Contact, AllUser


class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

