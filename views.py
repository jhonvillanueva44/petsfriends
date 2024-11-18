from django.shortcuts import render
from api import models
from django.db.models.functions import TruncMonth
from django.db.models import Count
import json
from django.utils import timezone
from django.db.models import Q

# Vista para el index.html
def dashboard(request):
    
    #------------------------------------------------ WIDGETS PARTE SUPERIOR -------------------------------------------#
    
    # Conteos para widgets de la parte superior
    total_usuarios = models.Usuario.objects.count() 
    total_mascotas = models.Mascota.objects.count()
    total_productos = models.Producto.objects.count()  
    total_servicios = models.Servicio.objects.count() 

    #------------------------------------------------ GRAFICO DE BARRAS -------------------------------------------#

    # Obtener el conteo de las compras por mes
    compras_por_mes = models.Compra.objects.annotate(month=TruncMonth('fecha_compra')).values('month').annotate(total=Count('compra_id')).order_by('month')

    # Inicializar la serie con especificamente 12 datos correspondiente a 12 meses
    serie = [0] * 12 
    pie_data = []

    # Llenar la serie con los conteos
    for compra in compras_por_mes:
        month_index = compra['month'].month - 1
        serie[month_index] = compra['total']
        month_name = compra['month'].strftime("%B") 
        pie_data.append({
            'value': compra['total'],
            'name': month_name  
        })

    #----------------------------------------------- GRAFICO DE PASTEL ---------------------------------------------#


    context = {
        'total_usuarios': total_usuarios,
        'total_mascotas': total_mascotas,
        'total_productos': total_productos,
        'total_servicios': total_servicios,
        'serie': json.dumps(serie),  
        'pie_data': json.dumps(pie_data)  
    }

    return render(request, 'veterinaria/index.html', context)

def dashboard2(request):
    return render(request, 'veterinaria/index2.html')

def dashboard3(request):
    return render(request, 'veterinaria/index3.html')

def widgets(request):
    
    # Obtener la fecha actual
    fecha_actual = timezone.now()
    
    # Extraer el mes y año actuales
    mes_actual = fecha_actual.month
    anio_actual = fecha_actual.year
    
    # Filtrar usuarios que se registraron en el mes y año actuales
    total_usuarios_mes = models.Usuario.objects.filter(
        fecha_registro__month=mes_actual,
        fecha_registro__year=anio_actual
    ).count()
    
    # Obtener usuarios con foto de perfil (ajuste para asegurar que el campo foto no sea vacío)
    total_usuarios_con_foto = models.Usuario.objects.filter(foto__isnull=False).exclude(foto='').count()

    # Obtener el total de usuarios con todos los datos completos
    total_usuarios_completos = models.Usuario.objects.filter(
        Q(nombres__isnull=False) & ~Q(nombres='') &
        Q(apellidos__isnull=False) & ~Q(apellidos='') &
        Q(correo__isnull=False) & ~Q(correo='') &
        Q(username__isnull=False) & ~Q(username='') &
        Q(fecha_nacimiento__isnull=False) &
        Q(foto__isnull=False) & ~Q(foto='') &
        Q(telefono__isnull=False) & ~Q(telefono='') &
        Q(direccion__isnull=False) & ~Q(direccion='')
    ).count()

    total_usuarios = models.Usuario.objects.count()
    
    # Obtener usuarios con al menos una mascota 
    total_usuarios_con_mascota = models.Usuario.objects.filter(
        mascota__isnull=False  
    ).distinct().count()
    
    return render(request, 'veterinaria/pages/widgets.html', {
        'total_usuarios': total_usuarios,
        'total_usuarios_mes': total_usuarios_mes,
        'total_usuarios_con_foto': total_usuarios_con_foto,
        'total_usuarios_completos': total_usuarios_completos,
        'total_usuarios_con_mascota': total_usuarios_con_mascota,
    })

def chartjs(request):
    return render(request, 'veterinaria/pages/charts/chartjs.html')

def flot(request):
    return render(request, 'veterinaria/pages/charts/flot.html')

def inline(request):
    return render(request, 'veterinaria/pages/charts/inline.html')

def uplot(request):
    return render(request, 'veterinaria/pages/charts/uplot.html')


def calendar(request):
    return render(request, 'veterinaria/pages/calendar.html')


def mailbox(request):
    return render(request, 'veterinaria/pages/mailbox/mailbox.html')

def compose(request):
    return render(request, 'veterinaria/pages/mailbox/compose.html')

def readMail(request):
    return render(request, 'veterinaria/pages/mailbox/read-mail.html')


def simples(request):
    return render(request, 'veterinaria/pages/search/simple.html')

def enhanced(request):
    return render(request, 'veterinaria/pages/search/enhanced.html')


