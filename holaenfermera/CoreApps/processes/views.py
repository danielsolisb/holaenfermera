from typing import Any
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, TemplateView, DetailView, View, FormView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

from django.db.models import Max
from collections import defaultdict
from datetime import timedelta

from CoreApps.patients.models import Patient
from CoreApps.patients.forms import PatientForm

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



class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = "patient_form.html"
    success_url = reverse_lazy('dashboard')  # Ajusta esta URL según corresponda

    def form_valid(self, form):
        # Creamos la instancia sin guardar aún para asignar created_by
        patient = form.save(commit=False)
        patient.created_by = self.request.user
        patient.save()  # Esto ejecuta el método save del modelo, asignando los admins de forma automática
        form.save_m2m()  # Guarda los campos ManyToMany, en este caso 'admins'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['user_name'] = user.username
        context['title'] = "Add Patient"
        context['subTitle'] = "Data"
        # Serializar las intersecciones para pasarlas al JavaScript
        return context

