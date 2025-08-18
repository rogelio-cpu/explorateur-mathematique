from django.db import models

# Create your models here.

class Nombre(models.Model):
    ENSEMBLE_CHOICES = [
        ('chiffre_arabe', 'Chiffre Arabe'),
        ('entier_naturel', 'Entier Naturel'),
        ('entier_negatif', 'Entier Négatif'),
        ('entier_relatif', 'Entier Relatif'),
        ('nombre_decimal', 'Nombre Décimal'),
        ('rationnel', 'Rationnel'),
        ('irrationnel', 'Irrationnel'),
        ('reel', 'Réel'),
        ('imaginaire_pur', 'Imaginaire Pur'),
        ('complexe', 'Complexe'),
    ]
    valeur = models.CharField(max_length=255)
    ensemble = models.CharField(max_length=32, choices=ENSEMBLE_CHOICES)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.valeur} ({self.get_ensemble_display()})"
