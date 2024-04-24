from django.contrib import admin
from .models import*
# Register your models here.
#admin.site.register(category)
admin.site.register(produit)
admin.site.register(stock)
admin.site.register(commande)
admin.site.register(ProduitCommande)
admin.site.register(Paiement)