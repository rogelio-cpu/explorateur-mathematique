from django.utils.translation import gettext_lazy as _
from .en import DESCRIPTIONS_EN
from .fr import DESCRIPTIONS_FR

# Dictionnaire global
DESCRIPTIONS = {
    "fr": DESCRIPTIONS_FR,
    "en": DESCRIPTIONS_EN,
}

# Messages génériques de l’API
API_MESSAGES = {
    'error_messages': {
        'number_required': _('parametre_nombre_requis'),
        'calculation_error': _('erreur_calcul'),
    },
    'response_keys': {
        'original_expression': _('expression_originale'),
        'calculated_value': _('valeur_calculee'),
        'analysis': _('analyse'),
    }
}

def get_descriptions(language: str = 'en'):
    """
    Retourne les descriptions dans la langue spécifiée.
    Retombe toujours sur l'anglais si la langue demandée n'existe pas.
    """
    return DESCRIPTIONS.get(language, DESCRIPTIONS_EN)
