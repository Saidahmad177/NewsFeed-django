from django import forms
from firstapp.models import Contact


class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
