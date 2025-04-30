from django import forms


class PlaceForm(forms.Form):
    name = forms.CharField(label='Название области')
    lat = forms.FloatField(widget=forms.HiddenInput())
    lng = forms.FloatField(widget=forms.HiddenInput())
