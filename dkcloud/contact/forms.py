from django import forms


class ContactForm(forms.Form):
    """
    Contact form used by user to contact the appropriate personel
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=100)
    message = forms.CharField(max_length=1000,
        widget=forms.Textarea())