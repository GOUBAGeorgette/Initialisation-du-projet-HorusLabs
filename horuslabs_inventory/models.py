from django.db import models

class Equipement(models.Model):
    CATEGORIES = [
        ('Drones', 'Drones'),
        ('Robots', 'Robots'),
        ('Informatique', 'Informatique'),
        ('Électronique', 'Électronique'),
        ('Maintenance', 'Maintenance'),
        ('Divertissement', 'Divertissement'),
        ('Actionneurs', 'Actionneurs'),
        ('Accessoires', 'Accessoires'),
        ('Composants', 'Composants'),
        ('Stockage', 'Stockage'),
        ('Écrans et affichage', 'Écrans et affichage'),
        ('Modules de communication', 'Modules de communication'),
        ('Capteurs', 'Capteurs'),
        ('Cartes mémoire et stockage', 'Cartes mémoire et stockage'),
    ]

    categorie = models.CharField(max_length=50, choices=CATEGORIES, default='Drones')
    nom = models.CharField(max_length=100)
    marque_modele = models.CharField(max_length=100, blank=True)
    type = models.CharField(max_length=100, blank=True)
    quantite = models.PositiveIntegerField()
    etat = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=200, blank=True)
    utilisabilite = models.CharField(max_length=100, blank=True)
    responsable = models.CharField(max_length=100, blank=True)
    remarque = models.TextField(blank=True)
    suggestion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nom} ({self.categorie})"
