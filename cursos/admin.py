from django.contrib import admin
from .models import cursos, anuncio,inscripcion

class CursoAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion","fecha_inicio","fecha_fin"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]
    
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ["encabezado","texto","fecha_publicacion"]
    search_fields = ["encabezado"]
    list_filter = ["encabezado"]
    
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ["nombres","apellidos","telefono","email"]
    search_fields = ["nombres"]


admin.site.register(cursos,CursoAdmin)
admin.site.register(anuncio, AnuncioAdmin)
admin.site.register(inscripcion, InscripcionAdmin)