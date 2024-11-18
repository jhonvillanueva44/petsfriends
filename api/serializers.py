from rest_framework import serializers
from . import models 

# Serializer para Usuarios
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '_all_'  

    def update(self, instance, validated_data):
        if 'foto' not in validated_data or validated_data['foto'] is None:
            validated_data['foto'] = instance.foto
        return super().update(instance, validated_data)
    
# Serializer para EspecialidadVeterinario
class ServicioVeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServicioVeterinario
        fields = '_all_'
        
# Serializer para Veterinario
class VeterinarioSerializer(serializers.ModelSerializer):
    especialidad = ServicioVeterinarioSerializer(read_only=True)
    class Meta:
        model = models.Veterinario
        fields = ['veterinario_id', 'nombres', 'apellidos', 'telefono', 'correo', 'especialidad', 'fecha_nacimiento', 'foto']
        
# Serializer para CategoriaServicio
class CategoriaServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoriaServicio
        fields = '_all_'

# Serializer para Servicio
class ServicioSerializer(serializers.ModelSerializer):
    categoria = CategoriaServicioSerializer(read_only=True)
    veterinario = VeterinarioSerializer(read_only=True)
    class Meta:
        model = models.Servicio
        fields = ['servicio_id', 'nombre', 'descripcion', 'precio', 'categoria', 'veterinario']
        
# Serializer para DetalleVeterinaria
class DetalleVeterinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DetalleVeterinaria
        fields = '_all_' 
   
# Serializer para CategoriaProductos    
class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoriaProducto
        fields = '_all_'
        
# Serializer para Producto  
class ProductoSerializer(serializers.ModelSerializer):
    categoria_producto_id = CategoriaProductoSerializer(read_only=True)
    class Meta:
        model = models.Producto
        fields = ['producto_id', 'nombre', 'precio', 'categoria_producto_id', 'stock', 'marca', 'descripcion', 'estado', 'imagen']
   
# Serializer para MetodoPago       
class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MetodoPago
        fields = '_all_' 
       
# Serializer para Carrito       
class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carrito 
        fields = ['id', 'usuario'] 

# Serializer para ProductoCarrito con nested serializers
class ProductoCarritoSerializer(serializers.ModelSerializer):
    carrito = CarritoSerializer()  # Incluye los detalles completos del carrito
    producto = ProductoSerializer()  # Incluye los detalles completos del producto

    class Meta:
        model = models.ProductoCarrito
        fields = ['id', 'carrito', 'producto', 'cantidad', 'precio']
        
class VentaSerializer(serializers.ModelSerializer):
    metodo_pago = serializers.PrimaryKeyRelatedField(queryset=models.MetodoPago.objects.all())
    carrito = serializers.PrimaryKeyRelatedField(queryset=models.Carrito.objects.all(), required=False)
    usuario = serializers.PrimaryKeyRelatedField(queryset=models.Usuario.objects.all())
    
    class Meta:
        model = models.Venta
        fields = ['id', 'metodo_pago', 'numero_tarjeta', 'correo', 'fecha_expiracion', 'cvv', 'carrito', 'usuario', 'subtotal', 'total', 'fecha_venta']

# Serializer para DetalleVenta
class DetalleCarritoSerializer(serializers.ModelSerializer):
    carrito = CarritoSerializer()
    producto = ProductoSerializer() 

    class Meta:
        model = models.DetalleCarrito
        fields = ['id', 'carrito', 'producto', 'cantidad', 'precio']
      
# Serializer para DetalleVenta
class DetalleVentaSerializer(serializers.ModelSerializer):
    carrito = CarritoSerializer()
    producto =ProductoSerializer() 
    venta =VentaSerializer() 

    class Meta:
        model = models.DetalleVenta
        fields = ['id', 'carrito', 'producto', 'cantidad', 'precio', 'venta']
        
        
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mascota
        fields = ['mascota_id' , 'usuario','nombre', 'especie','raza','fecha_nacimiento',
                'peso','altura','edad','color','fotom','observaciones','fecha_inscripcion','codigo_identificacion'] 

    def update(self, instance, validated_data):
        if 'fotom' not in validated_data or validated_data['fotom'] is None:
            validated_data['fotom'] = instance.fotom
        return super().update(instance, validated_data)

    
# Serializer para Horario  
class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Horario
        fields = '_all_' 
        
        
class CitaSerializer(serializers.ModelSerializer):
    usuario_id = UsuarioSerializer(required=False)  # Incluir información completa de Usuario
    mascota_id = MascotaSerializer()  # Incluir información completa de Mascota
    servicio_id = ServicioSerializer()  # Incluir información completa de Servicio
    horario_id = HorarioSerializer()  # Incluir información completa de Horario

    class Meta:
        model = models.Cita
        fields = [
            'cita_id', 'usuario_id', 'mascota_id', 'servicio_id', 'razon', 
            'observaciones', 'fecha_cita', 'horario_id', 'costo_cita', 'estado'
        ]

# Serializer para HistorialMascota  
class HistorialMascotaSerializer(serializers.ModelSerializer):
    mascota_id = MascotaSerializer(read_only=True)
    cita_id = CitaSerializer(read_only=True)
    class Meta:
        model = models.HistorialMascota
        fields = ['historial_id', 'mascota_id', 'cita_id','fecha']