from django.shortcuts import render, redirect
from .models import Producto

from django.http import JsonResponse
from .forms import productoForm
#from .forms import productoForm
# Create your views here.


def lista_productos(request):
    #bd findAll
    productos = Producto.objects.all()

    #parsear datos a un dict

    data=[
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen':p.imagen
        }
        for p in productos
    ]

    return JsonResponse(data, safe=False)

def ver_productos(request):
    return render(request,'ver.html')

def agregar_producto(request):
    if request.method == 'POST':
        form = productoForm(request.POST)
        if form.is_valid():
            #guarda en db
            form.save()
            return redirect('ver')
    else:
        form = productoForm()
    return render(request,'agregar.html',{'form':form})