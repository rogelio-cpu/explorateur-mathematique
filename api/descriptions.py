DESCRIPTIONS = {
    # Ensembles mathématiques
    "chiffre_arabe": {
        "description": "Un chiffre arabe est un symbole de base (0-9) utilisé dans le système numérique moderne.",
        "condition": "Doit être un seul caractère parmi 0,1,2,3,4,5,6,7,8,9"
    },
    
    "entier_naturel": {
        "description": "Nombre entier positif ou nul (ℕ = {0, 1, 2, 3, ...})",
        "exemple": "0, 42, 1000"
    },
    
    "entier_positif": {
        "description": "Nombre entier strictement positif (ℕ* = {1, 2, 3, ...})",
        "exemple": "1, 99"
    },
    
    "entier_negatif": {
        "description": "Nombre entier strictement négatif (ℤ- = {-1, -2, -3, ...})",
        "exemple": "-5, -100"
    },
    
    "entier_relatif": {
        "description": "Nombre entier positif ou négatif (ℤ = {..., -2, -1, 0, 1, 2, ...})",
        "exemple": "-3, 0, 7"
    },
    
    "nombre_decimal": {
        "description": "Nombre rationnel pouvant s'écrire avec un nombre fini de chiffres après la virgule",
        "exemple": "3.14, -0.5",
        "attention": "1/3 = 0.333... n'est pas décimal"
    },
    
    "rationnel": {
        "description": "Nombre pouvant s'exprimer comme fraction a/b où a et b sont entiers (ℚ)",
        "exemple": "1/2, -4/3, 0.75 (=3/4)"
    },
    
    "irrationnel": {
        "description": "Nombre réel qui n'est pas rationnel (ne peut pas s'écrire comme fraction simple)",
        "exemple": "√2, π, e"
    },
    
    "reel": {
        "description": "Tous les nombres rationnels et irrationnels (ℝ)",
        "exemple": "-5, 3.14, √2"
    },
    
    "imaginaire_pur": {
        "description": "Nombre complexe sans partie réelle (de la forme bi où b ≠ 0)",
        "exemple": "2i, -3.5i"
    },
    
    "complexe": {
        "description": "Nombre de la forme a + bi où a et b sont réels (ℂ)",
        "exemple": "3+4i, -1.5-2i"
    },
    
    # Propriétés arithmétiques
    "est_pair": {
        "description": "Nombre divisible par 2",
        "methode": "n % 2 == 0",
        "exemple": "4 → vrai, 7 → faux"
    },
    
    "est_premier": {
        "description": "Nombre ayant exactement deux diviseurs distincts : 1 et lui-même",
        "methode": "Test de divisibilité de 2 à √n",
        "exemple": "7 → vrai (diviseurs: 1,7), 6 → faux (1,2,3,6)"
    },
    
    "binaire": {
        "description": "Représentation du nombre en base 2 (système binaire)",
        "methode": "Conversion via bin() puis suppression du préfixe '0b'",
        "exemple": "5 → '101'"
    },
    
    "hexadecimal": {
        "description": "Représentation du nombre en base 16 (système hexadécimal)",
        "methode": "Conversion via hex() puis suppression du préfixe '0x'",
        "exemple": "255 → 'ff'"
    },
    
    "racine_carree": {
        "description": "Nombre qui multiplié par lui-même donne le nombre original (√n)",
        "methode": "math.sqrt() arrondi à 4 décimales",
        "attention": "Définie seulement pour n ≥ 0"
    },
    
    "diviseurs": {
        "description": "Liste de tous les entiers qui divisent n sans reste",
        "methode": "Test de divisibilité de 1 à n",
        "exemple": "6 → [1,2,3,6]"
    },
    
    "est_fibonacci": {
        "description": "Nombre appartenant à la suite de Fibonacci (0,1,1,2,3,5,8,...)",
        "methode": "Test via identité : 5n²±4 doit être un carré parfait",
        "exemple": "8 → vrai, 9 → faux"
    },
    
    "chiffre_romain": {
        "description": "Numération romaine utilisant les symboles I,V,X,L,C,D,M",
        "regles": [
            "Addition si valeur supérieure ou égale : VI = 6",
            "Soustraction si valeur inférieure : IV = 4"
        ],
        "valeurs": {
            "I":1, "V":5, "X":10, "L":50, 
            "C":100, "D":500, "M":1000
        }
    },
    
    "somme_chiffres": {
        "description": "Somme de tous les chiffres composant le nombre",
        "methode": "Conversion en chaîne puis somme des chiffres convertis en int",
        "exemple": "123 → 1+2+3 = 6"
    },
    
    "est_carre_parfait": {
        "description": "Nombre qui est le carré d'un entier (n = k²)",
        "methode": "Vérifie si √n est entier",
        "exemple": "9 → vrai (3²), 10 → faux"
    },
    
    "est_cube_parfait": {
        "description": "Nombre qui est le cube d'un entier (n = k³)",
        "methode": "Vérifie si ∛n est entier",
        "exemple": "8 → vrai (2³), 9 → faux"
    },
    
    "log_base10": {
        "description": "Logarithme décimal (puissance à laquelle 10 doit être élevé pour obtenir n)",
        "attention": "Défini seulement pour n > 0",
        "exemple": "100 → 2 (car 10² = 100)"
    },
    
    "puissance_de_deux": {
        "description": "Nombre qui peut s'écrire sous la forme 2^k",
        "methode": "Vérification via opération bit à bit : n & (n-1) == 0",
        "exemple": "8 → vrai (2³), 6 → faux"
    },
    
    "nombre_chiffres": {
        "description": "Quantité de chiffres dans l'écriture décimale du nombre",
        "methode": "Conversion en chaîne puis calcul de la longueur",
        "exemple": "-123 → 3 chiffres"
    },
    
    "est_abondant": {
        "description": "Nombre dont la somme des diviseurs propres est supérieure à lui-même",
        "diviseurs_propres": "Tous les diviseurs sauf le nombre lui-même",
        "exemple": "12 → vrai (1+2+3+4+6 = 16 > 12)"
    },
    
    "est_palindrome": {
        "description": "Nombre qui se lit identiquement de gauche à droite et de droite à gauche",
        "methode": "Comparaison avec sa version inversée",
        "exemple": "12321 → vrai, 123 → faux"
    },
    
    "factorisation_premiers": {
        "description": "Décomposition en produit de nombres premiers",
        "methode": "Division successive par les nombres premiers",
        "exemple": "84 → [2, 2, 3, 7] (2²×3×7)"
    },
    
    "cosinus": {
        "description": "Cosinus de l'angle (en radians) correspondant au nombre",
        "attention": "Le nombre est interprété comme un angle en radians",
        "exemple": "math.pi → -1 (car cos(π) = -1)"
    },
    
    "sinus": {
        "description": "Sinus de l'angle (en radians) correspondant au nombre",
        "exemple": "math.pi/2 → 1 (car sin(π/2) = 1)"
    }
}