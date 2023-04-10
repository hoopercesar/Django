from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    # usamos el algunos de los inputs del formulario creado en models
    # en este caso, sólo 3 de los inputs para ingresarlos por frontend
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        