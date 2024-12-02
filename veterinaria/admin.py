from django.contrib import admin
from api import models

admin.site.register(models.Usuario)
admin.site.register(models.ServicioVeterinario)
admin.site.register(models.Veterinario)
admin.site.register(models.CategoriaServicio)
admin.site.register(models.Servicio)
admin.site.register(models.DetalleVeterinaria)
admin.site.register(models.CategoriaProducto)
admin.site.register(models.Producto)
admin.site.register(models.MetodoPago)
admin.site.register(models.Carrito)
admin.site.register(models.ProductoCarrito)
admin.site.register(models.Venta)
admin.site.register(models.DetalleVenta)
admin.site.register(models.Mascota)
admin.site.register(models.Horario)
admin.site.register(models.Cita)
admin.site.register(models.HistorialMascota)
admin.site.register(models.DetalleCarrito)

