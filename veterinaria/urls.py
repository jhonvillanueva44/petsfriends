from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('2/', views.dashboard2, name='index2'),
    path('3/', views.dashboard3, name='index3'),
    path('4/', views.dashboard4, name='index4'),
    
    path('widgets/', views.widgets, name='widgets'),
    
    path('chartjs/', views.chartjs, name='chartjs'),
    path('flot/', views.flot, name='flot'),
    path('inline/', views.inline, name='inline'),
    path('uplot/', views.uplot, name='uplot'),
    
    path('usuarios/', views.tableUsuarios, name='table-usuarios'),
    path('usuarios/<int:usuario>/', views.verUsuario, name='ver_usuario'),
    path('usuarios/crear/', views.crearUsuario, name='crear_usuario'),
    path('usuarios/editar/<int:usuario_id>/', views.editarUsuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:usuario_id>/', views.eliminarUsuario, name='eliminar_usuario'),
    
    path('especialidad/', views.tableEspecialidad, name='table-especialidad'),
    path('especialidad/<int:Servicio_veterinario_id>/', views.verEspecialidad, name='ver_especialidad'),
    path('especialidad/crear/', views.crearEspecialidad, name='crear_especialidad'),
    path('especialidad/editar/<int:Servicio_veterinario_id>/', views.editarEspecialidad, name='editar_especialidad'),
    path('especialidad/eliminar/<int:Servicio_veterinario_id>/', views.eliminarEspecialidad, name='eliminar_especialidad'),
    
    path('veterinarios/', views.tableVeterinarios, name='table-veterinarios'),
    path('veterinarios/<int:veterinario_id>/', views.verVeterinario, name='ver_veterinario'),
    path('veterinarios/crear/', views.crearVeterinario, name='crear_veterinario'),
    path('veterinarios/editar/<int:veterinario_id>/', views.editarVeterinario, name='editar_veterinario'),
    path('veterinarios/eliminar/<int:veterinario_id>/', views.eliminarVeterinario, name='eliminar_veterinario'),
    
    path('categorias-servicios/', views.tableCategoriasServicios, name='table-categorias-servicios'),
    path('categorias-servicios/<int:categoria_servicio_id>/', views.verCategoriaServicios, name='ver_categoria_servicios'),
    path('categorias-servicios/crear/', views.crearCategoriaServicios, name='crear_categoria_servicios'),
    path('categorias-servicios/editar/<int:categoria_servicio_id>/', views.editarCategoriaServicios, name='editar_categoria_servicios'),
    
    path('servicios/', views.tableServicios, name='table-servicios'),
    path('servicios/<int:servicio_id>/', views.verServicio, name='ver_servicio'),
    path('servicios/crear/', views.crearServicio, name='crear_servicio'),
    path('servicios/editar/<int:servicio_id>/', views.editarServicio, name='editar_servicio'),
    
    path('detalles-veterinaria/', views.tableDetallesVeterinaria, name='table-detalles-veterinaria'),
    path('detalles-veterinaria/<int:detalle_veterinaria_id>/', views.verDetalleVeterinaria, name='ver_detalle_veterinaria'),
    path('detalles-veterinaria/crear/', views.crearDetalleVeterinaria, name='crear_detalle_veterinaria'),
    path('detalles-veterinaria/editar/<int:detalle_veterinaria_id>/', views.editarDetalleVeterinaria, name='editar_detalle_veterinaria'),
    
    path('categorias-productos/', views.tableCategoriasProductos, name='table-categorias-productos'),
    path('categorias-productos/<int:categoria_producto_id>/', views.verCategoriaProducto, name='ver_categoria_producto'),
    path('categorias-productos/crear/', views.crearCategoriaProducto, name='crear_categoria_producto'),
    path('categorias-productos/editar/<int:categoria_producto_id>/', views.editarCategoriaProducto, name='editar_categoria_producto'),
    
    path('productos/', views.tableProductos, name='table-productos'),
    path('productos/<int:producto_id>/', views.verProducto, name='ver_producto'),
    path('productos/crear/', views.crearProducto, name='crear_producto'),
    path('productos/editar/<int:producto_id>/', views.editarProducto, name='editar_producto'),
    
    path('metodos-pago/', views.tableMetodosPago, name='table-metodos-pago'),
    path('metodos-pago/<int:metodo_id>/', views.verMetodoPago, name='ver_metodo_pago'),
    path('metodos-pago/crear/', views.crearMetodoPago, name='crear_metodo_pago'),
    path('metodos-pago/editar/<int:metodo_id>/', views.editarMetodoPago, name='editar_metodo_pago'),
    
    path('carritos/', views.tableCarritos, name='table-carritos'),
    path('carritos/<int:carrito_id>/', views.verCarrito, name='ver_carrito'),
    
    path('productos-carrito/', views.tableProductosCarrito, name='table-productos-carrito'),
    path('productos_carrito/<int:carrito_id>/', views.verProductosCarrito, name='ver_productos_carrito'),
    
    path('ventas/', views.tableVentas, name='table-ventas'),
    path('ventas/<int:venta_id>/', views.verVenta, name='ver_venta'),
    
    path('detalles-venta/', views.tableDetallesVenta, name='table-detalles-venta'),
    path('detalles-venta/<int:venta_id>/', views.verDetalleVenta, name='ver_detalle_venta'),
    
    path('mascotas/', views.tableMascotas, name='table-mascotas'),
    path('mascotas/<int:mascota_id>/', views.verMascota, name='ver_mascota'),
    path('mascotas/crear/', views.crearMascota, name='crear_mascota'),
    path('mascotas/editar/<int:mascota_id>/', views.editarMascota, name='editar_mascota'),
    
    path('horarios/', views.tableHorarios, name='table-horarios'),
    path('horarios/<int:horario_id>/', views.verHorario, name='ver_horario'),
    path('horarios/crear/', views.crearHorario, name='crear_horario'),
    path('horarios/editar/<int:horario_id>/', views.editarHorario, name='editar_horario'),
    
    path('citas/', views.tableCitas, name='table-citas'),
    path('citas/<int:cita_id>/', views.verCita, name='ver_cita'),
    path('citas/crear/', views.crearCita, name='crear_cita'),
    path('citas/editar/<int:cita_id>/', views.editarCita, name='editar_cita'),
    
    path('historiales/', views.tableHistorialMascotas, name='table-historial-mascotas'),
    path('historial/<int:historial_id>/', views.verHistorialMascota, name='ver_historial_mascota'),
]