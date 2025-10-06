import pandas as pd
from horuslabs_inventory.models import Equipement

def nettoyer_unicode(valeur, max_length=100):
    if pd.isna(valeur):
        return ""
    return str(valeur).strip()[:max_length]

def importer_equipements_depuis_excel(fichier):
    df = pd.read_excel(fichier)

    for _, row in df.iterrows():
        Equipement.objects.create(
            categorie=nettoyer_unicode(row['Catégorie'], 50),
            nom=nettoyer_unicode(row['Nom'], 100),
            marque_modele=nettoyer_unicode(row['Marque/ Modèle'], 100),
            type=nettoyer_unicode(row['Type'], 100),
            quantite=int(row['Quantité']) if not pd.isna(row['Quantité']) else 0,
            etat=nettoyer_unicode(row['Etat'], 100),
            emplacement=nettoyer_unicode(row['Emplacement'], 200),
            utilisabilite=nettoyer_unicode(row['Utilisabilité'], 100),
            responsable=nettoyer_unicode(row['Personne en charge du matériel'], 100),
            remarque=nettoyer_unicode(row['Remarque'], 1000),
            suggestion=nettoyer_unicode(row['Suggestions'], 1000),
        )
    print("✅ Importation terminée avec succès.")