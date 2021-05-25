from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index',views.index,name='index'),
    path('cursos',views.cursos,name='cursos'),
    path('contacto',views.contacto,name='contacto'),
    path('inscribirse',views.inscribirse,name='inscribirse'),
    path('quienesSomos',views.quienesSomos,name='quienesSomos')
    ]