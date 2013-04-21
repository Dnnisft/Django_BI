from django.db import models

class Clientes(models.Model):
  codigocliente = models.CharField(max_length=7, unique=True)
  nombre1 = models.CharField(max_length=60)
  nombre2 = models.CharField(max_length=60)
  apellido1 = models.CharField(max_length=60)
  apellido2 = models.CharField(max_length=60)
  apellidocasada = models.CharField(max_length=60, blank=True)
  genero = models.CharField(max_length=1)
  estadocivil = models.CharField(max_length=15, blank = True)
  fechanacimiento = models.DateField(blank = True)
  estadocivil = models.CharField(max_length=15, blank = True)
  telefono1 = models.IntegerField(max_length=8, blank = True)
  telefono2 = models.IntegerField(max_length=8, blank = True)
  Fecha_registro = models.DateTimeField(auto_now=True)
  codigodepartamento = models.ForeignKey('Departamentos')
	
	
  def __unicode__(self):
      return self.codigocliente
	  
class Departamentos(models.Model):
  codigodepartamento = models.CharField(max_length=4, unique=True)
  nombredepartamento = models.CharField(max_length=30)
  codigozona = models.ForeignKey('Zonas')
 
 
  def __unicode__(self):
      return self.codigodepartamento

class Ventas(models.Model):
  codigoventa = models.CharField(max_length=7, unique=True)
  codigocliente = models.ForeignKey('Clientes')
  Fecha_registro = models.DateTimeField(auto_now=True)
  totalventa = models.DecimalField(max_digits=10, decimal_places = 2)
  codigosucursal = models.ForeignKey('Sucursales')
	
  def __unicode__(self):
      return self.codigoventa
	  
class Ventasxproductos(models.Model):
  codigoventa = models.ForeignKey('Ventas')
  codigoproducto = models.ForeignKey('Productos')
  totalventa = models.IntegerField()
	
	
  def __unicode__(self):
      return self.totalventa
	  
class Productos(models.Model):
  codigoproducto = models.CharField(max_length=7, unique=True)
  nombreproducto = models.CharField(max_length=60)
  descripcionproducto = models.TextField(blank=True)
  codigosubcategoria = models.ForeignKey('Subcategorias')
  preciocosto = models.DecimalField (max_digits=10, decimal_places = 2)
  Preciounitario = models.DecimalField(max_digits=10, decimal_places = 2)
  unidades_stock = models.IntegerField()
  codigoproveedor = models.ForeignKey('Proveedores')
  
  def __unicode__(self):
      return self.codigoproducto
	  
class Subcategorias(models.Model):
  codigosubcategoria = models.CharField(max_length=7, unique=True)
  nombresubcategoria = models.CharField(max_length=30)
  descripcionsubcategoria = models.TextField(blank=True)
  codigocategoria = models.ForeignKey('Categorias')
 
  def __unicode__(self):
      return self.codigosubcategoria
	  
class Categorias(models.Model):
  codigocategoria = models.CharField(max_length=7, unique=True)
  nombrecategoria = models.CharField(max_length=30)
  descripcioncategoria = models.TextField(blank=True)
  
  def __unicode__(self):
      return self.codigocategoria
	  
class Proveedores(models.Model):
  codigoproveedor = models.CharField(max_length=7, unique=True)
  nombreproveedor = models.CharField(max_length=30)
  representanteproveedor = models.CharField(max_length=30)
  codigoDepartamento = models.ForeignKey('Departamentos')
  telefono1proveedor = models.IntegerField(max_length=8)
  telefono2proveedor = models.IntegerField(max_length=8, blank=True)	
  
  def __unicode__(self):
      return self.codigoproveedor

class Sucursales(models.Model):
  codigosucursal = models.CharField(max_length=4, unique=True)
  nombresucursal = models.CharField(max_length=30)
  codigoDepartamento = models.ForeignKey('Departamentos')
  
  def __unicode__(self):
      return self.codigosucursal

class Zonas(models.Model):
  codigozona = models.CharField(max_length=4, unique=True)
  nombrezona = models.CharField(max_length=25)
  def __unicode__(self):
      return self.codigozona

