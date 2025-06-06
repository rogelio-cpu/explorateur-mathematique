from .utils import (
    est_chiffre_arabe, est_nombre_arabe, est_entier_naturel, est_entier_naturel_negatif,
    est_decimal_fini, est_fraction_rationnelle, est_nombre_rationnel, est_irrationnel_connu,
    est_reel, est_imaginaire_pur, est_complexe, get_ensemble_definitions
)
from django.utils.translation import gettext_lazy as _

def analyser_nombre(nombre):
    """Analyse complète d'un nombre avec résultats détaillés"""
    if isinstance(nombre, float):
        nombre = str(nombre)

    definitions = get_ensemble_definitions()
    
    # Renommer les clés en snake_case (valeurs déjà prêtes)
    noms_ensembles = {
        'chiffre_arabe': 'Ensemble des chiffres arabes',
        'nombre_arabe': 'Ensemble des nombres arabes',
        'entier_naturel': 'Ensemble des entiers naturels',
        'entier_naturel_negatif': 'Ensemble des entiers naturels négatifs',
        'entier_relatif': 'Ensemble des entiers relatifs',
        'decimal_fini': 'Ensemble des décimaux finis',
        'fraction_rationnelle': 'Ensemble des fractions rationnelles',
        'nombre_rationnel': 'Ensemble des nombres rationnels',
        'irrationnel_connu': 'Ensemble des irrationnels connus',
        'reel': 'Ensemble des nombres réels',
        'imaginaire_pur': 'Ensemble des imaginaires purs',
        'complexe': 'Ensemble des nombres complexes'
    }

    result = {
        key: {
            'nom': noms_ensembles.get(key, key.replace('_', ' ').capitalize()),
            'appartient': False,
            'definition': definitions[key]['definition'],
            'description': definitions[key]['description'],
            'explication': ""
        } for key in definitions
    }

    # Vérifications (inchangées sauf noms de clés déjà en underscore)
    result['chiffre_arabe']['appartient'] = est_chiffre_arabe(nombre)
    result['chiffre_arabe']['explication'] = (
        f"{nombre} ∈ A : C'est bien un chiffre entre 0 et 9." if result['chiffre_arabe']['appartient']
        else f"{nombre} ∉ A" +
             (f"\n↪ Contient {len(nombre)} caractères" if len(nombre) != 1 else "") +
             ("\n↪ Contient des caractères non numériques" if not nombre.isdigit() else "")
    )

    result['nombre_arabe']['appartient'] = est_nombre_arabe(nombre)
    result['nombre_arabe']['explication'] = (
        f"{nombre} ∈ B : Nombre composé de chiffres sans zéro initial." if result['nombre_arabe']['appartient']
        else f"{nombre} ∉ B" +
             ("\n↪ Moins de 2 chiffres" if len(nombre) < 2 else "") +
             ("\n↪ Commence par zéro" if nombre.startswith('0') else "") +
             ("\n↪ Contient des caractères non numériques" if not nombre.isdigit() else "")
    )

    result['entier_naturel']['appartient'] = est_entier_naturel(nombre)
    result['entier_naturel']['explication'] = (
        f"{nombre} ∈ ℕ : C'est 0 ou un nombre arabe valide." if result['entier_naturel']['appartient']
        else f"{nombre} ∉ ℕ\n↪ Ce n'est ni '0' ni un nombre arabe conforme"
    )

    result['entier_naturel_negatif']['appartient'] = est_entier_naturel_negatif(nombre)
    result['entier_naturel_negatif']['explication'] = (
        f"{nombre} ∈ ℕ⁻ : C'est un entier négatif avec une partie positive conforme à B." if result['entier_naturel_negatif']['appartient']
        else f"{nombre} ∉ ℕ⁻" +
             ("\n↪ Ne commence pas par '-'" if not nombre.startswith('-') else "") +
             ("\n↪ La partie après '-' n'est pas un nombre arabe valide" if nombre.startswith('-') else "")
    )

    result['entier_relatif']['appartient'] = (
        result['entier_naturel']['appartient'] or result['entier_naturel_negatif']['appartient']
    )
    result['entier_relatif']['explication'] = (
        f"{nombre} ∈ ℤ : C'est un entier positif, nul ou négatif." if result['entier_relatif']['appartient']
        else f"{nombre} ∉ ℤ\n↪ Ce n'est ni un entier naturel ni un entier négatif connu"
    )

    result['decimal_fini']['appartient'] = est_decimal_fini(nombre)
    result['decimal_fini']['explication'] = (
        f"{nombre} ∈ 𝔻 : Il s'agit d'un nombre avec une partie décimale finie." if result['decimal_fini']['appartient']
        else f"{nombre} ∉ 𝔻" +
             ("\n↪ Ne contient pas de point décimal" if '.' not in nombre else "") +
             ("\n↪ Le format n'est pas celui d'un décimal fini ou tous les chiffres après la virgule sont nuls"
              if '.' in nombre else "")
    )

    result['fraction_rationnelle']['appartient'] = est_fraction_rationnelle(nombre)
    result['fraction_rationnelle']['explication'] = (
        f"{nombre} ∈ F : C'est une fraction non décimale avec dénominateur ≠ 10ⁿ." if result['fraction_rationnelle']['appartient']
        else f"{nombre} ∉ F" +
             ("\n↪ N'est pas une fraction" if '/' not in nombre else "") +
             ("\n↪ Le dénominateur est une puissance de 10 (forme décimale déguisée)" if '/' in nombre else "")
    )

    result['nombre_rationnel']['appartient'] = est_nombre_rationnel(nombre)
    result['nombre_rationnel']['explication'] = (
        f"{nombre} ∈ ℚ : Il peut s'écrire comme un rapport de deux entiers." if result['nombre_rationnel']['appartient']
        else f"{nombre} ∉ ℚ\n↪ Ce nombre ne peut pas être exprimé comme une fraction exacte de deux entiers"
    )

    result['irrationnel_connu']['appartient'] = est_irrationnel_connu(nombre)
    result['irrationnel_connu']['explication'] = (
        f"{nombre} est un irrationnel célèbre." if result['irrationnel_connu']['appartient']
        else f"{nombre} n'est pas un irrationnel célèbre connu\n↪ Vous pouvez essayer 'pi', 'e', 'sqrt(2)'..."
    )

    result['reel']['appartient'] = est_reel(nombre)
    result['reel']['explication'] = (
        f"{nombre} ∈ ℝ\n↪ Le nombre est un entier ou un décimal valide." if result['reel']['appartient']
        else f"{nombre} ∉ ℝ\n↪ Le nombre ne correspond pas à une représentation réelle standard"
    )

    result['imaginaire_pur']['appartient'] = est_imaginaire_pur(nombre)
    result['imaginaire_pur']['explication'] = (
        f"{nombre} ∈ iℝ\n↪ Le nombre est bien de la forme 'bi' avec b réel." if result['imaginaire_pur']['appartient']
        else f"{nombre} ∉ iℝ\n↪ Le nombre n'est pas un imaginaire pur (ex: '3i', '-1.5i')"
    )

    result['complexe']['appartient'] = est_complexe(nombre)
    result['complexe']['explication'] = (
        f"{nombre} ∈ ℂ\n↪ Le nombre est bien un complexe (a + bi, ou ℝ ou iℝ)." if result['complexe']['appartient']
        else f"{nombre} ∉ ℂ\n↪ Le nombre n'est pas un complexe valide"
    )

    return result
