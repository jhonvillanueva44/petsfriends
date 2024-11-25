from django.db import models
import uuid
from cloudinary.models import CloudinaryField

# La tabla para usuarios
class Usuario(models.Model):
    usuario = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    foto = CloudinaryField('foto', null=True, blank=True)
    telefono = models.CharField(max_length=9, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Usuario' 
        verbose_name_plural = 'Usuarios' 
        
# La tabla para especialidades de veterinarios
class ServicioVeterinario(models.Model):
    Servicio_veterinario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Servicio de Veterinario'
        verbose_name_plural = 'Servicio de Veterinarios'
        
# La tabla para veterinarios
class Veterinario(models.Model):
    veterinario_id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    correo = models.EmailField(unique=True)
    especialidad_id = models.ForeignKey(ServicioVeterinario, on_delete=models.CASCADE, default=0)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    foto = CloudinaryField('foto', null=True, blank=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        
# La tabla para categorias de servicios
class CategoriaServicio(models.Model):
    categoria_servicio_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría de Servicio'
        verbose_name_plural = 'Categorías de Servicios'
        
# La tabla para servicios
class Servicio(models.Model):
    servicio_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(CategoriaServicio, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        
# La tabla para detalles de la veterinaria
class DetalleVeterinaria(models.Model):
    detalle_veterinaria_id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=9)
    correo_contacto = models.EmailField(null=True, blank=True)
    horario_apertura = models.CharField(max_length=100, default='Lunes a Viernes: 9 AM')
    horario_cierre = models.CharField(max_length=100, default='Lunes a Viernes: 5 PM')
    instagram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.direccion} ({self.telefono})"

    class Meta:
        verbose_name = 'Detalle de Veterinaria'
        verbose_name_plural = 'Detalles de Veterinarias'
        
# La tabla para categorias de productos
class CategoriaProducto(models.Model):
    categoria_producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría de Producto'
        verbose_name_plural = 'Categorías de Productos'
        
#La tabla para productos
class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria_producto_id = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    marca = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.BooleanField(default=True)
    imagen = CloudinaryField('imagen', null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        
# Tabla para métodos de pago
class MetodoPago(models.Model):
    metodo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pago'
        
# Tabla para carrito
class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'Carrito de {self.usuario.username}'

    class Meta:
        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'
        
# Tabla para productos del carrito
class ProductoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Calcular el precio en base a la cantidad y precio unitario del producto
        self.precio = self.producto.precio * self.cantidad
        super(ProductoCarrito, self).save(*args, **kwargs)

        # Crear o actualizar el DetalleCarrito correspondiente
        detalle_carrito, created = DetalleVenta.objects.update_or_create(
            carrito=self.carrito,
            producto=self.producto,
            defaults={
                'cantidad': self.cantidad,
                'precio': self.precio
            }
        )

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre} en el carrito'

    class Meta:
        verbose_name = 'Producto en Carrito'
        verbose_name_plural = 'Productos en Carrito'


        
# Tabla para venta
class Venta(models.Model):
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    numero_tarjeta = models.CharField(max_length=20)
    correo = models.EmailField(blank=True, null=True)
    fecha_expiracion = models.DateField(blank=True, null=True)
    cvv = models.PositiveIntegerField(null=True)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def calcular_subtotal(self):
        """Calcula el subtotal sumando el precio * cantidad de cada producto en el carrito"""
        subtotal = 0
        detalles_venta = DetalleVenta.objects.filter(carrito=self.carrito)
        for detalle in detalles_venta:
            subtotal += detalle.precio * detalle.cantidad
        return subtotal

    def save(self, *args, **kwargs):
        """Sobrescribe el método save para calcular el subtotal antes de guardar y crear DetalleVenta"""
        self.subtotal = self.calcular_subtotal()  
        self.total = self.subtotal  
        super(Venta, self).save(*args, **kwargs)

        # Crear registros de DetalleVenta para cada ProductoCarrito del carrito
        productos_carrito = ProductoCarrito.objects.filter(carrito=self.carrito)
        for producto in productos_carrito:
            DetalleVenta.objects.create(
                venta=self,
                carrito=self.carrito,
                producto=producto.producto,
                cantidad=producto.cantidad,
                precio=producto.precio
            )

    def __str__(self):
        return f'venta {self.id} - {self.usuario.username}'

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        
# Tabla para detalles de la venta
class DetalleVenta(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    venta = models.ForeignKey('Venta', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre} en el carrito'

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        
# Tabla para mascotas
class Mascota(models.Model):
    mascota_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    edad = models.PositiveIntegerField(null=True, blank=True)
    color = models.CharField(max_length=50)
    fotom = CloudinaryField('fotom', null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    codigo_identificacion = models.CharField(max_length=16, unique=True, editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.codigo_identificacion:
            self.codigo_identificacion = str(uuid.uuid4())[:8]  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        
# Tabla para horarios
class Horario(models.Model):
    horario_id = models.AutoField(primary_key=True)
    hora = models.TimeField(unique=True)  

    def __str__(self):
        return self.hora.strftime("%H:%M") 

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        
# Tabla para citas
class Cita(models.Model):
    cita_id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    mascota_id = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    servicio_id = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    razon = models.TextField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    fecha_cita = models.DateField()
    horario_id = models.ForeignKey(Horario, on_delete=models.CASCADE)  
    costo_cita = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
            if self.servicio_id:
                self.costo_cita = self.servicio_id.precio
            super().save(*args, **kwargs)
            
    def __str__(self):
        return f"Cita para {self.mascota_id.nombre} el {self.fecha_cita} a las {self.horario_id.hora}"

    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        
# Tabla de historial de mascotas
class HistorialMascota(models.Model):
    historial_id = models.AutoField(primary_key=True)
    mascota_id = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    cita_id = models.ForeignKey(Cita, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Historial de {self.mascota_id.nombre} en {self.fecha}"

    class Meta:
        verbose_name = 'Historial de Mascota'
        verbose_name_plural = 'Historiales de Mascotas'
        
        
# Modelo DetalleCarrito actualizado
class DetalleCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre} en el carrito'

    class Meta:
        verbose_name = 'Detalle de Carrito'
        verbose_name_plural = 'Detalles de Carrito'