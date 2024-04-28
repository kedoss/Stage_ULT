from django.contrib import admin,messages
from .models import*
from typing import Any
# Register your models here.
#admin.site.register(category)
@admin.register(produit)
class produitAdmin(admin.ModelAdmin) :
    list_display = "nom", "unite", "quantite", "prix_vente"

@admin.register(stock)
class stockAdmin(admin.ModelAdmin) :
       list_display = "created_by", "produit", "quantite_initiale", "quantite_actuelle"

       def save_model(self, request, obj: stock, form, change) -> None:
        if change:
            messages.add_message(request, messages.ERROR, "modification ntikunda")
            return
        produit = obj.produit
        try:
            produit.quantite += obj.quantite_initiale
        except Exception:
            produit.quantite = obj.quantite_initiale
        produit.save()
        obj.quantite_actuelle = obj.quantite_initiale
        return super().save_model(request, obj, form, change)


@admin.register(commande)
class commandeAdmin(admin.ModelAdmin) :
    list_display =  "created_by", "prix_total", "created_at","client"


@admin.register(ProduitCommande)
class ProduitCommandeAdmin(admin.ModelAdmin) :
    list_display = "produit", "commande", "quantite", "prix"

    def save_model(self, request, obj:ProduitCommande, form, change):
        if change:
            messages.add_message(request, messages.ERROR, "modification ntikunda")
            return
        commande = commande.objects.filter(done=False).first()
        if not commande:
            # commande = INSERT INTO Commande(created_by) VALUES (request.user)
            commande = commande.objects.create(created_by = request.user)
            obj.commande = commande
            obj.prix = obj.produit.prix * obj.quantite
            commande.prix_total += obj.prix
            commande.save()
            return super().save_model(request, obj, form, change)


@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin) :
    list_display = "montant", "created_by", "created_at", "commande"