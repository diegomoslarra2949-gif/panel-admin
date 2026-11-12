from django.shortcuts import render
from .models import Noticia


def lista_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, "noticias.html", {"noticias": noticias})