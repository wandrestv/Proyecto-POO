from django.shortcuts import render

def empleado(request):
    data = {
        'titulo' : 'Pago de Empleados',
        'crear_url' : '/pagoempleado',
        'listar_url' : '/empleado',
    }
    return render(request, "nomina_personal/empleados/listEmpleados.html", data)

def pagoEmpleado(request):
    data = {
        'titulo' : 'Nómina de Pago',
        'crear_url':'/pagoempleado',
        'action':'add',
        'listar_url': '/empleado',
    }
    return render(request, "nomina_personal/empleados/formEmpleado.html", data)

def consultaEmpleado(request):
    data = {
        'titulo' : 'Consulta Pago de Empleados',
        'crear_url':'/consultaempleado',
        'action':'add',
        'listar_url': '/empleado',
    }
    return render(request, "nomina_personal/empleados/consulta_pago.html", data)

def nomina_personal(request):
    data = {
        'titulo' : "Tesorería"
    }
    return render(request, "nomina_personal/nomina_persona.html",data)

def proveedor(request):
    data = {
        'titulo' : 'Pago de Proveedores',
        'crear_url' : '/pagoproveedor',
        'listar_url' : '/proveedor',
    }
    return render(request, "nomina_personal/proveedores/listProveedores.html", data)

def pagoProveedor(request):
    data = {
        'titulo' : 'Pago de Proveedores',
        'crear_url':'/pagoproveedor',
        'action':'add',
        'listar_url': '/proveedor',
    }
    return render(request, "nomina_personal/proveedores/formProveedor.html", data)

def consultaProveedor(request):
    data = {
        'titulo' : 'Consulta Pago de Proveedores',
        'crear_url':'/consultaproveedor',
        'action':'add',
        'listar_url': '/proveedor',
    }
    return render(request, "nomina_personal/proveedores/consulta_pago.html", data)

# Create your views here.
