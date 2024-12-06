from django.urls import path
from . import views

urlpatterns = [
    
    # URLs para Usuarios
    path('usuarios/', views.UsuariosListCreate.as_view(), name='usuarios-list-create'),
    path('usuarios/<int:pk>/', views.UsuariosRetrieveUpdateDestroy.as_view(), name='usuarios-retrieve-update-destroy'),
    
    # URL para EspecialidadVeterinario
    path('especialidades-veterinario/', views.ServicioVeterinarioList.as_view(), name='especialidades-veterinario-list'),
    
    # URL para Veterinario
    path('veterinarios/', views.VeterinariosList.as_view(), name='veterinarios-list'),
    
    # URL para CategoriaServicio
    path('categorias-servicios/', views.CategoriaServiciosList.as_view(), name='categoria-servicios-list'),
    
    # URL para Servicio
    path('servicios/', views.ServiciosList.as_view(), name='servicios-list'),
    path('servicios/<int:servicio_id>/', views.ServicioDetail.as_view(), name='servicio-detail'), 
    
    # URL para DetalleVeterinaria
    path('detalle-veterinaria/', views.DetalleVeterinariaList.as_view(), name='detalle-veterinaria-list'),
    
    # URL para CategoriaProducto
    path('categorias-productos/', views.CategoriaProductosList.as_view(), name='categoria-productos-list'),
    
    # URL para Producto
    path('productos/', views.ProductosList.as_view(), name='productos-list'),
    
    # URL para MetodoPago
    path('metodos-pago/', views.MetodoPagoList.as_view(), name='metodo-pago-list'),
    path('metodos-pago/<int:pk>/', views.MetodoPagoRetrieveUpdateDestroy.as_view(), name='metodo-pago-retrieve-update-destroy'),

    # URLs para Carritos
    path('carritos/', views.CarritoListCreate.as_view(), name='carrito-list-create'),
    path('carritos/<int:pk>/', views.CarritoRetrieveUpdateDestroy.as_view(), name='carrito-retrieve-update-destroy'),
    
    
    # URLs para ProductoCarrito
    path('productos-carrito/', views.ProductoCarritoListCreate.as_view(), name='producto-carrito-list-create'),
    path('productos-carrito/<int:pk>/', views.ProductoCarritoRetrieveUpdateDestroy.as_view(), name='producto-carrito-retrieve-update-destroy'),
    path('productos-carrito/<int:carrito_id>/<int:usuario_id>/', views.ProductoCarritoListCreate.as_view(), name='producto-carrito-list-create'),

    # URLs para DetalleVenta
    path('detalles-venta/', views.DetalleVentaListCreate.as_view(), name='detalle-venta-list-create'),
    path('detalles-venta/<int:pk>/', views.DetalleVentaRetrieveUpdateDestroy.as_view(), name='detalle-venta-retrieve-update-destroy'),
    
    
    # URLs para DetalleVenta
    path('detalles-carrito/', views.DetalleCarritoListCreate.as_view(), name='detalle-carrito-list-create'),
    path('detalles-carrito/<int:pk>/', views.DetalleCarritoRetrieveUpdateDestroy.as_view(), name='detalle-carrito-retrieve-update-destroy'),
    
    # URLs para Venta
    path('ventas/', views.VentaListCreate.as_view(), name='venta-list-create'),
    path('ventas/<int:pk>/', views.VentaRetrieveUpdateDestroy.as_view(), name='venta-retrieve-update-destroy'),
    
    # URLs para Mascota
    path('mascotas/', views.MascotaListCreate.as_view(), name='mascota-list-create'),
    path('mascotas/<int:pk>/', views.MascotaRetrieveUpdateDestroy.as_view(), name='mascota-retrieve-update-destroy'),
    path('mascotas/<int:mascota_id>/<int:usuario_id>/', views.MascotaListCreate.as_view(), name='mascota-list-create'),
    path('mascotas/usuario/<int:usuario_id>/', views.MascotaPorUsuario.as_view(), name='mascota-por-usuario'),

    # URL para Horario
    path('horarios/', views.HorarioList.as_view(), name='horario-list'),
    path('horarios/<int:horario_id>/', views.HorarioDetail.as_view(), name='horario-detail'), 
    
    # URLs para Cita
    path('citas/', views.CitaListCreate.as_view(), name='cita-list-create'),
    path('citas/<int:pk>/<int:usuario_id>/', views.CitaRetrieveUpdateDestroy.as_view(), name='cita-retrieve-update-destroy'),
    path('citas/usuario/<int:usuario_id>/', views.CitasPorUsuario.as_view(), name='citas-por-usuario'),
    path('citas/usuario/<int:usuario_id>/cita/<int:cita_id>/', views.CitasPorUsuarioDelete.as_view(), name='citas-por-usuario-delete'),


 
    # URL para HistorialMascota
    path('historial-mascotas/', views.HistorialMascotaList.as_view(), name='historial-mascotas-list'),
    
    
]
