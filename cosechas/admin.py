from django.contrib import admin
from .models import Cultivo, Cosecha


@admin.register(Cultivo)
class CultivoAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre")
	search_fields = ("nombre",)


@admin.register(Cosecha)
class CosechaAdmin(admin.ModelAdmin):
	list_display = ("id", "nombre", "cultivo", "fecha_cosecha", "cantidad")
	list_filter = ("cultivo", "fecha_cosecha")
	search_fields = ("nombre", "descripcion")
