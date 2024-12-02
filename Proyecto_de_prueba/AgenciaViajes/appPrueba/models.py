from django.db import models

class Estado(models.Model):
    Id_estado = models.IntegerField(primary_key=True)

class Usuario(models.Model):
    Id_usuario = models.IntegerField(primary_key=True)
    User_name = models.CharField(max_length=60, null=True, blank=True)
    Contraseña = models.CharField(max_length=100, null=True, blank=True)

class FechaHora(models.Model):
    Id_fecha_hora = models.IntegerField(primary_key=True)
    Fecha_hora = models.DateTimeField(null=True, blank=True)

class Aeropuerto(models.Model):
    Id_aeropuerto = models.IntegerField(primary_key=True)
    Aviones_disponibles = models.IntegerField(null=True, blank=True)
    Empleados = models.IntegerField(null=True, blank=True)
    Id_estado = models.ForeignKey(Estado)
    Id_usuario = models.ForeignKey(Usuario)
    Id_fecha_hora = models.ForeignKey(FechaHora)

class ModelosAviones(models.Model):
    Id_modelo = models.IntegerField(primary_key=True)
    Modelo = models.CharField(max_length=60, null=True, blank=True)

class Granjero(models.Model):
    Rut_granjero = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=True, blank=True)
    Apellido = models.CharField(max_length=30, null=True, blank=True)
    Edad_granjero = models.IntegerField(null=True, blank=True)
    Licencia = models.CharField(max_length=45, null=True, blank=True)
    Id_estado = models.ForeignKey(Estado)
    Id_usuario = models.ForeignKey(Usuario)
    Id_fecha_hora = models.ForeignKey(FechaHora)
    
class Aviones(models.Model):
    Id_avion = models.IntegerField(primary_key=True)
    Capacidad = models.IntegerField(null=True, blank=True)
    Id_modelo = models.ForeignKey(ModelosAviones)
    Id_estado = models.ForeignKey(Estado)
    Id_usuario = models.ForeignKey(Usuario)
    Id_fecha_hora = models.ForeignKey(FechaHora)
    Id_aeropuerto = models.ForeignKey(Aeropuerto)
    Rut_granjero = models.ForeignKey(Granjero)

class Gallinas(models.Model):
    Rut_gallina = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=True, blank=True)
    Apellido = models.CharField(max_length=30, null=True, blank=True)
    Plumas = models.IntegerField(null=True, blank=True)
    Equipaje_kg_gallina = models.IntegerField()
    Id_estado = models.ForeignKey(Estado)
    Id_usuario = models.ForeignKey(Usuario)
    Id_fecha_hora = models.ForeignKey(FechaHora)
    Id_pasaje = models.ForeignKey(Pasajes)

class Gallos(models.Model):
    Rut_gallo = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=True, blank=True)
    Apellido = models.CharField(max_length=30, null=True, blank=True)
    Alas = models.IntegerField(null=True, blank=True)
    Equipaje_kg_gallo = models.IntegerField(null=True, blank=True)
    Id_estado = models.ForeignKey(Estado)
    Id_usuario = models.ForeignKey(Usuario)
    Id_fecha_hora = models.ForeignKey(FechaHora)
    Id_pasaje = models.ForeignKey(Pasajes)

class Pasajes(models.Model):
    Id_pasaje = models.IntegerField(primary_key=True, null=True, blank=True)
    Rut_gallina = models.ForeignKey(Gallinas)
    Rut_gallo = models.ForeignKey(Gallos)
    Asiento = models.IntegerField(null=True, blank=True)
    Hora_vuelo = models.DateTimeField(null=True, blank=True)
    Numero_avion = models.IntegerField(null=True, blank=True)
    Codigo_verificacion = models.CharField(max_length=60, null=True, blank=True)
    Id_estado = models.ForeignKey(Estado)
    Id_usuario = models.ForeignKey(Usuario)
    Id_fecha_hora = models.ForeignKey(FechaHora)
    Id_aeropuerto = models.ForeignKey(Aeropuerto)

class Trabajador(models.Model):
    Id_trabajador = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=30, null=True, blank=True)
    Apellido = models.CharField(max_length=30, null=True, blank=True)
    Area_trabajo = models.CharField(max_length=50, null=True, blank=True)
    Id_estado = models.ForeignKey(Estado)
    Id_usuario = models.ForeignKey(Usuario)
    Id_fecha_hora = models.ForeignKey(FechaHora)
    Id_aeropuerto = models.ForeignKey(Aeropuerto)
