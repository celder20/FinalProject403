from django import forms
from .models import footballlingo

class FootballLingoForm(forms.ModelForm) :
    class Meta :
        model = footballlingo
        fields = '__all__'