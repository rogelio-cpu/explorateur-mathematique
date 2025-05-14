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
    
    from .utils import filtrer_expression_non_math
    expression = filtrer_expression_non_math(expression)
    
    try:
        # Si l'expression est une fraction simple (ex: 3/4)
        if '/' in expression and all(part.strip().isdigit() for part in expression.split('/', 1)):
            valeur_calculee = expression
            analyse_fraction = analyser_nombre(expression)
            # On calcule la valeur numérique de la fraction
            num, den = expression.split('/', 1)
            try:
                resultat = float(num) / float(den)
                if resultat.is_integer():
                    valeur_num = str(int(resultat))
                else:
                    valeur_num = str(resultat).rstrip('0').rstrip('.') if '.' in str(resultat) else str(resultat)
                analyse_numerique = analyser_nombre(valeur_num)
            except Exception as e:
                valeur_num = None
                analyse_numerique = {'error': f'Erreur lors du calcul de la fraction: {str(e)}'}
            return Response({
                'niveau_1': {
                    'expression_fraction': expression,
                    'analyse': analyse_fraction
                },
                'niveau_2': {
                    'valeur_numerique': valeur_num,
                    'analyse': analyse_numerique
                }
            })
        else:
            # Correction : si l'expression est entre parenthèses, on les retire pour l'analyse et le calcul
            expr = expression
            if expr.startswith('(') and expr.endswith(')'):
                expr = expr[1:-1].strip()
            # Toujours calculer l'expression complète (sin, cos, tan, etc. inclus)
            valeur_calculee = calculer_expression(expr)
            # Correction : pour l'analyse, il faut toujours passer la valeur calculée sous forme de string
            analyse = analyser_nombre(str(valeur_calculee))
            return Response({
                'expression_originale': expression,
                'valeur_calculee': valeur_calculee,
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
