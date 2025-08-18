DESCRIPTIONS_EN = {
    "chiffre_arabe": {
        "nom": "Arabic Numeral",
        "definition": "A = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}",
        "description": "An Arabic numeral is a basic symbol (0-9) used in the modern numerical system.",
        "example": "5, 7, 9",
        "true": "{nombre} ∈ A → It is a digit between 0 and 9",
        "false": "{nombre} ∉ A → Not a valid digit"
    },
    "entier_naturel": {
        "nom": "Natural Number",
        "definition": "ℕ = {0, 1, 2, 3, ...}",
        "description": "Non-negative integer (ℕ).",
        "example": "0, 42, 1000",
        "true": "{nombre} ∈ ℕ",
        "false": "{nombre} ∉ ℕ"
    },
    "entier_positif": {
        "nom": "Strictly Positive Integer",
        "definition": "ℕ* = {1, 2, 3, ...}",
        "description": "Strictly positive integer.",
        "example": "1, 99",
        "true": "{nombre} ∈ ℕ*",
        "false": "{nombre} ∉ ℕ*"
    },
    "entier_negatif": {
        "nom": "Strictly Negative Integer",
        "definition": "ℤ⁻ = {-1, -2, -3, ...}",
        "description": "Strictly negative integer.",
        "example": "-5, -100",
        "true": "{nombre} ∈ ℤ⁻",
        "false": "{nombre} ∉ ℤ⁻"
    },
    "entier_relatif": {
        "nom": "Integer",
        "definition": "ℤ = {..., -2, -1, 0, 1, 2, ...}",
        "description": "Positive or negative integer.",
        "example": "-3, 0, 7",
        "true": "{nombre} ∈ ℤ",
        "false": "{nombre} ∉ ℤ"
    },
    "nombre_decimal": {
        "nom": "Decimal Number",
        "definition": "Number with a finite number of digits after the decimal point",
        "description": "Rational number with a finite number of decimals.",
        "example": "3.14, -0.5",
        "attention": "1/3 = 0.333... is not a finite decimal",
        "true": "{nombre} is a finite decimal number",
        "false": "{nombre} is not a finite decimal number"
    },
    "rationnel": {
        "nom": "Rational Number",
        "definition": "ℚ = {a/b | a, b ∈ ℤ, b ≠ 0}",
        "description": "Number that can be expressed as a fraction of integers.",
        "example": "1/2, -4/3, 0.75",
        "true": "{nombre} ∈ ℚ",
        "false": "{nombre} ∉ ℚ"
    },
    "irrationnel": {
        "nom": "Irrational Number",
        "definition": "ℝ \\ ℚ",
        "description": "Real number that is not rational.",
        "example": "√2, π, e",
        "true": "{nombre} is irrational",
        "false": "{nombre} is not irrational"
    },
    "reel": {
        "nom": "Real Number",
        "definition": "ℝ = ℚ ∪ Irrationals",
        "description": "Set of rational and irrational numbers.",
        "example": "-5, 3.14, √2",
        "true": "{nombre} ∈ ℝ",
        "false": "{nombre} ∉ ℝ"
    },
    "imaginaire_pur": {
        "nom": "Pure Imaginary",
        "definition": "iℝ = {bi | b ∈ ℝ}",
        "description": "Complex number without real part (of the form bi).",
        "example": "2i, -3.5i",
        "true": "{nombre} ∈ iℝ",
        "false": "{nombre} ∉ iℝ"
    },
    "complexe": {
        "nom": "Complex Number",
        "definition": "ℂ = {a + bi | a, b ∈ ℝ}",
        "description": "Number of the form a + bi where a and b are real.",
        "example": "3+4i, -1.5-2i",
        "true": "{nombre} ∈ ℂ",
        "false": "{nombre} ∉ ℂ"
    },
    # Properties and operations
    "est_pair": {
        "nom": "Even Number",
        "description": "Number divisible by 2",
        "methode": "n % 2 == 0",
        "example": "4 → true, 7 → false",
        "true": "{nombre} is even",
        "false": "{nombre} is odd"
    },
    "est_premier": {
        "nom": "Prime Number",
        "description": "Number with exactly two distinct divisors: 1 and itself",
        "methode": "Check divisibility from 2 to √n",
        "example": "7 → true, 6 → false",
        "true": "{nombre} is prime",
        "false": "{nombre} is not prime"
    },
    "binaire": {
        "nom": "Binary Representation",
        "description": "Number in base 2",
        "methode": "Convert via bin() and remove '0b' prefix",
        "example": "5 → '101'"
    },
    "hexadecimal": {
        "nom": "Hexadecimal Representation",
        "description": "Number in base 16",
        "methode": "Convert via hex() and remove '0x' prefix",
        "example": "255 → 'ff'"
    },
    "racine_carree": {
        "nom": "Square Root",
        "description": "Number that multiplied by itself gives the original number",
        "methode": "math.sqrt(), round to 4 decimals",
        "attention": "Defined only for n ≥ 0",
        "true": "√{nombre} exists",
        "false": "√{nombre} does not exist"
    },
    "diviseurs": {
        "nom": "Divisors",
        "description": "List of all integers dividing n without remainder",
        "methode": "Check divisibility from 1 to n",
        "example": "6 → [1,2,3,6]"
    },
    "est_fibonacci": {
        "nom": "Fibonacci Number",
        "description": "Number belonging to the Fibonacci sequence (0,1,1,2,3,5,...)",
        "methode": "Check if 5*n^2 ± 4 is a perfect square",
        "example": "8 → true, 9 → false",
        "true": "{nombre} is a Fibonacci number",
        "false": "{nombre} is not a Fibonacci number"
    },
    "chiffre_romain": {
        "nom": "Roman Numeral",
        "description": "Roman numeral using symbols I, V, X, L, C, D, M",
        "regles": [
            "Addition if higher or equal value: VI = 6",
            "Subtraction if lower value: IV = 4"
        ],
        "valeurs": {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    },
    "somme_chiffres": {
        "nom": "Sum of Digits",
        "description": "Sum of all digits composing the number",
        "methode": "Convert to string, then sum digits as int",
        "example": "123 → 6"
    },
    "est_carre_parfait": {
        "nom": "Perfect Square",
        "description": "Number that is the square of an integer",
        "methode": "Check if √n is integer",
        "example": "9 → true, 10 → false"
    },
    "est_cube_parfait": {
        "nom": "Perfect Cube",
        "description": "Number that is the cube of an integer",
        "methode": "Check if ∛n is integer",
        "example": "8 → true, 9 → false"
    },
    "log_base10": {
        "nom": "Base-10 Logarithm",
        "description": "Decimal logarithm (power to which 10 must be raised to get n)",
        "attention": "Defined only for n > 0",
        "example": "100 → 2"
    },
    "puissance_de_deux": {
        "nom": "Power of Two",
        "description": "Number that can be written as 2^k",
        "methode": "Check via bitwise: n & (n-1) == 0",
        "example": "8 → true, 6 → false"
    },
    "nombre_chiffres": {
        "nom": "Number of Digits",
        "description": "Number of digits in decimal representation",
        "methode": "Convert to string, then calculate length",
        "example": "-123 → 3 digits"
    },
    "est_abondant": {
        "nom": "Abundant Number",
        "description": "Number whose sum of proper divisors is greater than itself",
        "diviseurs_propres": "All divisors except the number itself",
        "example": "12 → true"
    },
    "est_palindrome": {
        "nom": "Palindrome Number",
        "description": "Number that reads identically forward and backward",
        "methode": "Compare with its reversed version",
        "example": "12321 → true, 123 → false"
    },
    "factorisation_premiers": {
        "nom": "Prime Factorization",
        "description": "Decomposition into product of prime numbers",
        "methode": "Divide successively by primes",
        "example": "84 → [2,2,3,7]"
    },
    "cosinus": {
        "nom": "Cosine",
        "description": "Cosine of the angle (in radians) corresponding to the number",
        "attention": "Number is interpreted as an angle in radians",
        "example": "math.pi → -1"
    },
    "sinus": {
        "nom": "Sine",
        "description": "Sine of the angle (in radians) corresponding to the number",
        "example": "math.pi/2 → 1"
    }
}
