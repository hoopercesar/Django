from django import forms

class CreateNewTask(): 
    title = forms.CharField(label='titulo tarea', max_length=200)
    description = forms.Textarea(label='decripción tarea', required=False)