from django import forms

class ContactsForm(forms.Form):
    page = forms.CharField(widget=forms.TextInput(attrs={'id': 'page', 'class': 'form_control'}), max_length=100, required=False)
    count = forms.CharField(widget=forms.TextInput(attrs={'id': 'count', 'class': 'form_control'}), max_length=100, required=False)
    sort = forms.CharField(widget=forms.TextInput(attrs={'id': 'type', 'class': 'form_control'}), max_length=100, required=False)

