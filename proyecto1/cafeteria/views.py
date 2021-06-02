from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *


class UsuarioAPI(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]


class TipoPagoAPI(viewsets.ModelViewSet):
    queryset = TipoPago.objects.all()
    serializer_class = TipoPagoSerializer
    permission_classes = [permissions.AllowAny]


class CategoriaProductoAPI(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    permission_classes = [permissions.AllowAny]


class ProveedorAPI(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [permissions.AllowAny]


class UbicacionAPI(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer
    permission_classes = [permissions.AllowAny]


class DetalleProductoAPI(viewsets.ModelViewSet):
    queryset = DetalleProducto.objects.all()
    serializer_class = DetalleProductoSerializer
    permission_classes = [permissions.AllowAny]


class HorarioAPI(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    permission_classes = [permissions.AllowAny]


class RepartidorAPI(viewsets.ModelViewSet):
    queryset = Repartidor.objects.all()
    serializer_class = RepartidorSerializer
    permission_classes = [permissions.AllowAny]


