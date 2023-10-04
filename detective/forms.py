from django import forms


class CepForm(forms.Form):
    uf = forms.CharField(max_length=2)
    cidade = forms.CharField(max_length=100)
    logradouro = forms.CharField(max_length=100)
