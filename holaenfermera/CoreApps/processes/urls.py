from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from CoreApps.processes.views import Dashboard, PatientCreateView

urlpatterns = [
    path("Dashboard", Dashboard.as_view(), name='Dashboard'),  
    path('logout/', include('django.contrib.auth.urls'), name="logout"), #agregado para login 
    path("Patient", PatientCreateView.as_view(), name='Patient'),  
]

# Añadir patrones de URL estáticos, si los tienes
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
