from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'usuario', Usuario)
router.register(r'rol', Rol)
router.register(r'farmacia', Farmacia)
router.register(r'tipoDocumento', TipoDocumento)
router.register(r'proveedor', Proveedor)
router.register(r'existenciaBodega', ExistenciaBodega)
router.register(r'producto', Producto)
router.register(r'unidadDeMedida', UnidadDeMedida)
router.register(r'tipoProducto', TipoProducto)
router.register(r'salidaBodega', SalidaBodega)
router.register(r'catalogoMarca', CatalogoMarca)
router.register(r'caja', Caja)
router.register(r'movimiento', Movimiento)
router.register(r'tipoMovimiento', TipoMovimiento)

urlpatterns = [
    path('', include(router.urls)),
    path('api-inventario/', include('rest_framework.urls', namespace='rest_framework')),
]
