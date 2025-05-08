from rest_framework import serializers
from .models import Nombre

class NombreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nombre
        fields = ['id', 'valeur', 'ensemble', 'date_ajout']

class NumberAnalysisSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=100)
    is_valid = serializers.BooleanField(read_only=True)
    analysis_results = serializers.JSONField(read_only=True)
    
    def validate_number(self, value):
        """Validation basique du nombre"""
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Le nombre ne peut pas être vide")
        return value