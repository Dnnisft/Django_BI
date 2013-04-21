from inventario.models import *
from inventario.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def lista_productos(request):
    productos = Productos.objects.all()
    return render_to_response('lista_productos.html',{'datos':productos}, context_instance=RequestContext(request))

def lista_clientes(request):
    clientes = 	Clientes.objects.all()
    return render_to_response('lista_clientes.html',{'datos':clientes}, context_instance=RequestContext(request))

def lista_ventas(request):
    ventas = Ventas.objects.all()
    return render_to_response('lista_ventas.html',{'datos':ventas}, context_instance=RequestContext(request))

def lista_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render_to_response('lista_proveedores.html',{'datos':proveedores}, context_instance=RequestContext(request))

def lista_categorias(request):
    categorias = Categorias.objects.all()
    return render_to_response('lista_categorias.html',{'datos':categorias}, context_instance=RequestContext(request))

def lista_subcategorias(request):
    subcategorias = Subcategorias.objects.all()
    return render_to_response('lista_subcategorias.html',{'datos':subcategorias}, context_instance=RequestContext(request))

def lista_sucursales(request):
    sucursales = Sucursales.objects.all()
    return render_to_response('lista_sucursales.html',{'datos':sucursales}, context_instance=RequestContext(request))

def lista_zonas(request):
    zonas = Zonas.objects.all()
    return render_to_response('lista_zonas.html',{'datos':zonas}, context_instance=RequestContext(request))

def lista_departamentos(request):
    departamentos = Departamentos.objects.all()
    return render_to_response('lista_departamentos.html',{'datos':departamentos}, context_instance=RequestContext(request))

	
def agregar_producto(request):
    if request.method=='POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('')
    else:
        formulario = ProductoForm()
    return render_to_response('productoform.html',{'formulario':formulario}, context_instance=RequestContext(request))


def agregar_proveedor(request):
    if request.method=='POST':
        formulario = ProveedorForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('')
    else:
        formulario = ProveedorForm()
    return render_to_response('proveedorform.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
def agregar_departamento(request):
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('')
    else:
        formulario = DepartamentoForm()
    return render_to_response('departamentoform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def agregar_zona(request):
    if request.method=='POST':
        formulario = ZonaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('')
    else:
        formulario = ZonaForm()
    return render_to_response('zonaform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def agregar_categoria(request):
    if request.method=='POST':
        formulario = CategoriaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('')
    else:
        formulario = CategoriaForm()
    return render_to_response('categoriaform.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
def agregar_subcategoria(request):
    if request.method=='POST':
        formulario = SubcategoriaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('')
    else:
        formulario = SubcategoriaForm()
    return render_to_response('subcategoriaform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def agregar_cliente(request):
    if request.method=='POST':
        formulario = ClienteForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('')
    else:
        formulario = ClienteForm()
    return render_to_response('clienteform.html',{'formulario':formulario}, context_instance=RequestContext(request))
	
def agregar_sucursal(request):
    if request.method=='POST':
        formulario = SucursalForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('')
    else:
        formulario = SucursalForm()
    return render_to_response('sucursalform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def agregar_venta(request):
    if request.method=='POST':
        formulario = VentasForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('')
    else:
        formulario = VentasForm()
    return render_to_response('ventaform.html',{'formulario':formulario}, context_instance=RequestContext(request))
