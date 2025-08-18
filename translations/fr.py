DESCRIPTIONS_FR ={
    "chiffre_arabe": {
        "nom": "Chiffre arabe",
        "definition": "A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
        "description": "Un chiffre arabe est un symbole élémentaire (0-9) du système de numération moderne.",
        "exemple": "5, 7, 9",
        "true": "{nombre} ∈ A → C'est un chiffre entre 0 et 9",
        "false": "{nombre} ∉ A → N'est pas un chiffre valide"
    },
    "entier_naturel": {
        "nom": "Entier naturel",
        "definition": "ℕ = {0, 1, 2, 3, ...}",
        "description": "Entier non négatif (ℕ).",
        "exemple": "0, 42, 1000",
        "true": "{nombre} ∈ ℕ",
        "false": "{nombre} ∉ ℕ"
    },
    "entier_positif": {
        "nom": "Entier strictement positif",
        "definition": "ℕ* = {1, 2, 3, ...}",
        "description": "Entier strictement positif.",
        "exemple": "1, 99",
        "true": "{nombre} ∈ ℕ*",
        "false": "{nombre} ∉ ℕ*"
    },
    "entier_negatif": {
        "nom": "Entier strictement négatif",
        "definition": "ℤ⁻ = {-1, -2, -3, ...}",
        "description": "Entier strictement négatif.",
        "exemple": "-5, -100",
        "true": "{nombre} ∈ ℤ⁻",
        "false": "{nombre} ∉ ℤ⁻"
    },
    "entier_relatif": {
        "nom": "Entier relatif",
        "definition": "ℤ = {..., -2, -1, 0, 1, 2, ...}",
        "description": "Entier positif ou négatif.",
        "exemple": "-3, 0, 7",
        "true": "{nombre} ∈ ℤ",
        "false": "{nombre} ∉ ℤ"
    },
    "nombre_decimal": {
        "nom": "Nombre décimal",
        "definition": "Nombre avec un nombre fini de chiffres après la virgule",
        "description": "Nombre rationnel à écriture décimale finie.",
        "exemple": "3.14, -0.5",
        "attention": "1/3 = 0.333... n'est pas un décimal fini",
        "true": "{nombre} est un nombre décimal fini",
        "false": "{nombre} n'est pas un nombre décimal fini"
    },
    "rationnel": {
        "nom": "Nombre rationnel",
        "definition": "ℚ = {a/b | a, b ∈ ℤ, b ≠ 0}",
        "description": "Nombre pouvant s'exprimer comme quotient d'entiers.",
        "exemple": "1/2, -4/3, 0.75",
        "true": "{nombre} ∈ ℚ",
        "false": "{nombre} ∉ ℚ"
    },
    "irrationnel": {
        "nom": "Nombre irrationnel",
        "definition": "ℝ \\ ℚ",
        "description": "Réel qui n'est pas rationnel.",
        "exemple": "√2, π, e",
        "true": "{nombre} est irrationnel",
        "false": "{nombre} n'est pas irrationnel"
    },
    "reel": {
        "nom": "Nombre réel",
        "definition": "ℝ = ℚ ∪ Irrationnels",
        "description": "Ensemble des rationnels et irrationnels.",
        "exemple": "-5, 3.14, √2",
        "true": "{nombre} ∈ ℝ",
        "false": "{nombre} ∉ ℝ"
    },
    "imaginaire_pur": {
        "nom": "Imaginaire pur",
        "definition": "iℝ = {bi | b ∈ ℝ}",
        "description": "Nombre complexe sans partie réelle (de la forme bi).",
        "exemple": "2i, -3.5i",
        "true": "{nombre} ∈ iℝ",
        "false": "{nombre} ∉ iℝ"
    },
    "complexe": {
        "nom": "Nombre complexe",
        "definition": "ℂ = {a + bi | a, b ∈ ℝ}",
        "description": "Nombre de la forme a + bi avec a et b réels.",
        "exemple": "3+4i, -1.5-2i",
        "true": "{nombre} ∈ ℂ",
        "false": "{nombre} ∉ ℂ"
    },
    "est_pair": {
        "nom": "Nombre pair",
        "description": "Nombre divisible par 2",
        "methode": "n % 2 == 0",
        "exemple": "4 → vrai, 7 → faux",
        "true": "{nombre} est pair",
        "false": "{nombre} est impair"
    },
    "est_premier": {
        "nom": "Nombre premier",
        "description": "Nombre ayant exactement deux diviseurs distincts : 1 et lui-même",
        "methode": "Test de divisibilité de 2 à √n",
        "exemple": "7 → vrai, 6 → faux",
        "true": "{nombre} est premier",
        "false": "{nombre} n'est pas premier"
    },
    "binaire": {
        "nom": "Représentation binaire",
        "description": "Représentation du nombre en base 2",
        "methode": "Conversion via bin() puis suppression du préfixe '0b'",
        "exemple": "5 → '101'"
    },
    "hexadecimal": {
        "nom": "Représentation hexadécimale",
        "description": "Représentation du nombre en base 16",
        "methode": "Conversion via hex() puis suppression du préfixe '0x'",
        "exemple": "255 → 'ff'"
    },
    "racine_carree": {
        "nom": "Racine carrée",
        "description": "Nombre qui multiplié par lui-même donne le nombre original",
        "methode": "math.sqrt() arrondi à 4 décimales",
        "attention": "Définie seulement pour n ≥ 0",
        "true": "√{nombre} existe",
        "false": "√{nombre} n'existe pas"
    },
    "diviseurs": {
        "nom": "Diviseurs",
        "description": "Liste de tous les entiers qui divisent n sans reste",
        "methode": "Test de divisibilité de 1 à n",
        "exemple": "6 → [1,2,3,6]"
    },
    "est_fibonacci": {
        "nom": "Nombre de Fibonacci",
        "description": "Nombre appartenant à la suite de Fibonacci",
        "methode": "5n²±4 doit être un carré parfait",
        "exemple": "8 → vrai, 9 → faux",
        "true": "{nombre} appartient à la suite de Fibonacci",
        "false": "{nombre} n'appartient pas à la suite de Fibonacci"
    },
    "chiffre_romain": {
        "nom": "Numération romaine",
        "description": "Numération romaine utilisant les symboles I,V,X,L,C,D,M",
        "regles": [
            "Addition si valeur supérieure ou égale : VI = 6",
            "Soustraction si valeur inférieure : IV = 4"
        ],
        "valeurs": {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    },
    "somme_chiffres": {
        "nom": "Somme des chiffres",
        "description": "Somme de tous les chiffres composant le nombre",
        "methode": "Conversion en chaîne puis somme des chiffres convertis en int",
        "exemple": "123 → 6"
    },
    "est_carre_parfait": {
        "nom": "Carré parfait",
        "description": "Nombre qui est le carré d'un entier",
        "methode": "Vérifie si √n est entier",
        "exemple": "9 → vrai, 10 → faux"
    },
    "est_cube_parfait": {
        "nom": "Cube parfait",
        "description": "Nombre qui est le cube d'un entier",
        "methode": "Vérifie si ∛n est entier",
        "exemple": "8 → vrai, 9 → faux"
    },
    "log_base10": {
        "nom": "Logarithme décimal",
        "description": "Logarithme base 10 du nombre",
        "attention": "Défini seulement pour n > 0",
        "exemple": "100 → 2"
    },
    "puissance_de_deux": {
        "nom": "Puissance de deux",
        "description": "Nombre qui peut s'écrire sous la forme 2^k",
        "methode": "Vérification via opération bit à bit : n & (n-1) == 0",
        "exemple": "8 → vrai, 6 → faux"
    },
    "nombre_chiffres": {
        "nom": "Nombre de chiffres",
        "description": "Quantité de chiffres dans l'écriture décimale du nombre",
        "methode": "Conversion en chaîne puis calcul de la longueur",
        "exemple": "-123 → 3 chiffres"
    },
    "est_abondant": {
        "nom": "Nombre abondant",
        "description": "Nombre dont la somme des diviseurs propres est supérieure à lui-même",
        "diviseurs_propres": "Tous les diviseurs sauf le nombre lui-même",
        "exemple": "12 → vrai"
    },
    "est_palindrome": {
        "nom": "Palindrome",
        "description": "Nombre qui se lit identiquement de gauche à droite et de droite à gauche",
        "methode": "Comparaison avec sa version inversée",
        "exemple": "12321 → vrai, 123 → faux"
    },
    "factorisation_premiers": {
        "nom": "Factorisation en nombres premiers",
        "description": "Décomposition en produit de nombres premiers",
        "methode": "Division successive par les nombres premiers",
        "exemple": "84 → [2,2,3,7]"
    },
    "cosinus": {
        "nom": "Cosinus",
        "description": "Cosinus de l'angle en radians",
        "attention": "Le nombre est interprété comme un angle en radians",
        "exemple": "math.pi → -1"
    },
    "sinus": {
        "nom": "Sinus",
        "description": "Sinus de l'angle en radians",
        "exemple": "math.pi/2 → 1"
    }
}
