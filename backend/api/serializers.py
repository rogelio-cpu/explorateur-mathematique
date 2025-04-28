from rest_framework import serializers
from .models import HistoriqueCalcul

class HistoriqueCalculSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle HistoriqueCalcul.
    Permet de convertir les instances du modèle en format JSON et vice-versa.
    """
    class Meta:
        model = HistoriqueCalcul
        fields = '__all__'
        
class ProprietesMathematiquesSerializer(serializers.Serializer):
    """
    Sérialiseur pour les propriétés mathématiques d'un nombre.
    Valide les entrées utilisateur et formate les résultats.
    """
    nombre = serializers.IntegerField(min_value=1, max_value=1000000)
    
    def validate_nombre(self, value):
        """
        Valide que le nombre est dans une plage raisonnable pour éviter
        des calculs trop longs ou des dépassements de mémoire.
        """
        if value <= 0:
            raise serializers.ValidationError("Le nombre doit être positif.")
        if value > 1000000:
            raise serializers.ValidationError("Le nombre est trop grand. Maximum autorisé: 1 000 000.")
        return value 