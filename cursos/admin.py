from django.contrib import admin
from .models import cursos, anuncio,inscripcion

'''
En este archivo se configuran la propiedades para el panel de administracion,
y se agregan los modelos para poder ser administrados desde el panel de administracion
'''

#Esta clase sirve para poder configurar la propiedades para el modelo curso que se muestran en el panel de administracion
class CursoAdmin(admin.ModelAdmin):
    list_display = ["nombre","descripcion","fecha_inicio","fecha_fin"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]

#Esta clase sirve para poder configurar las propiedades para el modelo anuncio que se muestra en el panel de administracion.
class AnuncioAdmin(admin.ModelAdmin):
    list_display = ["encabezado","texto","fecha_publicacion"]
    search_fields = ["encabezado"]
    list_filter = ["encabezado"]

#Esta clase sirve para poder configurar las propiedades para el modelo inscripcion en el panel de aadministracion.
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ["nombres","apellidos","telefono","email"]
    search_fields = ["nombres"]

#Con la siguientes instrunciones agregamos los modelos al panel administrativo asi como su configuracion.
admin.site.register(cursos,CursoAdmin)
admin.site.register(anuncio, AnuncioAdmin)
admin.site.register(inscripcion, InscripcionAdmin)