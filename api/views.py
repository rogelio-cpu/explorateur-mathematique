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
    print('Hello world')
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
                chiffre_arabe=donnees_brutes["chiffre_arabe"],
                entier_naturel=donnees_brutes["entier_naturel"],
                entier_positif=donnees_brutes["entier_positif"],
                entier_negatif=donnees_brutes["entier_negatif"],
                entier_relatif=donnees_brutes["entier_relatif"],
                nombre_decimal=donnees_brutes["nombre_decimal"],
                rationnel=donnees_brutes["rationnel"],
                irrationnel=donnees_brutes["irrationnel"],
                reel=donnees_brutes["reel"],
                imaginaire_pur=donnees_brutes["imaginaire_pur"],
                complexe=donnees_brutes["complexe"],
                est_pair=donnees_brutes["est_pair"],
                est_premier=donnees_brutes["est_premier"],
                binaire=donnees_brutes["binaire"],
                hexadecimal=donnees_brutes["hexadecimal"],
                racine_carree=donnees_brutes["racine_carree"],
                diviseurs=donnees_brutes["diviseurs"],
                est_fibonacci=donnees_brutes["est_fibonacci"],
                chiffre_romain=donnees_brutes["chiffre_romain"],
                somme_chiffres=donnees_brutes["somme_chiffres"],
                est_carre_parfait=donnees_brutes["est_carre_parfait"],
                est_cube_parfait=donnees_brutes["est_cube_parfait"],
                log_base10=donnees_brutes["log_base10"],
                puissance_de_deux=donnees_brutes["puissance_de_deux"],
                nombre_chiffres=donnees_brutes["nombre_chiffres"],
                est_abondant=donnees_brutes["est_abondant"],
                est_palindrome=donnees_brutes["est_palindrome"],
                factorisation_premiers=donnees_brutes["factorisation_premiers"]
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
