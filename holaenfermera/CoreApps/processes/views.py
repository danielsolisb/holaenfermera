from typing import Any
from django.urls import reverse_lazy
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
#from django.shortcuts import redirect
from django.utils.decorators import method_decorator
#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, TemplateView, DetailView, View, FormView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

from django.db.models import Max
from collections import defaultdict
from datetime import timedelta

#from CoreApps.patients.models import Patient
#from CoreApps.patients.forms import PatientForm
#from CoreApps.processes.models import Doctor, Prescription, Consent, ServiceFee, VaccineApplication, SuerotherapyApplication, SerumApplication
#from CoreApps.store.models import Product
#from CoreApps.processes.forms import DoctorForm, PrescriptionForm, ConsentForm, SerumApplicationForm

import json
from django.core.serializers import serialize

def page_not_found404(request, exception):
    return render(request, '404.html')

class Dashboard(TemplateView):
    template_name = 'Dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
          
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['user_name'] = user.username
        context['title'] = "Dashboard"
        # Serializar las intersecciones para pasarlas al JavaScript
        return context

#class PatientCreateView(CreateView):
#    model = Patient
#    form_class = PatientForm
#    template_name = "patient_form.html"
#    success_url = reverse_lazy('Dashboard')  # Ajusta esta URL según corresponda
#
#    def form_valid(self, form):
#        # Creamos la instancia sin guardar aún para asignar created_by
#        patient = form.save(commit=False)
#        patient.created_by = self.request.user
#        patient.save()  # Esto ejecuta el método save del modelo, asignando los admins de forma automática
#        form.save_m2m()  # Guarda los campos ManyToMany, en este caso 'admins'
#        return super().form_valid(form)
#
#    def get_context_data(self, **kwargs):
#        user = self.request.user
#        context = super().get_context_data(**kwargs)
#        context['user_name'] = user.username
#        context['title'] = "Agregar Paciente"
#        context['subTitle'] = "Datos"
#        # Serializar las intersecciones para pasarlas al JavaScript
#        return context
#
#
## 1. Vista para Seleccionar el Tipo de Documento
#class DocumentSelectionView(TemplateView):
#    template_name = "document_selection.html"
#
## 2. Vista para Seleccionar/Buscar Doctor
#class DoctorSelectionView(ListView):
#    model = Doctor
#    template_name = "doctor_selection.html"
#    context_object_name = "recent_doctors"
#
#    def get_queryset(self):
#        # Devuelve los 5 doctores más recientes
#        return Doctor.objects.all().order_by('-id')[:5]
#
#
## 3. Vista para búsqueda AJAX de doctores
#def doctor_search(request):
#    query = request.GET.get('q', '')
#    doctors = Doctor.objects.filter(name__icontains=query)
#    # Se asume que se dispone de un fragmento de plantilla "doctor_list_fragment.html" que muestra la tabla
#    return render(request, "doctor_list_fragment.html", {'doctors': doctors})
#
#
## 4. Vista para Crear un Doctor (o seleccionar uno nuevo)
#class DoctorCreateView(CreateView):
#    model = Doctor
#    form_class = DoctorForm
#    template_name = "doctor_form.html"
#
#    def get_success_url(self):
#        # Después de crear, redirige a la vista que marca al doctor como seleccionado;
#        # se añade el parámetro doc_type para indicar que se trata de receta
#        return reverse('doctor-selected', kwargs={'doctor_id': self.object.id}) + "?doc_type=prescription"
#
#
## 5. Vista para Confirmar la Selección de un Doctor y redirigir al formulario de receta
#
#def doctor_selected(request, doctor_id):
#    # Redirige a la vista de selección de paciente para receta,
#    # pasando el doctor_id por query parameter.
#    return redirect(f"{reverse('patient-selection-prescription')}?doctor_id={doctor_id}&doc_type=prescription")
#
## 6. Vista para Crear la Receta (con el doctor preseleccionado)
#
#class PrescriptionCreateView(CreateView):
#    model = Prescription
#    form_class = PrescriptionForm
#    template_name = "prescription_form.html"
#    success_url = reverse_lazy('document-selection')  # O la URL que prefieras
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        doctor_id = self.kwargs.get('doctor_id')
#        patient_id = self.request.GET.get('patient_id')
#        if doctor_id:
#            context['doctor'] = get_object_or_404(Doctor, pk=doctor_id)
#        if patient_id:
#            context['patient'] = get_object_or_404(Patient, pk=patient_id)
#        return context
#
#    def form_valid(self, form):
#        # Obtener el ID del doctor desde la URL
#        doctor_id = self.kwargs.get('doctor_id')
#        # Obtener el objeto Doctor correspondiente
#        doctor = get_object_or_404(Doctor, pk=doctor_id)
#        # Asignar el doctor a la instancia de la receta
#        form.instance.doctor = doctor
#
#        # Obtener el ID del paciente desde la URL
#        patient_id = self.request.GET.get('patient_id')
#        # Obtener el objeto Patient correspondiente
#        patient = get_object_or_404(Patient, pk=patient_id)
#        # Asignar el paciente a la instancia de la receta
#        form.instance.patient = patient
#
#        return super().form_valid(form)
#
#class PatientSelectionForPrescriptionView(ListView):
#    model = Patient
#    template_name = "patient_selection_prescription.html"
#    context_object_name = "recent_patients"
#    
#    def get_queryset(self):
#        # Devuelve los 5 pacientes más recientes
#        return Patient.objects.all().order_by('-id')[:5]
#    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        doctor_id = self.request.GET.get('doctor_id')
#        if doctor_id:
#            context['doctor_id'] = doctor_id
#        return context
#
#
#
#def patient_search_prescription(request):
#    query = request.GET.get('q', '')
#    patients = Patient.objects.filter(first_names__icontains=query) | \
#               Patient.objects.filter(last_names__icontains=query) | \
#               Patient.objects.filter(id_card__icontains=query)
#    return render(request, "patient_list_fragment.html", {'patients': patients})
#
#   
#
## 7. Vista para Seleccionar Paciente para Consentimiento
#class PatientSelectionConsentView(ListView):
#    model = Patient
#    template_name = "patient_selection_consent.html"
#    context_object_name = "recent_patients"
#
#    def get_queryset(self):
#        # Devuelve los 5 pacientes más recientes
#        return Patient.objects.all().order_by('-id')[:5]
#
#
## 8. Vista para búsqueda AJAX de pacientes
#def patient_search(request):
#    query = request.GET.get('q', '')
#    # Se realiza una búsqueda sencilla en nombres, apellidos o identificación
#    patients = Patient.objects.filter(first_names__icontains=query) | Patient.objects.filter(last_names__icontains=query) | Patient.objects.filter(id_card__icontains=query)
#    # Se asume que existe un fragmento de plantilla "patient_list_fragment.html"
#    return render(request, "patient_list_fragment.html", {'patients': patients})
#
#
## 9. Vista para Crear el Consentimiento (con el paciente preseleccionado)
#class ConsentCreateView(CreateView):
#    model = Consent
#    form_class = ConsentForm
#    template_name = "consent_form.html"
#    success_url = reverse_lazy('document-selection')
#
#    def get_initial(self):
#        initial = super().get_initial()
#        patient_id = self.kwargs.get('patient_id') or self.request.GET.get('patient_id')
#        if patient_id:
#            initial['patient'] = patient_id
#        return initial
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        patient_id = self.kwargs.get('patient_id') or self.request.GET.get('patient_id')
#        if patient_id:
#            context['patient'] = get_object_or_404(Patient, pk=patient_id)
#        return context
#
#    def form_valid(self, form):
#        # Si el campo patient no se asignó, intentamos obtenerlo de los parámetros (URL o query string)
#        if not form.instance.patient_id:
#            patient_id = self.kwargs.get('patient_id') or self.request.GET.get('patient_id')
#            if patient_id:
#                form.instance.patient = get_object_or_404(Patient, pk=patient_id)
#        return super().form_valid(form)
#
##SERVICIOS
#def search_patients(request):
#    query = request.GET.get('term', '')
#    patients = Patient.objects.filter(first_names__icontains=query) | Patient.objects.filter(last_names__icontains=query) | Patient.objects.filter(id_card__icontains=query)
#    results = [{'id': p.id, 'value': f'{p.first_names} {p.last_names} ({p.id_card})'} for p in patients]
#    return JsonResponse(results, safe=False)
#
#def search_products(request):
#    query = request.GET.get('term', '')
#    # Ajusta los campos de búsqueda para que coincidan con los campos reales del modelo Product
#    products = Product.objects.filter(
#        name__icontains=query) | Product.objects.filter(
#        administration_type__icontains=query) | Product.objects.filter(
#        specialty__icontains=query
#    )
#    results = [
#        {'id': p.id, 'value': f'{p.name} - {p.administration_type} - {p.specialty}'}
#        for p in products
#    ]
#    return JsonResponse(results, safe=False)
#
#def search_prescriptions(request):
#    query = request.GET.get('term', '')
#    prescriptions = Prescription.objects.filter(doctor__name__icontains=query) | Prescription.objects.filter(patient__first_names__icontains=query) | Prescription.objects.filter(patient__last_names__icontains=query)
#    results = [{'id': p.id, 'value': f'Receta de {p.patient.first_names} {p.patient.last_names} - Dr. {p.doctor.name}'} for p in prescriptions]
#    return JsonResponse(results, safe=False)
#
#def search_consents(request):
#    query = request.GET.get('term', '')
#    consents = Consent.objects.filter(patient__first_names__icontains=query) | Consent.objects.filter(patient__last_names__icontains=query)
#    results = [{'id': c.id, 'value': f'Consentimiento de {c.patient.first_names} {c.patient.last_names}'} for c in consents]
#    return JsonResponse(results, safe=False)
#
#class SerumApplicationCreateView(CreateView):
#    model = SerumApplication
#    form_class = SerumApplicationForm
#    template_name = 'serum_application_form.html'
#    success_url = reverse_lazy('Dashboard')
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['title'] = "Nueva Aplicación de Suero"
#        context['subTitle'] = "Formulario"
#        return context
#
#    def form_valid(self, form):
#        # Obtener los IDs de los objetos seleccionados desde la solicitud POST
#        patient_id = self.request.POST.get('patient_id')
#        product_id = self.request.POST.get('product_id')
#        prescription_id = self.request.POST.get('prescription_id')
#        consent_id = self.request.POST.get('consent_id')
#
#        # Asignar los objetos a la instancia del modelo, si se seleccionaron
#        if patient_id:
#            try:
#                form.instance.patient = Patient.objects.get(pk=patient_id)
#            except Patient.DoesNotExist:
#                # Manejar el caso en que el paciente no existe
#                form.add_error('patient', "Paciente inválido")
#                return self.form_invalid(form)  # Retornar el formulario con errores
#        if product_id:
#            form.instance.product = get_object_or_404(Product, pk=product_id)
#        if prescription_id:
#            form.instance.prescription = get_object_or_404(Prescription, pk=prescription_id)
#        if consent_id:
#            form.instance.consent = get_object_or_404(Consent, pk=consent_id)
#
#        return super().form_valid(form)