from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import *
from .models import *
# Create your views here.

class RolAPI(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [permissions.AllowAny]


class FarmaciaAPI(viewsets.ModelViewSet):
    queryset = Farmacia.objects.all()
    serializer_class = FarmaciaSerializer
    permission_classes = [permissions.AllowAny]


class TipoDocumentoAPI(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoSerializer
    permission_classes = [permissions.AllowAny]


class ProveedorAPI(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [permissions.AllowAny]


class ExistenciaBodegaAPI(viewsets.ModelViewSet):
    queryset = ExistenciaBodega.objects.all()
    serializer_class = ExistenciaBodegaSerializer
    permission_classes = [permissions.AllowAny]


class ProductoAPI(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]


class UnidadDeMedidaAPI(viewsets.ModelViewSet):
    queryset = UnidadDeMedida.objects.all()
    serializer_class = UnidadDeMedidaSerializer
    permission_classes = [permissions.AllowAny]


class TipoProductoAPI(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer
    permission_classes = [permissions.AllowAny]


class SalidaBodegaAPI(viewsets.ModelViewSet):
    queryset = SalidaBodega.objects.all()
    serializer_class = SalidaBodegaSerializer
    permission_classes = [permissions.AllowAny]


class CatalogoMarcaAPI(viewsets.ModelViewSet):
    queryset = CatalogoMarca.objects.all()
    serializer_class = CatalogoMarcaSerializer
    permission_classes = [permissions.AllowAny]


class CajaAPI(viewsets.ModelViewSet):
    queryset = Caja.objects.all()
    serializer_class = CajaSerializer
    permission_classes = [permissions.AllowAny]


class MovimientoAPI(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    permission_classes = [permissions.AllowAny]


class TipoMovimientoAPI(viewsets.ModelViewSet):
    queryset = TipoMovimiento.objects.all()
    serializer_class = TipoMovimientoSerializer
    permission_classes = [permissions.AllowAny]


class UsuarioAPI(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]
