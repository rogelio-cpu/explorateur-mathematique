from .utils import (
    est_chiffre_arabe, est_nombre_arabe, est_entier_naturel, est_entier_naturel_negatif, est_decimal_fini, est_fraction_rationnelle, est_nombre_rationnel, est_irrationnel_connu, est_reel, est_imaginaire_pur, est_complexe, get_ensemble_definitions
)

def analyser_nombre(nombre):
    """Analyse complète d'un nombre avec résultats détaillés"""
    # Convertir en string si c'est un float
    if isinstance(nombre, float):
        nombre = str(nombre)
    
    definitions = get_ensemble_definitions()
    
    result = {key: {
        'appartient': False,
        'definition': definitions[key]['definition'],
        'description': definitions[key]['description'],
        'explication': ""
    } for key in definitions}
    
    # 1. Chiffre arabe
    result['chiffre_arabe']['appartient'] = est_chiffre_arabe(nombre)
    if result['chiffre_arabe']['appartient']:
        result['chiffre_arabe']['explication'] = f"{nombre} ∈ A : C'est bien un chiffre entre 0 et 9."
    else:
        explication = f"{nombre} ∉ A"
        if len(nombre) != 1:
            explication += f"\n↪ Contient {len(nombre)} caractères (doit être un seul chiffre)"
        if not nombre.isdigit():
            explication += "\n↪ Contient des caractères non numériques"
        result['chiffre_arabe']['explication'] = explication
    
    # 2. Nombre arabe
    result['nombre_arabe']['appartient'] = est_nombre_arabe(nombre)
    if result['nombre_arabe']['appartient']:
        result['nombre_arabe']['explication'] = f"{nombre} ∈ B : Nombre composé de chiffres sans zéro initial."
    else:
        explication = f"{nombre} ∉ B"
        if len(nombre) < 2:
            explication += "\n↪ Moins de 2 chiffres"
        elif nombre[0] == '0':
            explication += "\n↪ Commence par zéro"
        elif not nombre.isdigit():
            explication += "\n↪ Contient des caractères non numériques"
        result['nombre_arabe']['explication'] = explication
    
    # 3. Entier naturel
    result['entier_naturel']['appartient'] = est_entier_naturel(nombre)
    if result['entier_naturel']['appartient']:
        result['entier_naturel']['explication'] = f"{nombre} ∈ ℕ : C'est 0 ou un nombre arabe valide."
    else:
        explication = f"{nombre} ∉ ℕ"
        if nombre != '0':
            explication += "\n↪ Ce n'est ni '0' ni un nombre arabe conforme"
        result['entier_naturel']['explication'] = explication
    
    # 4. Entier naturel négatif
    result['entier_naturel_negatif']['appartient'] = est_entier_naturel_negatif(nombre)
    if result['entier_naturel_negatif']['appartient']:
        result['entier_naturel_negatif']['explication'] = f"{nombre} ∈ ℕ⁻ : C'est un entier négatif avec une partie positive conforme à B."
    else:
        explication = f"{nombre} ∉ ℕ⁻"
        if not nombre.startswith('-'):
            explication += "\n↪ Ne commence pas par '-'"
        else:
            explication += "\n↪ La partie après '-' n'est pas un nombre arabe valide"
        result['entier_naturel_negatif']['explication'] = explication
    
    # 5. Entier relatif
    result['entier_relatif']['appartient'] = (result['entier_naturel']['appartient'] or 
                                            result['entier_naturel_negatif']['appartient'])
    if result['entier_relatif']['appartient']:
        result['entier_relatif']['explication'] = f"{nombre} ∈ ℤ : C'est un entier positif, nul ou négatif."
    else:
        result['entier_relatif']['explication'] = f"{nombre} ∉ ℤ\n↪ Ce n'est ni un entier naturel ni un entier négatif connu"
    
    # 6. Décimal fini
    result['decimal_fini']['appartient'] = est_decimal_fini(nombre)
    if result['decimal_fini']['appartient']:
        result['decimal_fini']['explication'] = f"{nombre} ∈ 𝔻 : Il s'agit d'un nombre avec une partie décimale finie."
    else:
        explication = f"{nombre} ∉ 𝔻"
        if '.' not in nombre:
            explication += "\n↪ Ne contient pas de point décimal"
        else:
            explication += "\n↪ Le format n'est pas celui d'un décimal fini ou tous les chiffres après la virgule sont nuls"
        result['decimal_fini']['explication'] = explication
    
    # 7. Fraction rationnelle
    result['fraction_rationnelle']['appartient'] = est_fraction_rationnelle(nombre)
    if result['fraction_rationnelle']['appartient']:
        result['fraction_rationnelle']['explication'] = f"{nombre} ∈ F : C'est une fraction non décimale avec dénominateur ≠ 10ⁿ."
    else:
        explication = f"{nombre} ∉ F"
        if '/' not in nombre:
            explication += "\n↪ N'est pas une fraction"
        else:
            explication += "\n↪ Le dénominateur est une puissance de 10 (forme décimale déguisée)"
        result['fraction_rationnelle']['explication'] = explication
    
    # 8. Nombre rationnel
    result['nombre_rationnel']['appartient'] = est_nombre_rationnel(nombre)
    if result['nombre_rationnel']['appartient']:
        result['nombre_rationnel']['explication'] = f"{nombre} ∈ ℚ : Il peut s'écrire comme un rapport de deux entiers."
    else:
        result['nombre_rationnel']['explication'] = f"{nombre} ∉ ℚ\n↪ Ce nombre ne peut pas être exprimé comme une fraction exacte de deux entiers"
    
    # 9. Irrationnel connu
    result['irrationnel_connu']['appartient'] = est_irrationnel_connu(nombre)
    if result['irrationnel_connu']['appartient']:
        result['irrationnel_connu']['explication'] = f"{nombre} est un irrationnel célèbre."
    else:
        result['irrationnel_connu']['explication'] = f"{nombre} n'est pas un irrationnel célèbre connu\n↪ Vous pouvez essayer 'pi', 'e', 'sqrt(2)'..."
    
    # 10. Réel
    result['reel']['appartient'] = est_reel(nombre)
    if result['reel']['appartient']:
        result['reel']['explication'] = f"{nombre} ∈ ℝ\n↪ Le nombre est un entier ou un décimal valide."
    else:
        result['reel']['explication'] = f"{nombre} ∉ ℝ\n↪ Le nombre ne correspond pas à une représentation réelle standard"
    
    # 11. Imaginaire pur
    result['imaginaire_pur']['appartient'] = est_imaginaire_pur(nombre)
    if result['imaginaire_pur']['appartient']:
        result['imaginaire_pur']['explication'] = f"{nombre} ∈ iℝ\n↪ Le nombre est bien de la forme 'bi' avec b réel."
    else:
        result['imaginaire_pur']['explication'] = f"{nombre} ∉ iℝ\n↪ Le nombre n'est pas un imaginaire pur (ex: '3i', '-1.5i')"
    
    # 12. Complexe
    result['complexe']['appartient'] = est_complexe(nombre)
    if result['complexe']['appartient']:
        result['complexe']['explication'] = f"{nombre} ∈ ℂ\n↪ Le nombre est bien un complexe (a + bi, ou ℝ ou iℝ)."
    else:
        result['complexe']['explication'] = f"{nombre} ∉ ℂ\n↪ Le nombre n'est pas un complexe valide"
    
    return result 