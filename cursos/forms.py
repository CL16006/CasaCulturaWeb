from django.forms import ModelForm
from .models import inscripcion

#Es este archivo se configuran los formularios que seran creados a partir de un modelo

#Este es la configuracion para un formulario del modelo inscripcion
class inscripcionForm(ModelForm):
    class Meta:
        model = inscripcion
        fields = '__all__'
