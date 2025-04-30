from django.db import models

# Create your models here.

class HistoriqueCalcul(models.Model):
    """
    Modèle pour stocker l'historique des calculs effectués sur des nombres.
    """
    nombre = models.IntegerField()
    date_calcul = models.DateTimeField(auto_now_add=True)
    
    # Résultats des calculs (stockés en JSON)
    chiffre_arabe=models.BooleanField()
    entier_naturel=models.BooleanField()
    entier_positif=models.BooleanField()
    entier_negatif=models.BooleanField()
    entier_relatif=models.BooleanField()
    nombre_decimal=models.BooleanField()
    rationnel=models.BooleanField()
    irrationnel=models.BooleanField()
    reel=models.BooleanField()
    imaginaire_pur=models.BooleanField()
    complexe=models.BooleanField()
    est_pair = models.BooleanField()
    est_premier = models.BooleanField()
    binaire = models.CharField(max_length=100)
    hexadecimal = models.CharField(max_length=100)
    racine_carree = models.FloatField(null=True)
    diviseurs = models.JSONField()
    est_fibonacci = models.BooleanField()
    chiffre_romain = models.CharField(max_length=50)
    somme_chiffres = models.IntegerField()
    est_carre_parfait = models.BooleanField()
    est_cube_parfait = models.BooleanField()
    log_base10 = models.FloatField(null=True)
    puissance_de_deux = models.BooleanField()
    nombre_chiffres = models.IntegerField()
    est_abondant = models.BooleanField()
    est_palindrome = models.BooleanField()
    factorisation_premiers = models.JSONField()
    
    def __str__(self):
        return f"Calcul pour {self.nombre} effectué le {self.date_calcul}"
    
    class Meta:
        verbose_name = "Historique de calcul"
        verbose_name_plural = "Historiques de calculs"
        ordering = ['-date_calcul']
