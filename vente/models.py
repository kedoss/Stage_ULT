from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
class category(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=31)

    def __str__(self):
        return self.nom
"""

class produit(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length = 31)
    unite = models.CharField(max_length = 31)
    quantite = models.FloatField(editable = False, null = True)
    prix_vente = models.FloatField()
    #category = models.ForeignKey(category, null=True, on_delete=models.SET_NULL)
    prix_vente = models.FloatField()

    def __str__(self):
        return f"{self.nom} igurishwa {self.prix_vente}"
    
class stock(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    produit = models.ForeignKey(produit, on_delete = models.CASCADE)
    quantite_initiale = models.FloatField(editable=False, null=True)
    quantite_actuelle = models.FloatField(editable=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delais_expiration = models.PositiveBigIntegerField()
    prix_achat = models.FloatField()

class commande(models.Model): 
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    prix_total = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=63)

class ProduitCommande(models.Model):
    id = models.BigAutoField(primary_key=True)
    produit = models.ForeignKey(produit, on_delete=models.PROTECT)
    commande = models.ForeignKey(commande, on_delete=models.CASCADE)
    quantite = models.FloatField()
    prix = models.FloatField()

class Paiement(models.Model):
    id = models.AutoField(primary_key=True)
    montant = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    commande = models.ForeignKey(commande, on_delete=models.CASCADE)