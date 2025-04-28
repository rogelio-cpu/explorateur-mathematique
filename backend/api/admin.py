from django.contrib import admin
from .models import HistoriqueCalcul

@admin.register(HistoriqueCalcul)
class HistoriqueCalculAdmin(admin.ModelAdmin):
    """
    Configuration de l'administration Django pour le modèle HistoriqueCalcul.
    """
    list_display = ('nombre', 'date_calcul', 'est_pair', 'est_premier', 'chiffre_romain')
    list_filter = ('est_pair', 'est_premier', 'est_palindrome', 'date_calcul')
    search_fields = ('nombre',)
    readonly_fields = ('date_calcul',)
    fieldsets = (
        ('Informations de base', {
            'fields': ('nombre', 'date_calcul')
        }),
        ('Propriétés booléennes', {
            'fields': ('est_pair', 'est_premier', 'est_fibonacci', 'est_carre_parfait', 
                      'est_cube_parfait', 'puissance_de_deux', 'est_abondant', 'est_palindrome')
        }),
        ('Représentations', {
            'fields': ('binaire', 'hexadecimal', 'chiffre_romain')
        }),
        ('Calculs', {
            'fields': ('racine_carree', 'diviseurs', 'somme_chiffres', 'log_base10', 
                      'nombre_chiffres', 'factorisation_premiers')
        }),
    )
