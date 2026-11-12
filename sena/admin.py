from django.contrib import admin
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha", "lugar")
    list_filter = ("fecha", "lugar")
    search_fields = ("titulo", "lugar", "descripcion")
    date_hierarchy = "fecha"