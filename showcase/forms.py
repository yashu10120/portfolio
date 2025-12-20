from django import forms
from .models import Contact   # assuming you already created a Contact model

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]
