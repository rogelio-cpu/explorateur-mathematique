from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProprietesMathematiquesSerializer, HistoriqueCalculSerializer
from .models import HistoriqueCalcul
from .math_utils import calculer_proprietes
from django.http import Http404

# Create your views here.

class ProprietesMathematiquesView(APIView):
    """
    Vue API pour calculer les propriétés mathématiques d'un nombre.
    """
    def get(self, request, format=None):
        """
        Récupère et calcule les propriétés mathématiques du nombre fourni.
        """
        # Récupérer le nombre depuis les paramètres de requête
        nombre_param = request.query_params.get('nombre', None)
        if nombre_param is None:
            return Response(
                {"erreur": "Veuillez fournir un nombre avec le paramètre 'nombre'"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Valider le nombre
        try:
            nombre = int(nombre_param)
        except ValueError:
            return Response(
                {"erreur": "Le paramètre 'nombre' doit être un entier valide"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = ProprietesMathematiquesSerializer(data={"nombre": nombre})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Calculer les propriétés
        try:
            resultats = calculer_proprietes(nombre)
            
            # Enregistrer dans l'historique (optionnel)
            HistoriqueCalcul.objects.create(
                nombre=nombre,
                est_pair=resultats["est_pair"],
                est_premier=resultats["est_premier"],
                binaire=resultats["binaire"],
                hexadecimal=resultats["hexadecimal"],
                racine_carree=resultats["racine_carree"],
                diviseurs=resultats["diviseurs"],
                est_fibonacci=resultats["est_fibonacci"],
                chiffre_romain=resultats["chiffre_romain"],
                somme_chiffres=resultats["somme_chiffres"],
                est_carre_parfait=resultats["est_carre_parfait"],
                est_cube_parfait=resultats["est_cube_parfait"],
                log_base10=resultats["log_base10"],
                puissance_de_deux=resultats["puissance_de_deux"],
                nombre_chiffres=resultats["nombre_chiffres"],
                est_abondant=resultats["est_abondant"],
                est_palindrome=resultats["est_palindrome"],
                factorisation_premiers=resultats["factorisation_premiers"]
            )
            
            return Response(resultats)
        except Exception as e:
            return Response(
                {"erreur": f"Erreur lors du calcul: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class HistoriqueCalculView(APIView):
    """
    Vue API pour gérer l'historique des calculs.
    """
    def get(self, request, format=None):
        """
        Récupère l'historique des calculs.
        """
        historique = HistoriqueCalcul.objects.all()
        serializer = HistoriqueCalculSerializer(historique, many=True)
        return Response(serializer.data)
    
    def delete(self, request, pk=None, format=None):
        """
        Supprime un élément de l'historique des calculs.
        """
        if pk:
            try:
                historique = HistoriqueCalcul.objects.get(pk=pk)
                historique.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except HistoriqueCalcul.DoesNotExist:
                raise Http404
        else:
            # Supprime tout l'historique
            HistoriqueCalcul.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
