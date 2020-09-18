from django import forms

class AddExampleForm(forms.Form):
    text = forms.CharField(max_length=2048)
    source = forms.URLField()
