from django.urls import path
from .views import MainPageView

app_name = 'mainpage'

urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
]