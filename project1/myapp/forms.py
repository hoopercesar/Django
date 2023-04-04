from django import forms

class CreateNewTask(forms.Form): 
    title = forms.CharField(label='Titulo Tarea', max_length=200)
    description = forms.CharField(widget=forms.Textarea)