from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from calculadora.views import index, guardar_operacion_api, guardar_ruta_api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/guardar/', guardar_operacion_api, name='guardar_operacion_api'),
    path('api/guardar-ruta/', guardar_ruta_api, name='guardar_ruta_api'), # <-- ¡Esta es la línea que faltaba!
]

# Permite servir imágenes y audios desde la carpeta /media/
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)