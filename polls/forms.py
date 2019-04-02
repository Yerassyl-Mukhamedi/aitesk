from django import forms

class CallForm(forms.Form):
    name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    name1 = forms.CharField(required=False, max_length=100, widget=forms.HiddenInput(attrs={'placeholder': 'Ваше имя'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}))
    message = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    
