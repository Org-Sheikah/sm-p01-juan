from django.db import models
from django.contrib.auth.models import User

# -------------------------------------------------------------
# 1. RELACIÓN 1 A 1 (OneToOneField)
# Ejemplo: Cada usuario tiene un único perfil
# -------------------------------------------------------------
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"


# -------------------------------------------------------------
# 2. RELACIÓN MACHOS A MACHOS O 1 A MUCHOS (ForeignKey)
# Ejemplo: Un usuario puede hacer MUCHOS cálculos o guardar varias Rutas
# -------------------------------------------------------------
class OperacionCalculadora(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # 1 Usuario -> Muchos Cálculos
    expresion = models.CharField(max_length=200)               # Ej: "5 + 5"
    resultado = models.CharField(max_length=100)               # Ej: "10"
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expresion} = {self.resultado}"


# -------------------------------------------------------------
# 3. RELACIÓN MUCHOS A MUCHOS (ManyToManyField)
# Ejemplo: Las rutas del mapa pueden tener MÚLTIPLES etiquetas/categorías
# y una etiqueta puede estar en MÚLTIPLES rutas
# -------------------------------------------------------------
class EtiquetaRuta(models.Model):
    nombre = models.CharField(max_length=50)  # Ej: "Trabajo", "Turismo", "Frecuente"

    def __str__(self):
        return self.nombre

class RutaGuardada(models.Model):
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    # Una ruta puede tener varias etiquetas y una etiqueta puede pertenecer a varias rutas:
    etiquetas = models.ManyToManyField(EtiquetaRuta)

    def __str__(self):
        return f"Ruta: {self.origen} -> {self.destino}"
    