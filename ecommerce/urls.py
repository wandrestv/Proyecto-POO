"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Ventas.views import inicio, articulo, cliente, crearCliente, venta
from Nomina_Personal.views import empleado, pagoEmpleado, nomina_personal, proveedor, pagoProveedor, consultaEmpleado, consultaProveedor
from django.conf.urls.static import static
from ecommerce import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('articulo/', articulo, name='articulo'),
    path('cliente/', cliente, name='cliente'),
    path('crearcliente/', crearCliente, name='crearcliente'),
    path('venta/', venta, name='venta'),
    path('empleado/', empleado, name='empleado'),
    path('pagoempleado/', pagoEmpleado, name='pagoempleado'),
    path('nomina_personal', nomina_personal, name='nomina_personal'),
    path('proveedor', proveedor, name='proveedor'),
    path('pagoproveedor', pagoProveedor, name='pagoproveedor'),
    path('consultaempleado', consultaEmpleado, name='consultaempleado'),
    path('consultaproveedor', consultaProveedor, name='consultaproveedor'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
