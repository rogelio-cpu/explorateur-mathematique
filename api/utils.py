import math
import re
from translations import DESCRIPTIONS, get_descriptions


# =============================
#   Vérifications de nombres
# =============================

def est_chiffre_arabe(nombre: str) -> bool:
    """Vérifie si c'est un chiffre arabe unique (0-9)."""
    return str(nombre) in "0123456789" and len(str(nombre)) == 1


def est_nombre_arabe(nombre: str) -> bool:
    """Vérifie si c'est un nombre arabe valide (≥ 2 chiffres, ne commence pas par 0)."""
    nombre_str = str(nombre)
    return nombre_str.isdigit() and len(nombre_str) >= 2 and not nombre_str.startswith("0")


def est_entier_naturel(nombre: str) -> bool:
    """Vérifie si c'est un entier naturel (0 ou nombre arabe valide)."""
    nombre_str = str(nombre)
    return (
        nombre_str == "0"
        or est_chiffre_arabe(nombre_str)
        or est_nombre_arabe(nombre_str)
    )


def est_entier_naturel_negatif(nombre: str) -> bool:
    """Vérifie si c'est un entier naturel négatif (-n où n est un entier naturel)."""
    nombre_str = str(nombre)
    return nombre_str.startswith("-") and est_entier_naturel(nombre_str[1:])


def est_entier_relatif(nombre: str) -> bool:
    """Vérifie si c'est un entier relatif."""
    return est_entier_naturel(nombre) or est_entier_naturel_negatif(nombre)


def est_decimal_fini(nombre: str) -> bool:
    """Vérifie si c'est un décimal fini."""
    if "." not in str(nombre):
        return False
    partie_entiere, partie_decimale = str(nombre).split(".", 1)

    # Partie entière
    if partie_entiere.startswith("-"):
        valide_entiere = est_entier_naturel(partie_entiere[1:]) or partie_entiere == "-"
    else:
        valide_entiere = est_entier_naturel(partie_entiere) or partie_entiere == ""

    # Partie décimale
    return valide_entiere and partie_decimale.isdigit() and len(partie_decimale) > 0


def est_fraction_rationnelle(nombre: str) -> bool:
    """Vérifie si c'est une fraction rationnelle p/q avec q ≠ 0."""
    if "/" not in str(nombre):
        return False
    num, den = str(nombre).split("/", 1)
    return est_entier_relatif(num) and est_entier_relatif(den) and int(den) != 0


def est_nombre_rationnel(nombre: str) -> bool:
    """Vérifie si le nombre est rationnel."""
    try:
        float(nombre)
        return True
    except ValueError:
        return est_fraction_rationnelle(nombre)


def est_irrationnel_connu(nombre: str) -> bool:
    """Reconnaît quelques irrationnels célèbres."""
    return str(nombre).lower() in ["pi", "e", "sqrt(2)", "sqrt(3)", "sqrt(5)", "phi"]


def est_reel(nombre: str) -> bool:
    """Vérifie si c'est un réel."""
    try:
        float(nombre)
        return True
    except ValueError:
        return est_irrationnel_connu(nombre)


def est_imaginaire_pur(nombre: str) -> bool:
    """Vérifie si c'est un imaginaire pur bi."""
    if not str(nombre).endswith("i"):
        return False
    partie = nombre[:-1]
    return partie in ("", "+", "-") or est_reel(partie)


def est_complexe(nombre: str) -> bool:
    """Vérifie si c'est un complexe a+bi."""
    if "+" in nombre:
        try:
            a, bi = nombre.split("+", 1)
            return est_reel(a) and est_imaginaire_pur(bi)
        except ValueError:
            return False
    return est_reel(nombre) or est_imaginaire_pur(nombre)


# =============================
#   Définitions (DESCRIPTIONS)
# =============================

def get_ensemble_definitions(lang: str = "fr"):
    """Retourne un sous-dictionnaire des ensembles avec fallback sur l'anglais si manquant."""
    current = DESCRIPTIONS.get(lang, get_descriptions("en"))
    fallback = get_descriptions("en")

    keys = [
        "chiffre_arabe",
        "entier_naturel",
        "entier_positif",
        "entier_negatif",
        "entier_relatif",
        "nombre_decimal",
        "rationnel",
        "irrationnel",
        "reel",
        "complexe",
    ]

    ensembles = {}
    for key in keys:
        ensembles[key] = current.get(key, fallback.get(key, {}))
    return ensembles


# =============================
#   Nettoyage & Détection
# =============================

def nettoyer_expression(expression: str) -> str:
    """Nettoie et normalise une expression mathématique."""
    # Décodage URL
    expression = (
        expression.replace("%2B", "+")
        .replace("%2D", "-")
        .replace("%2A", "*")
        .replace("%2F", "/")
        .replace(" ", "")
    )

    # Espaces autour des opérateurs
    for op in ["+", "-", "*", "/"]:
        expression = expression.replace(op, f" {op} ")

    # Multiplication implicite
    expression = re.sub(r"(\d)([a-z])", r"\1 * \2", expression)   # 2x -> 2 * x
    expression = re.sub(r"\)([a-z])", r") * \1", expression)      # cos(x)sin(x)
    expression = re.sub(r"(\d)\(", r"\1 * (", expression)         # 2(x+1)

    return " ".join(expression.split())


def detecter_expression(expression: str) -> dict:
    """Détecte le type d'expression mathématique."""
    expression = nettoyer_expression(expression.lower().strip())

    # Addition / Soustraction
    for op in ["+", "-"]:
        if f" {op} " in expression:
            a, b = expression.split(f" {op} ", 1)
            return {"type": "operation", "operateur": op, "operande1": a, "operande2": b}

    # Multiplication / Division
    for op in ["*", "/"]:
        if f" {op} " in expression:
            a, b = expression.split(f" {op} ", 1)
            return {"type": "operation", "operateur": op, "operande1": a, "operande2": b}

    # Constantes
    if expression in ["pi", "e"]:
        return {"type": "constante", "valeur": expression}

    # Trigonométrie
    if re.match(r"^(sin|cos|tan)\(([^)]+)\)$", expression):
        f, arg = re.findall(r"^(sin|cos|tan)\(([^)]+)\)$", expression)[0]
        return {"type": "trig", "fonction": f, "argument": arg}

    # Racine
    if re.match(r"^sqrt\(([^)]+)\)$", expression):
        return {"type": "sqrt", "argument": re.findall(r"^sqrt\(([^)]+)\)$", expression)[0]}

    # Logarithme base arbitraire : logb(a;b)
    if re.match(r"^logb\(([^;]+);([^)]+)\)$", expression):
        base, arg = re.findall(r"^logb\(([^;]+);([^)]+)\)$", expression)[0]
        return {"type": "log", "base": base, "argument": arg}

    # Puissance
    if "^" in expression:
        base, exp = expression.split("^", 1)
        return {"type": "power", "base": base, "exposant": exp}

    # Fraction
    if "/" in expression:
        num, den = expression.split("/", 1)
        return {"type": "fraction", "numerateur": num, "denominateur": den}

    return {"type": "nombre", "valeur": expression}


# =============================
#   Calculs
# =============================

def nettoyer_resultat(nombre) -> str:
    """Retourne un nombre sans .0 inutile."""
    try:
        nombre_f = float(nombre)
        return str(int(nombre_f)) if nombre_f.is_integer() else str(nombre_f)
    except Exception:
        return str(nombre)


def calculer_expression(expression: str) -> str:
    """Calcule la valeur d'une expression mathématique simple."""
    try:
        expr = detecter_expression(expression)

        if expr["type"] == "operation":
            op1 = float(calculer_expression(expr["operande1"]))
            op2 = float(calculer_expression(expr["operande2"]))
            if expr["operateur"] == "+":
                return nettoyer_resultat(op1 + op2)
            if expr["operateur"] == "-":
                return nettoyer_resultat(op1 - op2)
            if expr["operateur"] == "*":
                return nettoyer_resultat(op1 * op2)
            if expr["operateur"] == "/":
                if op2 == 0:
                    raise ZeroDivisionError("Division par zéro")
                return nettoyer_resultat(op1 / op2)

        elif expr["type"] == "constante":
            return nettoyer_resultat(math.pi if expr["valeur"] == "pi" else math.e)

        elif expr["type"] == "trig":
            # Les descriptions indiquent que l'argument est en radians
            angle = float(calculer_expression(expr["argument"]))
            if expr["fonction"] == "sin":
                return nettoyer_resultat(math.sin(angle))
            if expr["fonction"] == "cos":
                return nettoyer_resultat(math.cos(angle))
            if expr["fonction"] == "tan":
                return nettoyer_resultat(math.tan(angle))

        elif expr["type"] == "sqrt":
            return nettoyer_resultat(math.sqrt(float(calculer_expression(expr["argument"]))))

        elif expr["type"] == "log":
            base = float(calculer_expression(expr["base"]))
            arg = float(calculer_expression(expr["argument"]))
            return nettoyer_resultat(math.log(arg, base))

        elif expr["type"] == "power":
            base = float(calculer_expression(expr["base"]))
            exp = float(calculer_expression(expr["exposant"]))
            return nettoyer_resultat(math.pow(base, exp))

        elif expr["type"] == "fraction":
            num = float(calculer_expression(expr["numerateur"]))
            den = float(calculer_expression(expr["denominateur"]))
            if den == 0:
                raise ZeroDivisionError("Division par zéro")
            return nettoyer_resultat(num / den)

        return nettoyer_resultat(expr["valeur"])

    except Exception as e:
        raise ValueError(f"Erreur de calcul : {str(e)}")
