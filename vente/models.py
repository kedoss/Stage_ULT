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

    def __str__(self):
        return f"{self.nom} ugurishwa {self.prix_vente}"
    
class stock(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, editable=False)
    produit = models.ForeignKey(produit, on_delete = models.CASCADE)
    quantite_initiale = models.FloatField(default=0)
    quantite_actuelle = models.FloatField(editable=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    delais_expiration = models.PositiveBigIntegerField(null=True, blank=True)
    prix_achat = models.FloatField()

    def __str__(self) -> str:
        return f"{self.quantite_initiale} {self.produit.unite} de {self.produit}"

class commande(models.Model): 
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)#editable=True
    prix_total = models.FloatField(editable=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=63, null=True)
    done = models.BooleanField(default=False, editable=False)#editable=True

    def __str__(self) -> str:
        return f"Commande de {self.client} valant {self.prix_total}"

class ProduitCommande(models.Model):
    id = models.BigAutoField(primary_key=True)
    produit = models.ForeignKey(produit, on_delete=models.PROTECT)
    commande = models.ForeignKey(commande, on_delete=models.CASCADE, editable=False)
    quantite = models.FloatField()
    prix = models.FloatField(editable=False)

    def __str__(self) -> str:
        return f"{self.quantite} {self.produit.unite} de {self.produit}"
    
    class Meta:
        verbose_name = "Panier"
        verbose_name_plural = "Panier"

class Paiement(models.Model):
    id = models.AutoField(primary_key=True)
    montant = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    commande = models.ForeignKey(commande, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.montant} sur {self.commande} à {self.created_by}"