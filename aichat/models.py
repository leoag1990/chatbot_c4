from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class DatosUsuarios(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')

class ChatMensaje(models.Model):
    user = models.ForeignKey(DatosUsuarios, on_delete=models.CASCADE)
    mensaje = models.TextField()
    respuesta = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
