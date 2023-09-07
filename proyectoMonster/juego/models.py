from django.db import models

# Create your models here.


class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    

class TipoElemental(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    

class Evolucion(models.Model):
    nombre = models.CharField(max_length=100)
    nivel_requerido = models.PositiveIntegerField()
    monstruo_padre = models.ForeignKey('Monster', related_name='evoluciones', on_delete=models.CASCADE)
    monstruo_hijo = models.ForeignKey('Monster', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    

class Habilidades(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.nombre
    




class Monster(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    tipo1 = models.ForeignKey(TipoElemental, on_delete=models.CASCADE, related_name='monstruo_tipo1')
    tipo2 = models.ForeignKey(TipoElemental, on_delete=models.CASCADE, related_name='monstruo_tipo2')
    habilidad_especial = models.ForeignKey(Habilidades, on_delete=models.CASCADE)
    nivel = models.PositiveIntegerField()
    salud = models.PositiveIntegerField()
    ataque_fisico = models.PositiveIntegerField()
    poder_habilidad = models.PositiveIntegerField()
    armadura = models.PositiveIntegerField()
    resitencia_magica = models.PositiveIntegerField()
    velocidad = models.PositiveIntegerField()
    probabilidad_critico = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=250)
    estado_actual = models.ForeignKey(Estado, on_delete=models.SET_NULL, blank=True, null=True)
    imagen = models.ImageField(upload_to='img_monstruos/', blank=True, null=True)
    etapa_evolucion = models.ForeignKey(Evolucion, on_delete=models.SET_NULL, blank=True, null=True)
    experiencia = models.PositiveIntegerField(default=0)
    


class Objeto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    efecto = models.CharField(max_length=100)  # Puede ser un efecto específico del objeto.
    cantidad = models.PositiveIntegerField(default=1)  # Cuántos de este objeto tiene el jugador.
    efecto_en_monstruo = models.ForeignKey(Monster, on_delete=models.CASCADE, blank=True, null=True)
    precio_compra = models.PositiveIntegerField()
    precio_venta = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre


