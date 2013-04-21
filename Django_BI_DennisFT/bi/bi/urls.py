from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bi.views.home', name='home'),
    # url(r'^bi/', include('bi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	
	url(r'^addproducto$','inventario.views.agregar_producto'),
	url(r'^addcliente$','inventario.views.agregar_cliente'),
	url(r'^adddepartamento$','inventario.views.agregar_departamento'),
	url(r'^addzona$','inventario.views.agregar_zona'),
	url(r'^addcategoria$','inventario.views.agregar_categoria'),
	url(r'^addsubcategoria$','inventario.views.agregar_subcategoria'),
	url(r'^addproveedor$','inventario.views.agregar_proveedor'),
	url(r'^addventa$','inventario.views.agregar_venta'),
	url(r'^addsucursal$','inventario.views.agregar_sucursal'),
	
	url(r'^productos$','inventario.views.lista_productos'),
	url(r'^clientes$','inventario.views.lista_clientes'),
	url(r'^departamentos$','inventario.views.lista_departamentos'),
	url(r'^zonas$','inventario.views.lista_zonas'),
	url(r'^categorias$','inventario.views.lista_categorias'),
	url(r'^proveedores$','inventario.views.lista_proveedores'),
	url(r'^subcategorias$','inventario.views.lista_subcategorias'),
	url(r'^ventas$','inventario.views.lista_ventas'),
	url(r'^sucursales$','inventario.views.lista_sucursales'),
	
	
	
)
