from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
#from CoreApps.processes.views import Dashboard, PatientCreateView, DocumentSelectionView, DoctorSelectionView, DoctorCreateView, PrescriptionCreateView, PatientSelectionConsentView, ConsentCreateView

from .views import (
    Dashboard,
    #PatientCreateView,
    #DocumentSelectionView,
    #DoctorSelectionView,
    #doctor_search,
    #DoctorCreateView,
    #doctor_selected,
    #PrescriptionCreateView,
    #PatientSelectionConsentView,
    #patient_search,
    #ConsentCreateView,
    #PatientSelectionForPrescriptionView,
    #patient_search_prescription,
    #SerumApplicationCreateView,
    #search_patients, 
    #search_products, 
    #search_prescriptions, 
    #search_consents,
)

urlpatterns = [
    path("Dashboard", Dashboard.as_view(), name='Dashboard'),  
    path('logout/', include('django.contrib.auth.urls'), name="logout"), #agregado para login 
    #path("Patient", PatientCreateView.as_view(), name='Patient'),  

    # Vista de selección de documento (receta o consentimiento)
    #path('document-selection/', DocumentSelectionView.as_view(), name='document-selection'),
    
    # Flujo para Receta
    #path('doctor-selection/', DoctorSelectionView.as_view(), name='doctor-selection'),
    #path('doctor-search/', doctor_search, name='doctor-search'),
    #path('doctor-create/', DoctorCreateView.as_view(), name='doctor-create'),
    #path('doctor-selected/<int:doctor_id>/', doctor_selected, name='doctor-selected'),
    #path('prescription-create/<int:doctor_id>/', PrescriptionCreateView.as_view(), name='prescription-create'),
    
     # Nueva ruta para seleccionar paciente para receta:
    #path('patient-selection-prescription/', PatientSelectionForPrescriptionView.as_view(), name='patient-selection-prescription'),
    #path('patient-search-prescription/', patient_search_prescription, name='patient-search-prescription'),
    # Vista para crear la receta: requiere doctor_id en la URL y patient_id como query parameter
    #path('prescription-create/<int:doctor_id>/', PrescriptionCreateView.as_view(), name='prescription-create'),
    

    # Flujo para Consentimiento
    #path('patient-selection-consent/', PatientSelectionConsentView.as_view(), name='patient-selection-consent'),
    #path('patient-search/', patient_search, name='patient-search'),
    #path('consent-create/<int:patient_id>/', ConsentCreateView.as_view(), name='consent-create'),
    
    #Servicios
    #path('serum-application/create/', SerumApplicationCreateView.as_view(), name='serum-application-create'),
    #path('search/patients/', search_patients, name='search-patients'),
    #path('search/products/', search_products, name='search-products'),
    #path('search/prescriptions/', search_prescriptions, name='search-prescriptions'),
    #path('search/consents/', search_consents, name='search-consents'),
    
]

# Añadir patrones de URL estáticos, si los tienes
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
