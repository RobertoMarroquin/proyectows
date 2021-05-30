from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombreUsuario = models.CharField('Nombre',max_length = 50,blank=True, null=True)
    apelUsuario = models.CharField('Apellido',max_length=50,blank=True, null=True)
    telUsuario = models.CharField('Telefono',max_length = 8,blank=True, null=True)
    direccionUsuario = models.CharField("Direccion",max_length =50,blank=True, null=True)
    estadoUsuario = models.IntegerField('Estado',blank=True, null=True)
    emailUsuario = models.EmailField(("Email"), max_length=254,blank=True, null=True)
    claveUsuari = models.CharField(("Clave"), max_length=50,blank=True, null=True)

    class Meta:
        verbose_name = ("Usuario")
        verbose_name_plural = ("Usuarios")

    def __str__(self):
        return f'{self.nombreUsuario} {self.apelUsuario}'


class TipoPago(models.Model):
    tipoPago = models.CharField(("Tipo Pago"), max_length=30,blank=True, null=True)
    
    class Meta:
        verbose_name = ("TipoPago")
        verbose_name_plural = ("TipoPagos")

    def __str__(self):
        return self.tipoPago


class CategoriaProducto(models.Model):
    nombreCategoria = models.CharField(("Nombre Categoria"), max_length=30,blank=True, null=True)
    descripcionCategoria = models.CharField('Descripcion de Categoria',max_length = 30,blank=True, null=True)
    
    class Meta:
        verbose_name = ("Categoriaproducto")
        verbose_name_plural = ("Categoriaproductos")

    def __str__(self):
        return self.nombreCategoria


class Proveedor(models.Model):
    nombreProveedor  = models.CharField(max_length=50, blank=True, null=True)
    descripcionProveedor = models.CharField(max_length=50, blank=True, null=True)
    telefonoProveedor = models.CharField(max_length=8,blank=True, null=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return f'{self.nombreProveedor}'


class Repartidor(models.Model):
    idlocal = models.IntegerField('Local',blank=True, null=True)
    nombreRepartidor = models.CharField(("Nombre"), max_length=50,blank=True, null=True)
    carneRepartidor = models.CharField(("Carne"), max_length=50,blank=True, null=True)

    class Meta:
        verbose_name = ("Repartidor")
        verbose_name_plural = ("Repartidores")

    def __str__(self):
        return self.carneRepartidor


class Ubicacion(models.Model):
    descripcionubicacion =  models.CharField('Descripcion',max_length = 50,blank=True, null=True)
    
    class Meta:
        verbose_name = ("Ubicacion")
        verbose_name_plural = ("Ubicaciones")

    def __str__(self):
        return self.descripcionubicacion


class DetalleProducto(models.Model):
    cantidadProducto = models.IntegerField(("Cantidad de Producto"))
    precioProducto = models.CharField('Precio',max_length = 150,blank=True,null=True)

    class Meta:
        verbose_name = ("Detalle Producto")
        verbose_name_plural = ("Detalle Productos")

    def __str__(self):
        return f'{self.cantidadProducto} {self.cantidadProducto}'


class Horario(models.Model):
    idlocal = models.IntegerField(("id Local"),blank=True, null=True)
    dia = models.CharField('Dia',max_length=10,blank=True, null=True)
    apertura = models.CharField(("Apertura"), max_length=10, blank=True, null=True)
    cierre = models.CharField(("Cierre"), max_length=10, blank=True, null=True)
    
    class Meta:
        verbose_name = ("Horario")
        verbose_name_plural = ("Horarios")

    def __str__(self):
        return f'{self.dia} {self.idlocal}'
        