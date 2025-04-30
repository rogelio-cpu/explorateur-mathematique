import math
from fractions import Fraction
from .descriptions import DESCRIPTIONS

def calculer_proprietes_avec_descriptions(nombre):
    
    # Calcul des propriétés de base
    proprietes_calculees = calculer_proprietes(nombre)
    
    # Structure de résultat réorganisée
    resultat = {
        "nombre": nombre,
        "proprietes": []
    }
    
    # Construction de la réponse avec descriptions intégrées
    for prop, valeur in proprietes_calculees.items():
        if prop == "_explications":
            continue
            
        description = DESCRIPTIONS.get(prop, {
            "description": "Description non disponible",
            "methode": "",
            "exemple": ""
        })
        
        resultat["proprietes"].append({
            "nom": prop.replace("_", " "),
            "valeur": valeur,
            "description": description["description"],
            "methode_calcul": description.get("methode", ""),
            "exemple": description.get("exemple", "")
        })
    
    return resultat

def calculer_proprietes(nombre):
    """Version originale inchangée pour compatibilité"""
    result = {
        # Ensembles mathématiques
        "Chiffre_arabe": est_chiffre_arabe(nombre),
        "Entier_naturel": est_entier_naturel(nombre),
        "Entier_positif": est_entier_positif(nombre),
        "Entier_negatif": est_entier_negatif(nombre),
        "Entier_relatif": est_entier_relatif(nombre),
        "Nombre_decimal": est_nombre_decimal(nombre),
        "Rationnel": est_rationnel(nombre),
        "Irrationnel": est_irrationnel(nombre),
        "Reel": est_reel(nombre),
        "Imaginaire_pur": est_imaginaire_pur(nombre),
        "Complexe": est_complexe(nombre),
        
        # Propriétés existantes
        "Est_pair": nombre % 2 == 0,
        "Est_premier": est_premier(nombre),
        "Einaire": bin(nombre)[2:],
        "Eexadecimal": hex(nombre)[2:],
        "Eacine_carree": round(math.sqrt(nombre), 4),
        "Diviseurs": trouver_diviseurs(nombre),
        "Est_fibonacci": est_dans_fibonacci(nombre),
        "Chiffre_romain": convertir_en_romain(nombre),
        "Somme_chiffres": sum(int(chiffre) for chiffre in str(abs(nombre))),
        "Est_carre_parfait": math.sqrt(nombre).is_integer(),
        "Est_cube_parfait": round(nombre ** (1/3)) ** 3 == nombre,
        "Log_base10": round(math.log10(nombre), 4) if nombre > 0 else None,
        "Puissance_de_deux": (nombre & (nombre-1) == 0) and nombre != 0,
        "Nombre_chiffres": len(str(abs(nombre))),
        "Est_abondant": sum(trouver_diviseurs(nombre)[:-1]) > nombre,
        "Est_palindrome": str(nombre) == str(nombre)[::-1],
        "Factorisation_premiers": factoriser_en_premiers(nombre)
    }

    # Ajout des descriptions (conservé pour compatibilité)
    result["_explications"] = {
        prop: DESCRIPTIONS.get(prop, {"description": "Information non disponible"})
        for prop in result.keys() if prop != "_explications"
    }

    return result

# Fonctions des ensembles mathématiques
def est_chiffre_arabe(n):
    return str(n) in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def est_entier_naturel(n):
    try:
        return int(n) >= 0
    except:
        return False

def est_entier_positif(n):
    try:
        return int(n) > 0
    except:
        return False

def est_entier_negatif(n):
    try:
        return int(n) < 0
    except:
        return False

def est_entier_relatif(n):
    try:
        int(n)
        return True
    except:
        return False

def est_nombre_decimal(n):
    try:
        float(n)
        str_n = str(n)
        if '.' in str_n:
            return str_n.split('.')[-1].isdigit()
        return False
    except:
        return False

def est_rationnel(n):
    try:
        Fraction(str(n))
        return True
    except:
        return False

def est_irrationnel(n):
    try:
        float(n)
        return not est_rationnel(n)
    except:
        return False

def est_reel(n):
    try:
        float(n)
        return True
    except:
        return False

def est_imaginaire_pur(n):
    try:
        c = complex(str(n).replace('i', 'j'))
        return c.real == 0 and c.imag != 0
    except:
        return False

def est_complexe(n):
    try:
        complex(str(n).replace('i', 'j'))
        return True
    except:
        return False

# Fonctions auxiliaires existantes
def est_premier(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def trouver_diviseurs(n):
    n = abs(n)
    return [i for i in range(1, n+1) if n % i == 0]

def est_dans_fibonacci(n):
    x = 5 * n**2 + 4
    y = 5 * n**2 - 4
    return x**0.5 % 1 == 0 or y**0.5 % 1 == 0

def convertir_en_romain(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    chiffre_romain = ''
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            chiffre_romain += syms[i]
            n -= val[i]
        i += 1
    return chiffre_romain

def factoriser_en_premiers(n):
    if n < 2: return []
    facteurs = []
    while n % 2 == 0:
        facteurs.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            facteurs.append(i)
            n = n // i
        i += 2
    if n > 1:
        facteurs.append(n)
    return facteurs
































import math
from fractions import Fraction
from .descriptions import DESCRIPTIONS

def calculer_proprietes(nombre):
    result = {
        # Ensembles mathématiques
        "chiffre_arabe": est_chiffre_arabe(nombre),
        "entier_naturel": est_entier_naturel(nombre),
        "entier_positif": est_entier_positif(nombre),
        "entier_negatif": est_entier_negatif(nombre),
        "entier_relatif": est_entier_relatif(nombre),
        "nombre_decimal": est_nombre_decimal(nombre),
        "rationnel": est_rationnel(nombre),
        "irrationnel": est_irrationnel(nombre),
        "reel": est_reel(nombre),
        "imaginaire_pur": est_imaginaire_pur(nombre),
        "complexe": est_complexe(nombre),
        
        # Propriétés existantes
        "est_pair": nombre % 2 == 0,
        "est_premier": est_premier(nombre),
        "binaire": bin(nombre)[2:],
        "hexadecimal": hex(nombre)[2:],
        "racine_carree": round(math.sqrt(nombre), 4),
        "diviseurs": trouver_diviseurs(nombre),
        "est_fibonacci": est_dans_fibonacci(nombre),
        "chiffre_romain": convertir_en_romain(nombre),
        "somme_chiffres": sum(int(chiffre) for chiffre in str(abs(nombre))),
        "est_carre_parfait": math.sqrt(nombre).is_integer(),
        "est_cube_parfait": round(nombre ** (1/3)) ** 3 == nombre,
        "log_base10": round(math.log10(nombre), 4) if nombre > 0 else None,
        "puissance_de_deux": (nombre & (nombre-1) == 0) and nombre != 0,
        "nombre_chiffres": len(str(abs(nombre))),
        "est_abondant": sum(trouver_diviseurs(nombre)[:-1]) > nombre,
        "est_palindrome": str(nombre) == str(nombre)[::-1],
        "factorisation_premiers": factoriser_en_premiers(nombre)
    }

    # Ajout des descriptions
    result["_explications"] = {
        prop: DESCRIPTIONS.get(prop, {"description": "Information non disponible"})
        for prop in result.keys() if prop != "_explications"
    }

    return result

