from django.urls import path
from .views import analyse_nombre_api, nombres_api

urlpatterns = [
    path('analyse-nombre/', analyse_nombre_api, name='analyse-nombre-api'),
    path('nombres/', nombres_api, name='nombres-api'),
]
