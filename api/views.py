from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProprietesMathematiquesSerializer, HistoriqueCalculSerializer
from .models import HistoriqueCalcul
from .math_utils import calculer_proprietes_avec_descriptions, calculer_proprietes
from django.http import Http404

class ProprietesMathematiquesView(APIView):
    """
    Vue API pour calculer les propriétés mathématiques d'un nombre.
    Version avec gestion du champ 'statut' dans la réponse.
    """
    def get(self, request, format=None):
        nombre_param = request.query_params.get('nombre', None)
        if nombre_param is None:
            return Response({
                "statut": False,
                "erreur": "Veuillez fournir un nombre avec le paramètre 'nombre'"
            }, status=status.HTTP_200_OK)

        try:
            nombre = int(nombre_param)
        except ValueError:
            return Response({
                "statut": False,
                "erreur": "Le paramètre 'nombre' doit être un entier valide"
            }, status=status.HTTP_200_OK)

        serializer = ProprietesMathematiquesSerializer(data={"nombre": nombre})
        if not serializer.is_valid():
            return Response({
                "statut": False,
                "erreur": serializer.errors
            }, status=status.HTTP_200_OK)

        try:
            # Version avec descriptions pour la réponse API
            resultats_api = calculer_proprietes_avec_descriptions(nombre)
            # Version sans descriptions pour la sauvegarde en base
            donnees_brutes = calculer_proprietes(nombre)
            HistoriqueCalcul.objects.create(
                nombre=nombre,
                chiffre_arabe=donnees_brutes["Chiffre_arabe"],
                entier_naturel=donnees_brutes["Entier_naturel"],
                entier_positif=donnees_brutes["Entier_positif"],
                entier_negatif=donnees_brutes["Entier_negatif"],
                entier_relatif=donnees_brutes["Entier_relatif"],
                nombre_decimal=donnees_brutes["Nombre_decimal"],
                rationnel=donnees_brutes["Rationnel"],
                irrationnel=donnees_brutes["Irrationnel"],
                reel=donnees_brutes["Reel"],
                imaginaire_pur=donnees_brutes["Imaginaire_pur"],
                complexe=donnees_brutes["Complexe"],
                est_pair=donnees_brutes["Est_pair"],
                est_premier=donnees_brutes["Est_premier"],
                binaire=donnees_brutes["Binaire"],
                hexadecimal=donnees_brutes["Hexadecimal"],
                racine_carree=donnees_brutes["Racine_carree"],
                diviseurs=donnees_brutes["Diviseurs"],
                est_fibonacci=donnees_brutes["Est_fibonacci"],
                chiffre_romain=donnees_brutes["Chiffre_romain"],
                somme_chiffres=donnees_brutes["Somme_chiffres"],
                est_carre_parfait=donnees_brutes["Est_carre_parfait"],
                est_cube_parfait=donnees_brutes["Est_cube_parfait"],
                log_base10=donnees_brutes["Log_base10"],
                puissance_de_deux=donnees_brutes["Puissance_de_deux"],
                nombre_chiffres=donnees_brutes["Nombre_chiffres"],
                est_abondant=donnees_brutes["Est_abondant"],
                est_palindrome=donnees_brutes["Est_palindrome"],
                factorisation_premiers=donnees_brutes["Factorisation_premiers"]
            )
            # Ajout du champ 'statut' à la réponse
            return Response({
                "statut": True,
                **resultats_api
            })
        except Exception as e:
            return Response({
                "statut": False,
                "erreur": f"Erreur lors du calcul: {str(e)}"
            }, status=status.HTTP_200_OK)

class HistoriqueCalculView(APIView):
    """
    Vue API pour gérer l'historique des calculs.
    """
    def get(self, request, format=None):
        historique = HistoriqueCalcul.objects.all()
        serializer = HistoriqueCalculSerializer(historique, many=True)
        return Response(serializer.data)
    
    def delete(self, request, pk=None, format=None):
        if pk:
            try:
                historique = HistoriqueCalcul.objects.get(pk=pk)
                historique.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except HistoriqueCalcul.DoesNotExist:
                raise Http404
        else:
            HistoriqueCalcul.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
