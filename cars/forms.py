from django import forms

class FormsCar(forms.Form):
    model = forms.CharField(max_length=50)
    year = forms.IntegerField()
