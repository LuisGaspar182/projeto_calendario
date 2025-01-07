from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TatuadorViewSet, ClienteViewSet, TatuagemViewSet

router = DefaultRouter()
router.register('tatuadores', TatuadorViewSet)
router.register('clientes', ClienteViewSet)
router.register('tatuagens', TatuagemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
