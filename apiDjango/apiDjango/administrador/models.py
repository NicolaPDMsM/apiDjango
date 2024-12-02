from django.db import models

class Usuario(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=60)
    estado=models.IntegerField()
    fecha_hora=models.DateField()