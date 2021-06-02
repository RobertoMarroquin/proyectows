from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'usuario', UsuarioAPI)
router.register(r'rol', RolAPI)
router.register(r'farmacia', FarmaciaAPI)
router.register(r'tipoDocumento', TipoDocumentoAPI)
router.register(r'proveedor', ProveedorAPI)
router.register(r'existenciaBodega', ExistenciaBodegaAPI)
router.register(r'producto', ProductoAPI)
router.register(r'unidadDeMedida', UnidadDeMedidaAPI)
router.register(r'tipoProducto', TipoProductoAPI)
router.register(r'salidaBodega', SalidaBodegaAPI)
router.register(r'catalogoMarca', CatalogoMarcaAPI)
router.register(r'caja', CajaAPI)
router.register(r'movimiento', MovimientoAPI)
router.register(r'tipoMovimiento', TipoMovimientoAPI)

urlpatterns = [
    path('', include(router.urls)),
    path('api-inventario/', include('rest_framework.urls', namespace='rest_framework_inventario')),
]
