from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.template import loader
from .models import anuncio, inscripcion, cursos

def index(request):
    anuncios=anuncio.objects.order_by('fecha_publicacion')[:]
    template = loader.get_template('cursos/index.html')
    context = {
        'anuncios_list': anuncios,
    }
    return HttpResponse(template.render(context, request))
#yami
def home(request):
    anuncios=anuncio.objects.order_by('fecha_publicacion')[:]
    template = loader.get_template('cursos/home.html')
    context = {
        'anuncios_list': anuncios,
    }
    return HttpResponse(template.render(context, request))
#fatima
def verCursos(request):
    lista_cursos=cursos.objects.order_by('nombre')[:]
    template = loader.get_template('cursos/cursos.html')
    context = {
        'cursos_list': lista_cursos,
    }
    return  HttpResponse(template.render(context, request))
#alberto
def inscribirse(request):

    template = loader.get_template('cursos/inscribirse.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


#yami
def contacto(request):

    template = loader.get_template('cursos/contacto.html')
    context = {
        
    }
     
    return HttpResponse(template.render(context, request))
    
#yesica
def quienesSomos(request):

    template = loader.get_template('cursos/quienesSomos.html')
    context = {

      }
    return HttpResponse(template.render(context, request))

def admin(request):
    template = loader.get_template('cursos/administrar.html')
    context = {

    }
    return HttpResponse(template.render(context, request))