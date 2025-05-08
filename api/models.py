from django.db import models

# Create your models here.

class Nombre(models.Model):
    ENSEMBLE_CHOICES = [
        ('chiffre_arabe', 'Chiffre Arabe'),
        ('nombre_arabe', 'Nombre Arabe'),
        ('entier_naturel', 'Entier Naturel'),
        ('entier_naturel_negatif', 'Entier Naturel Négatif'),
        ('entier_relatif', 'Entier Relatif'),
        ('decimal_fini', 'Décimal Fini'),
        ('fraction_rationnelle', 'Fraction Rationnelle'),
        ('nombre_rationnel', 'Nombre Rationnel'),
        ('irrationnel_connu', 'Irrationnel Connu'),
        ('reel', 'Réel'),
        ('imaginaire_pur', 'Imaginaire Pur'),
        ('complexe', 'Complexe'),
    ]
    valeur = models.CharField(max_length=255)
    ensemble = models.CharField(max_length=32, choices=ENSEMBLE_CHOICES)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.valeur} ({self.get_ensemble_display()})"
