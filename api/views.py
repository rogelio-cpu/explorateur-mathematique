from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .math_engine import analyser_nombre
from .models import Nombre
from .serializers import NombreSerializer
from .utils import calculer_expression

@api_view(['GET'])
def analyse_nombre_api(request):
    """
    API d'analyse mathématique des nombres
    Exemple: /api/analyse-nombre/?nombre=3.14
    Exemple avec symboles: /api/analyse-nombre/?nombre=sin(45)
    Retourne une analyse détaillée du nombre selon différents ensembles mathématiques
    """
    expression = request.query_params.get('nombre', '').strip()
    
    if not expression:
        return Response(
            {'error': 'Paramètre "nombre" requis'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        # Calculer la valeur si c'est une expression
        nombre = calculer_expression(expression)
        
        # Analyser le résultat
        analyse = analyser_nombre(nombre)
        
        return Response({
            'expression_originale': expression,
            'valeur_calculee': nombre,
            'analyse': analyse
        })
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET', 'POST'])
def nombres_api(request):
    """
    GET: Liste tous les nombres stockés en base
    POST: Ajoute un nombre à la base avec son type d'ensemble
    """
    if request.method == 'GET':
        nombres = Nombre.objects.all().order_by('-date_ajout')
        serializer = NombreSerializer(nombres, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NombreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)