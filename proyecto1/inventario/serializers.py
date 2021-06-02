from rest_framework import serializers
from .models import *

class  TipoMovimientoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  TipoMovimiento
        fields = [  
            "idTipoMovimiento",
            "nombreTipoMovimiento",
        ]


class  MovimientoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Movimiento
        fields = [  
            "idMovimiento",
            "fecha",
            "entradaAnterior",
            "cantidad",
            "entradaActual",
            "motivoMovimiento",
            "caja",
            "tipoMovimiento",
        ]


class  CajaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Caja
        fields = [
            "idCaja",
            "numeroCaja",
            "nombreCaja",
            "efectivoInicial",
            "estadoCaja",
            "farmacia",
            "usuario",
        ]


class  CatalogoMarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogoMarca 
        fields = [
            "idMarca",
            "descripcion",
            "estado",
            "nombre",
        ]


class  SalidaBodegaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  SalidaBodega
        fields = [
            "idSalidadBodega",
            "cantidad",
            "entregadoA",
            "observacion",
            "realizadoPor",
            "fechaSalida",
            "existenciaBodega",
            "farmacia",
        ]


class  TipoProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoProducto 
        fields = [
            "idTipo",
            "nombreTipo",
        ]


class  UnidadDeMedidaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnidadDeMedida 
        fields = [
            "idUnidad",
            "nombreUnidad",
        ]


class  ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Producto
        fields = [
            "idProducto",
            "nombreProducto",
            "descripcion",
            "presentacion",
            "estado",
            "unidadMedida",
            "tipoProducto",
            ]


class  ExistenciaBodegaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  ExistenciaBodega
        fields = [
            'idExistenciaBodega',
            "cantidad",
            "fechaIngreso",
            "fechaCaducidad",
            "numeroFactura",
            "precioUnitario",
            "realizadoPor",
            "tipoIngreso",
            "descripcion",
            "farmacia",
            "producto",
            "catalogoMarca",
        ]


class  ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Proveedor
        fields = [
            "idProveedor",
            "estadoProveedor",
            "numeroDocumento",
            "nombre",
            "direccionProveedor",
            "existenciaBodega",
        ]


class  TipoDocumentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  TipoDocumento
        fields = [
            "idTipoDocumento",
            "nombreDocumento",
            "proveedor",
            "farmacia",
        ]


class  FarmaciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Farmacia
        fields = [
            "idFarmacia",
            "nombreFarmacia",
            "telefono",
            "estado",
            "direccionFarmacia",
            "departamento",
            "municipio",
        ]


class  UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =  Usuario
        fields = [
            "idUsuario",
            "nombre",
            "apellido",
            "correo",
            "password",
            "estado",
            "rol",
            "farmacia",
        ]


class  RolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rol 
        fields = [
            "idRol",
            "nombreRol",
        ]

