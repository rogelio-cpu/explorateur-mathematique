import math
import re

def est_chiffre_arabe(nombre):
    """Vérifie si le nombre est un seul chiffre arabe (0-9)."""
    try:
        return len(str(nombre)) == 1 and str(nombre) in '0123456789'
    except:
        return False

def est_nombre_arabe(nombre):
    """Vérifie si le nombre est un nombre arabe valide (≥2 chiffres, ne commence pas par 0)."""
    try:
        nombre_str = str(nombre)
        return len(nombre_str) >= 2 and nombre_str.isdigit() and nombre_str[0] != '0'
    except:
        return False

def est_entier_naturel(nombre):
    """Vérifie si le nombre est un entier naturel (0 ou nombre arabe valide)."""
    try:
        nombre_str = str(nombre)
        # Un chiffre arabe (0-9) est aussi un entier naturel
        if est_chiffre_arabe(nombre_str):
            return True
        return nombre_str == '0' or est_nombre_arabe(nombre_str)
    except:
        return False

def est_entier_naturel_negatif(nombre):
    """Vérifie si le nombre est un entier naturel négatif (-n où n est un nombre arabe valide)."""
    try:
        nombre_str = str(nombre)
        if not nombre_str.startswith('-'):
            return False
        # La partie après le - doit être un entier naturel
        return est_entier_naturel(nombre_str[1:])
    except:
        return False

def est_entier_relatif(nombre):
    """Vérifie si le nombre est un entier relatif (positif, nul ou négatif)."""
    try:
        nombre_str = str(nombre)
        return est_entier_naturel(nombre_str) or est_entier_naturel_negatif(nombre_str)
    except:
        return False

def est_decimal_fini(nombre):
    """Vérifie si le nombre est un décimal fini valide."""
    try:
        nombre_str = str(nombre)
        parts = nombre_str.split('.')
        if len(parts) != 2:
            return False
        
        partie_entiere, partie_decimale = parts
        
        # Vérifier la partie entière
        if partie_entiere.startswith('-'):
            valide_entiere = partie_entiere == '-' or est_entier_naturel(partie_entiere[1:])
        else:
            valide_entiere = est_entier_naturel(partie_entiere) or partie_entiere == ''
        
        # Vérifier la partie décimale
        valide_decimale = partie_decimale.isdigit() and len(partie_decimale) > 0
        
        return valide_entiere and valide_decimale
    except:
        return False

def est_fraction_rationnelle(nombre):
    """Vérifie si le nombre est une fraction rationnelle (p/q avec q non puissance de 10)."""
    try:
        nombre_str = str(nombre)
        if '/' not in nombre_str:
            return False
        
        numerateur, denominateur = nombre_str.split('/')
        
        # Vérifier que le dénominateur n'est pas une puissance de 10
        if denominateur.isdigit():
            d = int(denominateur)
            if d == 0:
                return False
            while d % 10 == 0:
                d = d // 10
            return d == 1
        return False
    except:
        return False

def est_nombre_rationnel(nombre):
    """Vérifie si le nombre peut s'écrire comme une fraction d'entiers."""
    try:
        float(nombre)
        return True
    except ValueError:
        try:
            nombre_str = str(nombre)
            if '/' in nombre_str:
                numerateur, denominateur = nombre_str.split('/')
                return est_entier_naturel(numerateur) or est_entier_naturel_negatif(numerateur) and est_entier_naturel(denominateur)
            return False
        except:
            return False

def est_irrationnel_connu(nombre):
    """Vérifie si le nombre est un irrationnel célèbre."""
    irrationnels_connus = ['pi', 'e', 'sqrt(2)', 'sqrt(3)', 'sqrt(5)', 'phi']
    return nombre.lower() in irrationnels_connus

def est_reel(nombre):
    """Vérifie si le nombre est un réel valide."""
    try:
        float(nombre)
        return True
    except ValueError:
        return est_irrationnel_connu(nombre)

def est_imaginaire_pur(nombre):
    """Vérifie si le nombre est un imaginaire pur (bi)."""
    return nombre.endswith('i') and est_reel(nombre[:-1])

def est_complexe(nombre):
    """Vérifie si le nombre est un complexe valide (a+bi)."""
    if '+' in nombre:
        parties = nombre.split('+')
        if len(parties) == 2:
            a, bi = parties
            return est_reel(a) and est_imaginaire_pur(bi)
    return est_reel(nombre) or est_imaginaire_pur(nombre)

def get_ensemble_definitions():
    """Retourne les définitions pédagogiques de chaque ensemble"""
    return {
        'chiffre_arabe': {
            'definition': "A = {'0', ..., '9'}",
            'description': "Un seul caractère représentant un chiffre arabe de 0 à 9"
        },
        'nombre_arabe': {
            'definition': "B = {n ∈ chaînes | len(n) ≥ 2, ∀c ∈ n : c ∈ A, n[0] ≠ '0'}",
            'description': "Nombre composé de chiffres sans commencer par zéro (≥ 2 chiffres)"
        },
        'entier_naturel': {
            'definition': "ℕ = {0} ∪ B",
            'description': "0 ou un nombre arabe valide (entier positif)"
        },
        'entier_naturel_negatif': {
            'definition': "ℕ⁻ = {-n | n ∈ B}",
            'description': "Entier négatif dont la valeur absolue est un nombre arabe valide"
        },
        'entier_relatif': {
            'definition': "ℤ = ℕ ∪ ℕ⁻",
            'description': "Entier positif, nul ou négatif"
        },
        'decimal_fini': {
            'definition': "𝔻 = {p.a₁a₂...aₙ | p ∈ ℤ, aᵢ ∈ A, n ≥ 1}",
            'description': "Nombre avec partie décimale finie non nulle"
        },
        'fraction_rationnelle': {
            'definition': "F = {p/q | p ∈ ℤ, q ∈ ℕ*, q ≠ 10ⁿ}",
            'description': "Fraction dont le dénominateur n'est pas une puissance de 10"
        },
        'nombre_rationnel': {
            'definition': "ℚ = {p/q | p ∈ ℤ, q ∈ ℕ*}",
            'description': "Nombre pouvant s'exprimer comme fraction d'entiers"
        },
        'irrationnel_connu': {
            'definition': "irℚ = {π, e, √2, ...}",
            'description': "Nombre irrationnel célèbre ne pouvant s'exprimer comme fraction exacte"
        },
        'reel': {
            'definition': "ℝ = ℚ ∪ irℚ",
            'description': "Tous les nombres rationnels et irrationnels"
        },
        'imaginaire_pur': {
            'definition': "iℝ = {bi | b ∈ ℝ, i² = -1}",
            'description': "Nombre complexe sans partie réelle"
        },
        'complexe': {
            'definition': "ℂ = {a + bi | a,b ∈ ℝ}",
            'description': "Nombre avec partie réelle et imaginaire"
        }
    }

def nettoyer_expression(expression):
    """Nettoie une expression mathématique en gérant les espaces"""
    # Remplacer les caractères spéciaux de l'URL
    expression = expression.replace('%2B', '+')  # Plus
    expression = expression.replace('%2D', '-')  # Moins
    expression = expression.replace('%2A', '*')  # Multiplication
    expression = expression.replace('%2F', '/')  # Division
    
    # Supprimer tous les espaces
    expression = expression.replace(' ', '')
    
    # Ajouter des espaces autour des opérateurs explicites
    for op in ['+', '-', '*', '/']:
        expression = expression.replace(op, f' {op} ')
    
    # Gérer la multiplication implicite (ex: 2x, sin(x)cos(x))
    # Ajouter * entre un nombre et une fonction ou entre deux fonctions
    expression = re.sub(r'(\d)([a-z])', r'\1 * \2', expression)  # 2x -> 2 * x
    expression = re.sub(r'\)([a-z])', r') * \1', expression)      # sin(x)cos(x) -> sin(x) * cos(x)
    
    # Nettoyer les espaces multiples
    expression = ' '.join(expression.split())
    return expression

def detecter_expression(expression):
    """Détecte le type d'expression mathématique"""
    expression = expression.lower().strip()
    expression = nettoyer_expression(expression)
    
    # Vérifier d'abord les opérations de priorité basse (+, -)
    for op in ['+', '-']:
        if f' {op} ' in expression:
            parts = expression.split(f' {op} ')
            if len(parts) == 2:
                return {
                    'type': 'operation',
                    'operateur': op,
                    'operande1': parts[0].strip(),
                    'operande2': parts[1].strip()
                }
    
    # Puis les opérations de priorité haute (*, /)
    for op in ['*', '/']:
        if f' {op} ' in expression:
            parts = expression.split(f' {op} ')
            if len(parts) == 2:
                return {
                    'type': 'operation',
                    'operateur': op,
                    'operande1': parts[0].strip(),
                    'operande2': parts[1].strip()
                }
    
    # Constantes
    if expression in ['pi', 'e']:
        return {'type': 'constante', 'valeur': expression}
    
    # Fonctions trigonométriques
    trig_pattern = r'^(sin|cos|tan)\(([^)]+)\)$'
    trig_match = re.match(trig_pattern, expression)
    if trig_match:
        return {
            'type': 'trig',
            'fonction': trig_match.group(1),
            'argument': trig_match.group(2)
        }
    
    # Racine carrée
    sqrt_pattern = r'^sqrt\(([^)]+)\)$'
    sqrt_match = re.match(sqrt_pattern, expression)
    if sqrt_match:
        return {
            'type': 'sqrt',
            'argument': sqrt_match.group(1)
        }
    
    # Logarithmes
    log_pattern = r'^log(?:b)?\(([^;]+);([^)]+)\)$'
    log_match = re.match(log_pattern, expression)
    if log_match:
        return {
            'type': 'log',
            'base': log_match.group(1),
            'argument': log_match.group(2)
        }
    
    # Puissance
    power_pattern = r'^(.+)\^(.+)$'
    power_match = re.match(power_pattern, expression)
    if power_match:
        return {
            'type': 'power',
            'base': power_match.group(1),
            'exposant': power_match.group(2)
        }
    
    # Fraction
    fraction_pattern = r'^(.+)/(.+)$'
    fraction_match = re.match(fraction_pattern, expression)
    if fraction_match:
        return {
            'type': 'fraction',
            'numerateur': fraction_match.group(1),
            'denominateur': fraction_match.group(2)
        }
    
    return {'type': 'nombre', 'valeur': expression}

def nettoyer_resultat(nombre):
    """Nettoie un nombre en enlevant la partie décimale si elle est nulle"""
    try:
        # Convertir en float puis en string
        nombre_float = float(nombre)
        # Si c'est un entier (partie décimale = 0)
        if nombre_float.is_integer():
            return str(int(nombre_float))
        return str(nombre_float)
    except:
        return str(nombre)

def calculer_expression(expression):
    """Calcule la valeur d'une expression mathématique"""
    try:
        expr_info = detecter_expression(expression)
        
        if expr_info['type'] == 'operation':
            op1 = float(calculer_expression(expr_info['operande1']))
            op2 = float(calculer_expression(expr_info['operande2']))
            
            if expr_info['operateur'] == '+':
                return nettoyer_resultat(op1 + op2)
            elif expr_info['operateur'] == '-':
                return nettoyer_resultat(op1 - op2)
            elif expr_info['operateur'] == '*':
                return nettoyer_resultat(op1 * op2)
            elif expr_info['operateur'] == '/':
                if op2 == 0:
                    raise ValueError("Division par zéro")
                return nettoyer_resultat(op1 / op2)
        
        elif expr_info['type'] == 'constante':
            if expr_info['valeur'] == 'pi':
                return nettoyer_resultat(math.pi)
            elif expr_info['valeur'] == 'e':
                return nettoyer_resultat(math.e)
        
        elif expr_info['type'] == 'trig':
            angle = float(calculer_expression(expr_info['argument']))
            if expr_info['fonction'] == 'sin':
                return nettoyer_resultat(math.sin(math.radians(angle)))
            elif expr_info['fonction'] == 'cos':
                return nettoyer_resultat(math.cos(math.radians(angle)))
            elif expr_info['fonction'] == 'tan':
                return nettoyer_resultat(math.tan(math.radians(angle)))
        
        elif expr_info['type'] == 'sqrt':
            return nettoyer_resultat(math.sqrt(float(calculer_expression(expr_info['argument']))))
        
        elif expr_info['type'] == 'log':
            if 'base' in expr_info:
                # logb(base;x)
                base = float(calculer_expression(expr_info['base']))
                x = float(calculer_expression(expr_info['argument']))
                return nettoyer_resultat(math.log(x, base))
            else:
                # ln(x)
                return nettoyer_resultat(math.log(float(calculer_expression(expr_info['argument']))))
        
        elif expr_info['type'] == 'power':
            base = float(calculer_expression(expr_info['base']))
            exp = float(calculer_expression(expr_info['exposant']))
            return nettoyer_resultat(math.pow(base, exp))
        
        elif expr_info['type'] == 'fraction':
            num = float(calculer_expression(expr_info['numerateur']))
            den = float(calculer_expression(expr_info['denominateur']))
            return nettoyer_resultat(num / den)
        
        # Si c'est un nombre simple, le nettoyer aussi
        return nettoyer_resultat(expression)
    except Exception as e:
        raise ValueError(f"Erreur dans le calcul de l'expression: {str(e)}") 