from django.shortcuts import render
from django.shortcuts import HttpResponse

def inicio(request):
    data = {
        'titulo' : "Inicio"
    }
    return render(request,'base.html',data)

def articulo(request):
    return HttpResponse(html_base +
        """<h2>Mantenimiento de Articulos</h2>
        <p>List de articulos</p>""")

def cliente(request):
    data = {
        'titulo' : 'Gestión de Clientes',
        'crear_url' : '/crearcliente',
        'listar_url' : '/cliente',
    }
    return render(request, "ventas/clientes/listCliente.html", data)

def crearCliente(request):
    data = {
        'titulo' : 'Mantenimiento de Clientes',
        'crer_url':'/crearcliente',
        'action':'add',
        'listar_url': '/cliente',
    }
    return render(request, "ventas/clientes/formCliente.html", data)

def venta(request):
    data = {
        'titulo': "Ventas"
    }
    return render(request, "ventas/ventas.html",data)

# Create your views here.
