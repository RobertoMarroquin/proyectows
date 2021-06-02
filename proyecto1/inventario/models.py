from django.db import models

# Create your models here.
class Usuario(models.Model):
    idUsuario = models.IntegerField(("idUsuario"), primary_key=True)
    nombre = models.CharField(("Nombre"), max_length=80)
    apellido = models.CharField(("Apellido"), max_length=80)
    correo = models.CharField(("Correo"), max_length=80)
    password = models.CharField(("Password"), max_length=256)
    estado = models.IntegerField(("Estado"))
    rol = models.ForeignKey('inventario.Rol', on_delete=models.PROTECT)
    farmacia = models.ForeignKey('inventario.Farmacia', on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Usuario")
        verbose_name_plural =("Usuarios")

    def __str__(self):
        return self.idUsuario


class Rol(models.Model):
    idRol = models.IntegerField(("idRol"), primary_key=True)
    nombreRol = models.CharField(("Nombre Rol"), max_length=80)
    class Meta:
        verbose_name = ("Rol")
        verbose_name_plural = ("Rols")

    def __str__(self):
        return self.idRol


class Farmacia(models.Model):
    idFarmacia = models.IntegerField(("idFarmacia"), primary_key=True)
    nombreFarmacia =models.CharField(("Nombre Farmacia"), max_length=80)
    telefono = models.CharField(("Telefono"), max_length=50)
    estado = models.IntegerField(("Estado"))
    direccionFarmacia = models.CharField(("Direccion Farmacia"), max_length=150)
    departamento = models.CharField(("Departamento"), max_length=80)
    municipio = models.CharField(("Municipio"), max_length=80)

    class Meta:
        verbose_name = ("Farmacia")
        verbose_name_plural = ("Farmacias")

    def __str__(self):
        return self.idFarmacia


class tipoDocumento(models.Model):
    idTipoDocumento = models.IntegerField(("idTipoDocumento"), primary_key=True)
    nombreDocumento = models.CharField(("nombreDocumento"), max_length=30)
    proveedor = models.ForeignKey('inventario.Proveedor', on_delete=models.CASCADE)
    farmacia = models.ForeignKey('inventario.Farmacia', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Tipo Documento")
        verbose_name_plural = ("Tipo Documentos")

    def __str__(self):
        return self.idTipoDocumento


class Proveedor(models.Model):
    idProveedor = models.IntegerField(("idProveedor"), primary_key=True)
    estadoProveedor = models.IntegerField(("Estado Proveedor"))
    numeroDocumento = models.CharField("Numero Documento",max_length = 80)
    nombre = models.CharField("Nombre", max_length=80)
    direccionProveedor = models.CharField("Direccion Proveedor", max_length=150)
    existenciaBodega = models.ManyToManyField("inventario.ExistenciaBodega", verbose_name=("Enxistencias Bodega"))

    class Meta:
        verbose_name = ("Proveedor")
        verbose_name_plural = ("Proveedores")

    def __str__(self):
        return self.idProveedor


class ExistenciaBodega(models.Model):
    idExistenciaBodega = models.IntegerField(("idExistenciaBodega"))
    cantidad = models.FloatField(("cantidad"))
    fechaIngreso = models.DateField(("Fecha Ingreso"), auto_now=False, auto_now_add=False)
    fechaCaducidad = models.DateField(("Fecha Caducidad"), auto_now=False, auto_now_add=False)
    numeroFactura = models.IntegerField(("Nummero Factura"))
    precioUnitario = models.FloatField(("Precio Unitario"))
    realizadoPor = models.CharField(("Realizado Por"), max_length=50)
    tipoIngreso = models.CharField(("Tipo Ingreso"), max_length=50)
    descripcion = models.CharField('Descripcion',max_length = 150)
    farmacia = models.ForeignKey('inventario.Farmacia', on_delete=models.CASCADE)
    producto = models.ForeignKey('inventario.Producto', on_delete=models.CASCADE)
    catalogoMarca = models.ForeignKey("inventario.CatalogoMarca", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'ExistenciaBodega'
        verbose_name_plural = 'ExistenciaBodegas'

    def __str__(self):
        return self.idExistenciaBodega


class Producto(models.Model):
    idProducto = models.IntegerField('idProducto', primary_key=True)
    nombreProducto = models.CharField(("Nombre Producto"), max_length=80)
    descripcion = models.CharField(("Descripcion"), max_length=150)
    presentacion = models.CharField(("Presentacion"), max_length=80)
    estado = models.IntegerField(("Estado"))
    unidadMedida = models.ForeignKey('inventario.UnidadDeMedida', on_delete=models.CASCADE)
    tipoProducto = models.ForeignKey('inventario.TipoProducto', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.idProducto }' # TODO


class UnidadDeMedida(models.Model):
    idUnidad = models.IntegerField('idUnidad',primary_key=True)    
    nombreUnidad = models.CharField(("Nombre Unidad"), max_length=80)
    class Meta:
        verbose_name = 'UnidadDeMedida'
        verbose_name_plural = 'UnidadDeMedidas'

    def __str__(self):
        return f'{self.idUnidad }' # TODO


class TipoProducto(models.Model):
    idTipo = models.IntegerField('idTipo',primary_key=True)
    nombreTipo = models.CharField(("Nombre Tipo"), max_length=150)

    class Meta:
        verbose_name = 'TipoProducto'
        verbose_name_plural = 'TipoProductos'

    def __str__(self):
        return f'{self.idTipo}'


class SalidaBodega(models.Model):
    idSalidadBodega = models.IntegerField('idSalidadBodega',primary_key=True)
    cantidad = models.FloatField(("Cantidad"))
    entregadoA = models.CharField(("Entregado A"), max_length=50)
    observacion = models.CharField(("Observacion"), max_length=50)
    realizadoPor = models.CharField(("Realizado Por"), max_length=50)
    fechaSalida = models.DateField(("Fecha Salida"), auto_now=False, auto_now_add=False)
    existenciaBodega = models.ForeignKey('inventario.ExistenciaBodega', on_delete=models.CASCADE)
    farmacia = models.ForeignKey('inventario.Farmacia', on_delete=models.CASCADE)

    def __str__(self):
        return self.idSalidadBodega

    class Meta:
        verbose_name = 'SalidaBodega'
        verbose_name_plural = 'SalidaBodegas'   


class CatalogoMarca(models.Model):
    idMarca = models.IntegerField(("idMarca"), primary_key=True)
    descripcion = models.CharField(("Descripcion"), max_length=150)
    estado = models.IntegerField(("Estado"))
    nombre = models.CharField(("Nombre"), max_length=80)

    def __str__(self):
        return self.idMarca

    class Meta:
        verbose_name = 'CatalogoMarca'
        verbose_name_plural = 'CatalogoMarcas'  


class Caja(models.Model):
    idCaja = models.IntegerField(("idCaja"),primary_key=True)
    numeroCaja = models.IntegerField(("Numero Caja"))
    nombreCaja = models.CharField('Nombre Caja',max_length = 80)
    efectivoInicial = models.FloatField(("Efectivo Inicial"))
    estadoCaja = models.IntegerField(("Estado Caja"))
    farmacia = models.ForeignKey('inventario.Farmacia', on_delete=models.CASCADE)
    models.OneToOneField("inventario.Usuario", verbose_name=("Caja"), on_delete=models.CASCADE)

    def __str__(self):
        return self.idCaja

    class Meta:
        verbose_name = 'Caja'
        verbose_name_plural = 'Cajas'


class Movimiento(models.Model):
    idMovimiento = models.IntegerField(("idMovimiento"),primary_key=True)
    fecha = models.DateField(("Fecha"), auto_now=False, auto_now_add=False)
    entradaAnterior = models.FloatField(("Entrada Anterior"))
    cantidad = models.FloatField(("Cantidad"))
    entradaActual = models.FloatField(("Entrada Actual"))
    motivoMovimiento = models.CharField(("Motivo"), max_length=256)
    caja = models.ForeignKey('inventario.Caja', on_delete=models.CASCADE)
    tipoMovimiento = models.ForeignKey('inventario.TipoMovimiento', on_delete=models.CASCADE)

    def __str__(self):
        return self.idMovimiento

    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'       


class TipoMovimiento(models.Model):
    idTipoMovimiento = models.IntegerField(("idTipoMovimiento"),primary_key=True)
    nombreTipoMovimiento = models.CharField(("Nombre Tipo Movimiento"), max_length=80)
    def __str__(self):
        return self.idTipoMovimiento

    class Meta:
        verbose_name = 'TipoMovimiento'
        verbose_name_plural = 'TipoMovimientos'
