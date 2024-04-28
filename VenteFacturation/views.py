#from django.http import HttpResponse
from django.shortcuts import render
"""
def index(request):
    nom = request.GET.get("nom")
    prenom = request.GET.get("prenom")
    return HttpResponse(f"<h1>HARABABA {nom} {prenom}</h1>")
"""
"""
def index(request):
    a=int(request.GET.get("a", 0))
    b = int(request.GET.get("b", 0))
    c=int(request.GET.get("c", 0))
    kinini=max([a], [b],[c])
    return HttpResponse(f"<h1>mu biharuro vyose wanditse kinini ni <strong>{kinini}</strong></h1>")
"""

"""
def index(request, a, b, c):
    kinini = max([int(a), int(b), int(c)])
    return HttpResponse(f"<h1>mu biharuro vyose wanditse kinini ni <strong>{kinini}</strong></h1>")
"""


"""
def index(request, a, b):
    a=int(request.GET.get("a", 0))
    b = int(request.GET.get("b", 0))
    somme = a+b
    #return render(request, "index.html", locals())
    return render(request, "index.html", {"La somme est":somme})
"""


def index(request, a, b):
    return render(request, "index.html", locals())