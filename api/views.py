from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import activate
from datetime import datetime

from .models import Nombre
from .serializers import NombreSerializer
from .math_engine import analyser_nombre
from .utils import calculer_expression
from translations import API_MESSAGES, get_descriptions


# =========================
#   Helpers
# =========================

def get_language_and_explanations(request):
    """Retourne la langue et le dictionnaire d'explications associé."""
    lang = request.query_params.get("lang", "fr").lower()
    if lang not in ["fr", "en"]:
        lang = "fr"
    activate(lang)
    
    explanations = get_descriptions(lang)  # <-- ici on récupère le bon dictionnaire
    return lang, explanations


def format_analysis(expression, analyse, explanations):
    """Construit un dictionnaire d'analyse traduit."""
    translated = {}
    fallback = get_descriptions('en')
    for set_name, set_data in analyse.items():
        try:
            desc = explanations.get(set_name, fallback.get(set_name, {}))
            translated_value = {
                "name": desc.get("nom", set_name),
                "belongs": set_data.get("appartient", False),
                "definition": desc.get("definition", ""),
                "description": desc.get("description", ""),
                "example": desc.get("exemple", desc.get("example", "")),
            }

            if set_data.get("appartient"):
                translated_value["explanation"] = desc.get("true", "{nombre} ∈ set").format(nombre=expression)
            else:
                translated_value["explanation"] = desc.get("false", "{nombre} ∉ set").format(nombre=expression)


            translated[set_name] = translated_value

        except Exception:
            continue  # On saute les ensembles mal définis
    return translated


# =========================
#   API Views
# =========================

@api_view(["GET"])
def analyse_nombre_api(request):
    """
    Analyse d'une expression mathématique.
    Params:
        - nombre: expression à analyser
        - lang: langue (fr/en, par défaut: fr)
    """
    language, descriptions = get_language_and_explanations(request)
    messages = API_MESSAGES
    expression = request.query_params.get("nombre", "").strip()

    if not expression:
        return Response(
            {
                "error": messages['error_messages']['number_required'],
                "language": language,
                "timestamp": datetime.now().isoformat(),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        # Calcul de la valeur
        valeur_calculee = calculer_expression(expression)

        # Analyse de l'appartenance aux ensembles à partir de l'expression d'origine
        analyse = analyser_nombre(expression, language)

        # Traduction + formatage
        translated_analysis = format_analysis(expression, analyse, descriptions)

        return Response(
            {
                "language": language,
                "original_expression": expression,
                "calculated_value": str(valeur_calculee),
                "analysis": translated_analysis,
                "timestamp": datetime.now().isoformat(),
            }
        )

    except Exception as e:
        return Response(
            {
                "error": messages['error_messages']['calculation_error'],
                "language": language,
                "expression": expression,
                "timestamp": datetime.now().isoformat(),
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET", "POST"])
def nombres_api(request):
    """
    Gestion des nombres stockés.
    GET: liste les nombres
    POST: ajoute un nombre
    """
    language, descriptions = get_language_and_explanations(request)
    messages = API_MESSAGES

    if request.method == "GET":
        nombres = Nombre.objects.all().order_by("-date_ajout")
        serializer = NombreSerializer(nombres, many=True)
        return Response(
            {
                "language": language,
                "count": len(serializer.data),
                "results": serializer.data,
                "timestamp": datetime.now().isoformat(),
            }
        )

    elif request.method == "POST":
        serializer = NombreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "language": language,
                    "message": "Nombre ajouté avec succès",
                    "data": serializer.data,
                    "timestamp": datetime.now().isoformat(),
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {
                "language": language,
                "error": "Erreur de validation",
                "details": serializer.errors,
                "timestamp": datetime.now().isoformat(),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
