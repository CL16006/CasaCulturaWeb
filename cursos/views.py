from django.shortcuts import render
from django.contrib import admin

from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import anuncio, inscripcion, cursos
from .forms import inscripcionForm

#Esta vista sirve para poder
def index(request):
    anuncios=anuncio.objects.order_by('fecha_publicacion')[:]
    template = loader.get_template('cursos/index.html')
    context = {
        'anuncios_list': anuncios,
    }
    return HttpResponse(template.render(context, request))

'''
Esta vista sirve para poder definir el template al que ira conectada la vista home,
se hace una consulta a la base de datos donde se obtienen todos los anuncios registrados ordenados por fecha de publicacion
luego se pasan los datos al contexto para poder ser utilizados en la vista.
'''
def home(request):
    anuncios=anuncio.objects.order_by('fecha_publicacion')[:]
    template = loader.get_template('cursos/home.html')
    context = {
        'anuncios_list': anuncios,
    }
    return HttpResponse(template.render(context, request))

'''
Esta vista sirve para poder definir el template al que ira conectada la vista verCursos,
se hace una consulta a la base de datos donde se obtienen todos los cursos registrados ordenados por nombre
luego se pasan los datos al contexto para poder ser utilizados en la vista.
'''
def verCursos(request):
    lista_cursos=cursos.objects.order_by('nombre')[:]
    template = loader.get_template('cursos/cursos.html')
    context = {
        'cursos_list': lista_cursos,
    }
    return  HttpResponse(template.render(context, request))

#Esta vista sirve para definir el template al que ira enlazada la vista inscribirse
def inscribirse(request):

    template = loader.get_template('cursos/inscribirse.html')
    context = {}
    return HttpResponse(template.render(context, request))


#Esta vista sirve para definir el template al que ira enlazada la vista contacto
def contacto(request):

    template = loader.get_template('cursos/contacto.html')
    context = {}
     
    return HttpResponse(template.render(context, request))
    
#Esta vista sirve para definir el template al que ira enlazada la vista quienes somos
def quienesSomos(request):

    template = loader.get_template('cursos/quienesSomos.html')
    context = {}
    return HttpResponse(template.render(context, request))

#Esta vista sirve para definir el template para la vista admin
def admin(request):
    template = loader.get_template('cursos/administrar.html')
    context = {}
    return HttpResponse(template.render(context, request))

#Esta clase se crea con el fin de poder crear un formulario a partir del modelo inscripcion automaticamente y mostrarlo en una vista.
class FormularioInscripcionView(HttpRequest):

    def index(request):
        inscripcion = inscripcionForm
        context = {
            'form': inscripcion
        }
        return render(request,'cursos/inscripcion.html',context)

    def procesar_formulario(request):
        inscripcion = inscripcionForm(request.POST)
        if inscripcion.is_valid():
            inscripcion.save()
            inscripcion = inscripcionForm
        return  render(request,'cursos/inscripcion.html',{'form':inscripcion,'mensaje':'OK'})