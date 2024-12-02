from django import forms
from api import models
import datetime

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ['nombres', 'apellidos', 'correo', 'username', 'contraseña', 'fecha_nacimiento', 'foto', 'telefono', 'direccion']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }
        
class EspecialidadVeterinarioForm(forms.ModelForm):
    class Meta:
        model = models.ServicioVeterinario
        fields = ['nombre', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descripción breve...'}),
        }
        
class VeterinarioForm(forms.ModelForm):
    class Meta:
        model =  models.Veterinario
        fields = ['nombres', 'apellidos', 'telefono', 'correo', 'especialidad_id', 'fecha_nacimiento', 'foto']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'foto': forms.ClearableFileInput(attrs={'multiple': False}),
        }

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if len(telefono) != 9:
            raise forms.ValidationError("El teléfono debe tener 9 dígitos.")
        return telefono
    
class CategoriaServicioForm(forms.ModelForm):
    class Meta:
        model = models.CategoriaServicio
        fields = ['nombre', 'descripcion']
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre de la categoría debe tener al menos 3 caracteres.")
        return nombre
    
class ServicioForm(forms.ModelForm):
    class Meta:
        model = models.Servicio
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'veterinario']
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre del servicio debe tener al menos 3 caracteres.")
        return nombre
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser un valor positivo.")
        return precio
    
class DetalleVeterinariaForm(forms.ModelForm):
    class Meta:
        model = models.DetalleVeterinaria
        fields = ['direccion', 'telefono', 'correo_contacto', 'horario_apertura', 'horario_cierre', 'instagram', 'facebook', 'twitter']

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if len(telefono) != 9:
            raise forms.ValidationError("El teléfono debe tener 9 dígitos.")
        return telefono
    
class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = models.CategoriaProducto
        fields = ['nombre', 'descripcion']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre de la categoría debe tener al menos 3 caracteres.")
        return nombre
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ['nombre', 'precio', 'categoria_producto_id', 'stock', 'marca', 'descripcion', 'estado', 'imagen']
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre del producto debe tener al menos 3 caracteres.")
        return nombre
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio
    
class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = models.MetodoPago
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del método de pago'})
        }
        
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre del producto debe tener al menos 3 caracteres.")
        return nombre
    
class MascotaForm(forms.ModelForm):
    class Meta:
        model = models.Mascota
        fields = ['usuario', 'nombre', 'especie', 'raza', 'genero', 'fecha_nacimiento', 'peso', 'altura', 'edad', 'color', 'fotom', 'observaciones']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 3:
            raise forms.ValidationError("El nombre de la mascota debe tener al menos 3 caracteres.")
        return nombre

    def clean_peso(self):
        peso = self.cleaned_data.get('peso')
        if peso and peso <= 0:
            raise forms.ValidationError("El peso debe ser mayor que cero.")
        return peso

    def clean_altura(self):
        altura = self.cleaned_data.get('altura')
        if altura and altura <= 0:
            raise forms.ValidationError("La altura debe ser mayor que cero.")
        return altura

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        if edad and edad <= 0:
            raise forms.ValidationError("La edad debe ser mayor que cero.")
        return edad
    
class HorarioForm(forms.ModelForm):
    class Meta:
        model = models.Horario
        fields = ['hora']

    def clean_hora(self):
        hora = self.cleaned_data.get('hora')
        if hora and (hora.hour < 6 or hora.hour > 22):
            raise forms.ValidationError("La hora debe estar entre las 06:00 y las 22:00.")
        return hora

class CitaForm(forms.ModelForm):
    class Meta:
        model = models.Cita
        fields = ['usuario_id', 'mascota_id', 'servicio_id', 'razon', 'observaciones', 'fecha_cita', 'horario_id', 'estado']

