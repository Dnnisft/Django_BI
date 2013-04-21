#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from inventario.models import *



class ProductoForm(ModelForm):
    class Meta:
        model = Productos

class ClienteForm(ModelForm):
    class Meta:
        model = Clientes

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedores

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursales

class ZonaForm(ModelForm):
    class Meta:
        model = Zonas

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamentos

class CategoriaForm(ModelForm):
    class Meta:
        model = Categorias

class SubcategoriaForm(ModelForm):
    class Meta:
        model = Subcategorias
		
class VentasForm(ModelForm):
    class Meta:
        model = Ventas



