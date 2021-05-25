from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import anuncio

def index(request):
    anuncios=anuncio.objects.order_by('fecha_publicacion')[:]
    template = loader.get_template('cursos/index.html')
    context = {
        'anuncios_list': anuncios,
    }
    return HttpResponse(template.render(context, request))
#yami
def home(request):

    return HttpResponse("inicio")
#fatima
def cursos(request):

    return  HttpResponse("cursos")
#alberto
def inscribirse(request):

    return HttpResponse("Inscribirse")
#yami
def contacto(request):

    return HttpResponse("Contacto")
#yesica
def quienesSomos(request):

    return HttpResponse("quienes somos")

