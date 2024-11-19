from rest_framework import serializers
from . import models 
from cloudinary.models import CloudinaryField

# Serializer para Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Usuario
        fields = ['usuario', 'nombres', 'apellidos', 'correo', 'username', 'contraseña', 
                  'fecha_registro', 'fecha_nacimiento', 'foto', 'telefono', 'direccion']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.foto:
            representation['foto'] = instance.foto.url
        
        return representation

    def update(self, instance, validated_data):
        if 'foto' not in validated_data or validated_data['foto'] is None:
            validated_data['foto'] = instance.foto
        return super().update(instance, validated_data)
    
# Serializer para EspecialidadVeterinario
class ServicioVeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServicioVeterinario
        fields = '__all__'
        
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
        fields = '__all__'

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
        fields = '__all__' 
   
# Serializer para CategoriaProductos    
class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoriaProducto
        fields = '__all__'
        
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
        fields = '__all__' 
       
# Serializer para Carrito       
class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carrito 
        fields = ['id', 'usuario'] 

# Serializer para ProductoCarrito
class ProductoCarritoSerializer(serializers.ModelSerializer):
    carrito = CarritoSerializer()  
    producto = ProductoSerializer()  

    class Meta:
        model = models.ProductoCarrito
        fields = ['id', 'carrito', 'producto', 'cantidad', 'precio']
      
# Serializer para Venta  
class VentaSerializer(serializers.ModelSerializer):
    metodo_pago = serializers.PrimaryKeyRelatedField(queryset=models.MetodoPago.objects.all())
    carrito = serializers.PrimaryKeyRelatedField(queryset=models.Carrito.objects.all(), required=False)
    usuario = serializers.PrimaryKeyRelatedField(queryset=models.Usuario.objects.all())
    
    class Meta:
        model = models.Venta
        fields = ['id', 'metodo_pago', 'numero_tarjeta', 'correo', 'fecha_expiracion', 'cvv', 'carrito', 'usuario', 'subtotal', 'total', 'fecha_venta']

# Serializer para DetalleCarrito
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
        
# Serializer para Mascota       
class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Mascota
        fields = ['mascota_id' , 'usuario','nombre', 'especie','raza','fecha_nacimiento',
                'peso','altura','edad','color','fotom','observaciones','fecha_inscripcion','codigo_identificacion'] 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.fotom:
            representation['fotom'] = instance.fotom.url
        
        return representation 

    def update(self, instance, validated_data):
        fotom = validated_data.get('fotom', None)
        if fotom is None:
            validated_data['fotom'] = instance.fotom
        return super().update(instance, validated_data)

# Serializer para Horario  
class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Horario
        fields = '__all__' 
        
# Serializer para Cita 
class CitaSerializer(serializers.ModelSerializer):
    usuario_id = UsuarioSerializer(required=False) 
    mascota_id = MascotaSerializer()  
    servicio_id = ServicioSerializer()  
    horario_id = HorarioSerializer() 

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