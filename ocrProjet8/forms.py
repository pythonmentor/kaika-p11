"""Forms for ocrProjet8"""
from django import forms


class ContactForm(forms.Form):
    """Form for contact view"""

    subject = forms.CharField(label="Sujet", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=100)
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={"cols": 0}))
