from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_names',
            'last_names',
            'id_card',
            'birth_date',
            'address',
            'phone',
            'email'
        ]
