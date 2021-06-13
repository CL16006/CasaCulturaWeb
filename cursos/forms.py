from django.forms import ModelForm
from .models import inscripcion

class inscripcionForm(ModelForm):
    class Meta:
        model = inscripcion
        fields = '__all__'
