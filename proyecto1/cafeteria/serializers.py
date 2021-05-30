from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            "nombreUsuario",
            "apelUsuario",
            "telUsuario",
            "direccionUsuario",
            "estadoUsuario",
            "emailUsuario",
            "claveUsuari",
        ]


class TipoPagoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoPago
        fields = [
            "tipoPago",
        ]


class CategoriaProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = [
            "nombreCategoria",
            "descripcionCategoria"
        ]


class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proveedor
        fields = [
            "nombreProveedor",
            "descripcionProveedor",
            "telefonoProveedor",
        ]


class UbicacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ubicacion
        fields = [
            "descripcionubicacion",
        ]


class DetalleProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetalleProducto
        fields = [
            "cantidadProducto",
            "precioProducto",
        ]


class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = [
            "idlocal",
            "dia",
            "apertura",
            "cierre",
        ]
        

class RepartidorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Repartidor
        fields = [
            "idlocal",
            "nombreRepartidor",
            "carneRepartidor",
        ]
