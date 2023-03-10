from django import forms
from django.contrib.auth.models import User
from firstapp.models import Contact, AllUser, Comments


class FormContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
