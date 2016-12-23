from django import forms

class PlaylistForm(forms.Form):
    type = forms.CharField(widget=forms.TextInput(attrs={'id': 'type', 'class': 'form_control'}), max_length=100, required=False)
    page = forms.CharField(widget=forms.TextInput(attrs={'id': 'page', 'class': 'form_control'}), max_length=100, required=False)
    count = forms.CharField(widget=forms.TextInput(attrs={'id': 'count', 'class': 'form_control'}), max_length=100, required=False)
    sort = forms.CharField(widget=forms.TextInput(attrs={'id': 'type', 'class': 'form_control'}), max_length=100, required=False)

class CreateplaylistForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'count', 'class': 'form_control'}), max_length=100, required=False)
    paths = forms.CharField(widget=forms.TextInput(attrs={'id': 'type', 'class': 'form_control'}), max_length=100, required=False)
    type = forms.CharField(widget=forms.TextInput(attrs={'id': 'type', 'class': 'form_control'}), max_length=100, required=False)

class UpdateplaylistForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'count', 'class': 'form_control'}), max_length=100, required=False)
    type = forms.CharField(widget=forms.TextInput(attrs={'id': 'type', 'class': 'form_control'}), max_length=100, required=False)

class UpdateplaylistdefForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'count', 'class': 'form_control'}), max_length=100, required=False)
    paths = forms.CharField(widget=forms.TextInput(attrs={'id': 'type', 'class': 'form_control'}), max_length=100, required=False)
    type = forms.CharField(widget=forms.TextInput(attrs={'id': 'type', 'class': 'form_control'}), max_length=100, required=False)
