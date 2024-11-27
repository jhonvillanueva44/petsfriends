from rest_framework import generics
from . import models
from . import serializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

# Vista para crear y listar usuarios
class UsuariosListCreate(generics.ListCreateAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        try:
            serializer.save()
        except ValidationError as e:
            return Response({'error': 'Error en la carga de datos', 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Error inesperado', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': 'Error procesando la solicitud', 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Vista para recuperar, actualizar y eliminar usuarios
class UsuariosRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer
    parser_classes = (MultiPartParser, FormParser)  

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
    
# Vista para obtener la lista de métodos de pagos
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
    
# Vistas para ProductoCarritos
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
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        try:
            serializer.save()
        except ValidationError as e:
            return Response({'error': 'Error en la carga de datos', 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Error inesperado', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': 'Error procesando la solicitud', 'details': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        usuario_id = self.request.query_params.get('usuario_id', None)
        mascota_id = self.request.query_params.get('mascota_id', None)
        
        queryset = models.Mascota.objects.all()

        if usuario_id:
            queryset = queryset.filter(usuario_id=usuario_id)

        if mascota_id:
            queryset = queryset.filter(id=mascota_id)

        return queryset
    
class MascotaPorUsuario(generics.ListAPIView):
    serializer_class = serializers.MascotaSerializer

    def get_queryset(self):
        usuario_id = self.kwargs['usuario_id']
        return models.Mascota.objects.filter(usuario_id=usuario_id)

class MascotaRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Mascota.objects.all()
    serializer_class = serializers.MascotaSerializer

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
