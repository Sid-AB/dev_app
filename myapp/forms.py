from django import forms
from .models import APTEST

class OperationForm(forms.ModelForm):
    class Meta:
        model = APTEST
        fields=['num','libelle','ap','annee']