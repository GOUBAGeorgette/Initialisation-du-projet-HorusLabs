from django.contrib import admin
from .models import Equipement

@admin.register(Equipement)
class EquipementAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie', 'quantite', 'etat', 'responsable']
    list_filter = ['categorie', 'etat']
    search_fields = ['nom', 'responsable', 'remarque', 'suggestion']
