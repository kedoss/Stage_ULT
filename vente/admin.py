from django.contrib import admin,messages
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.safestring import mark_safe
from .models import*
from .models import ProduitCommande
# Register your models here.
#admin.site.register(category)
admin.site.site_header = "KIOSK ULT"

@admin.register(produit)
class produitAdmin(admin.ModelAdmin) :
    list_display = "nom", "unite", "quantite", "prix_vente", "options"
    search_fields = "nom",

    def options(self, obj:produit):
        return mark_safe(f"<a href='/admin/vente/stock/?produit__id__exact={obj.id}'>Voir Stock</a>")

@admin.register(stock)
class stockAdmin(admin.ModelAdmin) :
       list_display = "produit", "created_by", "quantite_initiale", "quantite_actuelle",

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
        obj.created_by = request.user
        return super().save_model(request, obj, form, change)
       
       
        def delete_model(self, request, obj:stock):
            produit = obj.produit
            produit.quantite -= obj.quantite_actuelle
            produit.save()
            return super().delete_model(request, obj)
        
        def delete_queryset(self, request, queryset: QuerySet[stock]):
            for obj in queryset:
                produit = obj.produit
                produit.quantite -= obj.quantite_actuelle
                produit.save()
            super().delete_queryset(request, queryset)


@admin.register(commande)
class commandeAdmin(admin.ModelAdmin) :
    list_display =  "created_by", "prix_total", "created_at","client"


@admin.register(ProduitCommande)
class ProduitCommandeAdmin(admin.ModelAdmin) :
    list_display = ("produit", "commande", "quantite", "prix")
    list_filter = ("produit",)
    

    def save_model(self, request, obj:ProduitCommande, form, change):
        if change:
            messages.add_message(request, messages.ERROR, "modification ntikunda")
            return
        produit = obj.produit
        if obj.quantite > (produit.quantite or 0):
            messages.add_message(request, messages.ERROR, f"{produit} hasigaye {produit.quantite or 0} {produit.unite} gusa")
            return
        
        commande_instance  = commande.objects.filter(done=False).first()
        if not commande_instance :
            # commande = INSERT INTO Commande(created_by) VALUES (request.user)
            commande_instance  = commande.objects.create(created_by = request.user)
            obj.commande = commande_instance 
            obj.prix = obj.produit.prix_vente * obj.quantite
            commande_instance .prix_total += obj.prix
            commande_instance .save()
            return super().save_model(request, obj, form, change)
        
    def delete_model(self, request, obj:ProduitCommande) -> None:
        commande_instance  = obj.commande
        commande_instance .prix_total -= obj.prix
        commande_instance .save()
        return super().delete_model(request, obj)
    
    def delete_queryset(self, request, queryset: QuerySet[ProduitCommande]) -> None:
        for obj in queryset:
            commande_instance  = obj.commande
            commande_instance .prix_total -= obj.prix
            commande_instance .save()
        return super().delete_queryset(request, queryset)


@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin) :
    list_display = "montant", "created_at", "created_by", "commande"