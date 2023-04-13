from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# con ésto se crea un modelo para una tabla en la base de datos
# datecompleted: null=True es un dato que se va a llenar cuando se complete
# user: se importó User. al usarlo de argumento queda asociada la tabla
# al usuario que la creó a través de un índice. models.CASCADE elimina
# toda la imformación del usuario cuando éste se da de baja. Se eliminan
# todas sus tablas en cascada
# para crear tabla en DB: > python manage.py makemigrations
# y luego: > python manage.py migrate
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' by ' + self.user.username
