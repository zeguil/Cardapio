from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#DRF
from rest_framework.routers import DefaultRouter
from rest_framework import permissions

#yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# viewSets
from cardapio.viewsets import CardapioViewSet
from nutricional.viewsets import NutricionalViewSet

router = DefaultRouter()
router.register('cardapio', CardapioViewSet, basename='Cardapio')
router.register('nutricional', NutricionalViewSet)

# configurção do swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Cardapio",
      default_version='v1',
      description="INOVATEC 2020",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contato@autoponia.com.br"),
      license=openapi.License(name="All rights reserved"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# rotas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # faz com que o django abra imagens no navegador