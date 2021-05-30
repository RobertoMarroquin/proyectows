from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioAPI)
router.register(r'tipoPago', TipoPagoAPI)
router.register(r'categoriaProducto', CategoriaProductoAPI)
router.register(r'proveedor', ProveedorAPI)
router.register(r'repartidor', RepartidorAPI)
router.register(r'ubicacion', UbicacionAPI)
router.register(r'detalleProducto', DetalleProductoAPI)
router.register(r'horario', HorarioAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('api-cafeteria/', include('rest_framework.urls', namespace='rest_framework')),
]
