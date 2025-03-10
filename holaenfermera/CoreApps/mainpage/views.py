from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MainPageView(TemplateView):
    template_name = 'mainpage/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hola Enfermera - Servicios de enfermería a domicilio'
        return context
