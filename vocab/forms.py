from django import forms

class AddExampleForm(forms.Form):
    text = forms.CharField(max_length=2048, min_length=1)
    source = forms.URLField()
