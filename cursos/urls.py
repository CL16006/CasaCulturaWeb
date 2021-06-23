from django.urls import path

from . import views

'''
En este archivo se definen las urls que se usaran en la aplicacion,
esto se hace creando una lista llamada urlpatterns, y se van agregando los path, primero se le agrega la url en que se mostrara,
luego se hubica la vista a la que ira asociada, y finalmente se le coloca un nombre.
'''

urlpatterns = [
    path('', views.home, name='home'),
    path('index',views.index,name='index'),
    path('verCursos',views.verCursos,name='verCursos'),
    path('contacto',views.contacto,name='contacto'),
    path('inscribirse',views.inscribirse,name='inscribirse'),
    path('quienesSomos',views.quienesSomos,name='quienesSomos'),
    path('administrar',views.admin,name='administrar'),
    path('inscripcion',views.FormularioInscripcionView.index, name='inscripcion'),
    path('guardarInscripcion',views.FormularioInscripcionView.procesar_formulario,name='guardarInscripcion')
    ]