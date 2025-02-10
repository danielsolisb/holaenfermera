from django import forms
from CoreApps.processes.models import Doctor, Prescription, Consent
from CoreApps.processes.models import SerumApplication
from CoreApps.patients.models import Patient
from CoreApps.store.models import Product

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Doctor'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Especialidad'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo'}),
        }

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        # Se asume que el campo "doctor" se asigna vía la URL o la vista, por lo que se excluye;
        # el campo "patient" y "prescription_date" se configuran automáticamente.
        fields = ['pdf']
        widgets = {
            'pdf': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ConsentForm(forms.ModelForm):
    class Meta:
        model = Consent
        # Se asume que "patient" y "document_date" se asignan automáticamente o mediante la URL,
        # por lo que solo se permiten editar "age" y "signature".
        fields = ['age', 'signature']
        widgets = {
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'signature': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



class SerumApplicationForm(forms.ModelForm):
    patient = forms.CharField(
        max_length=255,
        required=False,
        label="Buscar Paciente",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre, Apellido, ID...'})
    )

    product = forms.CharField(
        max_length=255,
        required=False,
        label="Buscar Producto",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Producto...'})
    )

    prescription = forms.CharField(
        max_length=255,
        required=False,
        label="Buscar Receta",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor, Fecha, Paciente...'})
    )

    consent = forms.CharField(
        max_length=255,
        required=False,
        label="Buscar Consentimiento",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Paciente, Fecha...'})
    )

    location = forms.ChoiceField(
        choices=SerumApplication.LOCATION_CHOICES,
        label="Ubicación",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = SerumApplication
        fields = ['patient', 'product', 'location', 'prescription', 'consent']