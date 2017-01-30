from django import forms

class FavoritesForm(forms.Form):
    virtualfolder = forms.CharField(widget=forms.TextInput(attrs={'id': 'page', 'class': 'form_control'}), max_length=100, required=False)
    type = forms.CharField(widget=forms.TextInput(attrs={'id': 'count', 'class': 'form_control'}), max_length=100, required=False)
    filetype = forms.CharField(widget=forms.TextInput(attrs={'id': 'type', 'class': 'form_control'}), max_length=100, required=False)

class UpdateFavoritesForm(forms.Form):
    uri = forms.CharField(widget=forms.TextInput(attrs={'id': 'page', 'class': 'form_control'}), max_length=150, required=True)
    createversion = forms.CharField(widget=forms.TextInput(attrs={'id': 'count', 'class': 'form_control'}), max_length=100, required=False)


class DeleteFavoritesForm(forms.Form):
    uri = forms.CharField(widget=forms.TextInput(attrs={'id': 'page', 'class': 'form_control'}), max_length=100, required=False)
    createversion = forms.CharField(widget=forms.TextInput(attrs={'id': 'count', 'class': 'form_control'}), max_length=100, required=False)