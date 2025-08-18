import math
from fractions import Fraction
from translations import get_descriptions


# ================================
# Fonctions principales
# ================================

def calculer_proprietes_avec_descriptions(nombre, lang="fr"):
    """Calcule les propriétés d'un nombre et ajoute les descriptions associées (localisées)."""
    proprietes_calculees = calculer_proprietes(nombre, lang=lang)
    descriptions = get_descriptions(lang)

    resultat = {
        "nombre": nombre,
        "proprietes": []
    }

    for prop, valeur in proprietes_calculees.items():
        if prop == "_explications":
            continue

        description = descriptions.get(prop, {
            "description": "Description non disponible",
            "methode": "",
            "exemple": ""
        })

        resultat["proprietes"].append({
            "nom": prop.replace("_", " ").capitalize(),
            "valeur": valeur,
            "description": description["description"],
            "methode_calcul": description.get("methode", ""),
            "exemple": description.get("exemple", "")
        })

    return resultat


def calculer_proprietes(nombre, lang: str = "fr"):
    """Calcule les propriétés mathématiques et numériques d'un nombre."""
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

        # Propriétés numériques
        "est_pair": nombre % 2 == 0,
        "est_premier": est_premier(nombre),
        "binaire": bin(nombre)[2:],
        "hexadecimal": hex(nombre)[2:],
        "racine_carree": round(math.sqrt(nombre), 4) if nombre >= 0 else None,
        "diviseurs": trouver_diviseurs(nombre),
        "est_fibonacci": est_dans_fibonacci(nombre),
        "chiffre_romain": convertir_en_romain(nombre),
        "somme_chiffres": sum(int(chiffre) for chiffre in str(abs(nombre))),
        "est_carre_parfait": (nombre >= 0) and (math.isqrt(nombre) ** 2 == nombre),
        "est_cube_parfait": (round(abs(nombre) ** (1 / 3)) ** 3 == abs(nombre)),
        "log_base10": round(math.log10(nombre), 4) if nombre > 0 else None,
        "puissance_de_deux": (nombre > 0) and (nombre & (nombre - 1) == 0),
        "nombre_chiffres": len(str(abs(nombre))),
        "est_abondant": sum(trouver_diviseurs(nombre)[:-1]) > nombre,
        "est_palindrome": str(nombre) == str(nombre)[::-1],
        "factorisation_premiers": factoriser_en_premiers(nombre)
    }

    # Ajout des descriptions
    descriptions = get_descriptions(lang)
    result["_explications"] = {
        prop: descriptions.get(prop, {"description": "Information non disponible"})
        for prop in result.keys() if prop != "_explications"
    }

    return result


# ================================
# Fonctions d'ensembles mathématiques
# ================================

def est_chiffre_arabe(n):
    return str(n) in list("0123456789")


def est_entier_naturel(n):
    try:
        return int(n) >= 0
    except Exception:
        return False


def est_entier_positif(n):
    try:
        return int(n) > 0
    except Exception:
        return False


def est_entier_negatif(n):
    try:
        return int(n) < 0
    except Exception:
        return False


def est_entier_relatif(n):
    try:
        int(n)
        return True
    except Exception:
        return False


def est_nombre_decimal(n):
    try:
        float(n)
        str_n = str(n)
        return "." in str_n and str_n.split(".")[-1].isdigit()
    except Exception:
        return False


def est_rationnel(n):
    try:
        Fraction(str(n))
        return True
    except Exception:
        return False


def est_irrationnel(n):
    try:
        float(n)
        return not est_rationnel(n)
    except Exception:
        return False


def est_reel(n):
    try:
        float(n)
        return True
    except Exception:
        return False


def est_imaginaire_pur(n):
    try:
        c = complex(str(n).replace("i", "j"))
        return c.real == 0 and c.imag != 0
    except Exception:
        return False


def est_complexe(n):
    try:
        complex(str(n).replace("i", "j"))
        return True
    except Exception:
        return False


# ================================
# Fonctions auxiliaires
# ================================

def est_premier(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def trouver_diviseurs(n):
    n = abs(n)
    return [i for i in range(1, n + 1) if n % i == 0]


def est_dans_fibonacci(n):
    x = 5 * n**2 + 4
    y = 5 * n**2 - 4
    return x**0.5 % 1 == 0 or y**0.5 % 1 == 0


def convertir_en_romain(n):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    chiffre_romain = ""
    i = 0
    while n > 0:
        for _ in range(n // val[i]):
            chiffre_romain += syms[i]
            n -= val[i]
        i += 1
    return chiffre_romain


def factoriser_en_premiers(n):
    if n < 2:
        return []
    facteurs = []
    while n % 2 == 0:
        facteurs.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            facteurs.append(i)
            n //= i
        i += 2
    if n > 1:
        facteurs.append(n)
    return facteurs
