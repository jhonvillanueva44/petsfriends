from rest_framework import generics
from . import models
from . import serializers

# Vistas para Usuarios
class UsuariosListCreate(generics.ListCreateAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class UsuariosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['partial'] = True
        return context
    
# Vista para obtener la lista de especialidades de veterinarios
class ServicioVeterinarioList(generics.ListAPIView):
    queryset = models.Servicio.objects.all() 
    serializer_class = serializers.ServicioSerializer  

# Vista para obtener la lista de veterinarios
class VeterinariosList(generics.ListAPIView):
    queryset = models.Veterinario.objects.all()
    serializer_class = serializers.VeterinarioSerializer
    
# Vista para obtener la lista de categorias de servicios
class CategoriaServiciosList(generics.ListAPIView):
    queryset = models.CategoriaServicio.objects.all()
    serializer_class = serializers.CategoriaServicioSerializer
    
# Vista para obtener la lista de servicios
class ServiciosList(generics.ListAPIView):
    queryset = models.Servicio.objects.all()
    serializer_class = serializers.ServicioSerializer
    
# Vista para obtener la lista de los detalles de la veterinaria
class DetalleVeterinariaList(generics.ListAPIView):
    queryset = models.DetalleVeterinaria.objects.all()
    serializer_class = serializers.DetalleVeterinariaSerializer
   
# Vista para obtener la lista de categorías de productos 
class CategoriaProductosList(generics.ListAPIView):
    queryset = models.CategoriaProducto.objects.all()
    serializer_class = serializers.CategoriaProductoSerializer
    
# Vista para obtener la lista de productos
class ProductosList(generics.ListAPIView):
    queryset = models.Producto.objects.all()
    serializer_class = serializers.ProductoSerializer
    
# Vista para obtener la lista de métodos de pago
class MetodoPagoList(generics.ListAPIView):
    queryset = models.MetodoPago.objects.all()
    serializer_class = serializers.MetodoPagoSerializer

class MetodoPagoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MetodoPago.objects.all()
    serializer_class = serializers.MetodoPagoSerializer
    
# Vistas para Carrito
class CarritoListCreate(generics.ListCreateAPIView):
    queryset = models.Carrito.objects.all()
    serializer_class = serializers.CarritoSerializer

    def perform_create(self, serializer):
        serializer.save()

class CarritoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Carrito.objects.all()
    serializer_class = serializers.CarritoSerializer
    
# Vistas para ProductoCarrito
class ProductoCarritoListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.ProductoCarritoSerializer

    def get_queryset(self):
        carrito_id = self.request.query_params.get('carritoId', None)
        usuario_id = self.request.query_params.get('usuarioId', None)

        queryset = models.ProductoCarrito.objects.all()

        if carrito_id is not None:
            queryset = queryset.filter(carrito_id=carrito_id)
        if usuario_id is not None:
            queryset = queryset.filter(carrito__usuario_id=usuario_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save()
        
class ProductoCarritoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductoCarritoSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.ProductoCarrito.objects.filter(id=pk)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

# Vistas para DetalleVenta
class DetalleVentaListCreate(generics.ListCreateAPIView):
    queryset = models.DetalleVenta.objects.all()
    serializer_class = serializers.DetalleVentaSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetalleVentaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DetalleVenta.objects.all()
    serializer_class = serializers.DetalleVentaSerializer

# Vistas para DetalleCarrito
class DetalleCarritoListCreate(generics.ListCreateAPIView):
    queryset = models.DetalleCarrito.objects.all()
    serializer_class = serializers.DetalleCarritoSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetalleCarritoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.DetalleCarrito.objects.all()
    serializer_class = serializers.DetalleCarritoSerializer
    
# Vistas para Venta
class VentaListCreate(generics.ListCreateAPIView):
    queryset = models.Venta.objects.all()
    serializer_class = serializers.VentaSerializer

    def perform_create(self, serializer):
        serializer.save()

class VentaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Venta.objects.all()
    serializer_class = serializers.VentaSerializer
    
# Vistas para Mascota
class MascotaListCreate(generics.ListCreateAPIView):
    serializer_class = serializers.MascotaSerializer

    def get_queryset(self):
        usuario_id = self.request.query_params.get('usuario_id', None)
        mascota_id = self.request.query_params.get('mascota_id', None)
        
        queryset = models.Mascota.objects.all()

        if usuario_id is not None:
            queryset = queryset.filter(usuario_id=usuario_id)

        if mascota_id is not None:
            queryset = queryset.filter(id=mascota_id)

        return queryset

    def perform_create(self, serializer):
        serializer.save()

class MascotaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mascota.objects.all()
    serializer_class = serializers.MascotaSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['partial'] = True  
        return context

class MascotaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mascota.objects.all()
    serializer_class = serializers.MascotaSerializer

    def get_queryset(self):
            pk = self.kwargs['pk']
            return models.Mascota.objects.filter(id=pk)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['partial'] = True 
        return context
    
# Vista para obtener la lista de horarios
class HorarioList(generics.ListAPIView):
    queryset = models.Horario.objects.all()  
    serializer_class = serializers.HorarioSerializer
    
# Vistas para Cita
class CitaListCreate(generics.ListAPIView):
    queryset = models.Cita.objects.all()
    serializer_class = serializers.CitaSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        cita_id = self.request.query_params.get('cita_id')
        usuario_id = self.request.query_params.get('usuario_id')
        if cita_id:
            queryset = queryset.filter(cita_id=cita_id)
        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)
        return queryset
    
class CitaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cita.objects.all()
    serializer_class = serializers.CitaSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return models.Cita.objects.filter(cita_id=pk)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['partial'] = True  
        return context
    
# Vista para obtener la lista de historiales
class HistorialMascotaList(generics.ListAPIView):
    queryset = models.HistorialMascota.objects.all()  
    serializer_class = serializers.HistorialMascotaSerializer
