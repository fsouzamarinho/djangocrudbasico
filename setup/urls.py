from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('estados/', include('estados.urls')),
    path('', include('cidades.urls')),
]
