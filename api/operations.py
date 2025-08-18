from .utils import (
    est_chiffre_arabe,
    est_nombre_arabe,
    est_entier_naturel,
    est_entier_relatif,
    est_entier_naturel_negatif,
    est_decimal_fini,
    est_fraction_rationnelle,
    est_nombre_rationnel,
    est_irrationnel_connu,
    est_reel,
    est_imaginaire_pur,
    est_complexe,
    get_ensemble_definitions,
)

from translations import get_descriptions


# Configuration des ensembles analysés (clés harmonisées avec les traductions)
ENSEMBLES_CONFIG = {
    "chiffre_arabe": est_chiffre_arabe,
    # "nombre_arabe" n'a pas de définition dans les traductions → ignoré
    "entier_naturel": est_entier_naturel,
    "entier_negatif": est_entier_naturel_negatif,
    "entier_relatif": est_entier_relatif,
    "nombre_decimal": est_decimal_fini,
    # "fraction_rationnelle" n'a pas d'entrée de définition standard → ignoré
    "rationnel": est_nombre_rationnel,
    "irrationnel": est_irrationnel_connu,
    "reel": est_reel,
    "imaginaire_pur": est_imaginaire_pur,
    "complexe": est_complexe,
}


def analyser_nombre(nombre, lang="fr"):
    """Analyse un nombre et renvoie les résultats avec définitions et explications localisées."""
    if isinstance(nombre, float):
        nombre = str(nombre)

    # Définitions et descriptions dans la langue
    definitions = get_ensemble_definitions(lang)
    descriptions = get_descriptions(lang)

    result = {}

    for ensemble_key, predicate in ENSEMBLES_CONFIG.items():
        try:
            appartient = bool(predicate(nombre))
        except Exception:
            appartient = False

        # Récupération des méta-infos
        desc = descriptions.get(ensemble_key, {})
        defn = definitions.get(ensemble_key, {})

        bloc = {
            "nom": desc.get("nom", ensemble_key),
            "appartient": appartient,
            "definition": defn.get("definition", desc.get("definition", "")),
            "description": defn.get("description", desc.get("description", "")),
            "explication": "",
        }

        if appartient:
            bloc["explication"] = desc.get("true", "{nombre} ∈ set").format(nombre=nombre)
        else:
            bloc["explication"] = desc.get("false", "{nombre} ∉ set").format(nombre=nombre)

        result[ensemble_key] = bloc

    return result
