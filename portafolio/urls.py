from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from web.sitemaps import StaticViewSitemap  # ⬅️ Asegúrate de crear este archivo

# Diccionario de sitemaps registrados
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),  # Mantiene la app web
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),  
    
]
