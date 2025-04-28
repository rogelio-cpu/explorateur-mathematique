from django.urls import path
from .views import ProprietesMathematiquesView, HistoriqueCalculView

urlpatterns = [
    # Endpoint pour calculer les propriétés mathématiques d'un nombre
    # Exemple d'utilisation: /api/proprietes-mathematiques/?nombre=42
    path('proprietes-mathematiques/', ProprietesMathematiquesView.as_view(), name='proprietes-mathematiques'),
    
    # Endpoint pour récupérer l'historique des calculs
    path('historique/', HistoriqueCalculView.as_view(), name='historique'),
    
    # Endpoint pour supprimer un élément spécifique de l'historique
    path('historique/<int:pk>/', HistoriqueCalculView.as_view(), name='historique-detail'),
] 