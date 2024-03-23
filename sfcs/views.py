from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Almacen
from .forms import AddRecordForm

# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST['usuario']
        password = request.POST['password']

        #Auth
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            mensaje_success = ("haz iniciado sesion correctamente!")
            messages.success(request, mensaje_success)
            print ("usuario loggeado")
            return redirect('home')
        else:
            messages.error(request, "Usuario o Password incorrectos!")
            print ("error al loggearse")
            return redirect('home')

    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.warning(request, "Haz cerrado sesion!")
    return redirect('home')

def capturar(request):
    return redirect('home')
    # if request.method == "POST":
    #     inv_codigo = request.POST['codigo']
    #     inv_medida = request.POST['medida']
    #     inv_clase = request.POST['clase']
    #     inv_unidad = request.POST['unidad']
    #     inv_descripcion = request.POST['descripcion']
    #     inv_valor = request.POST['valor']
    #     inv_listamedidas = request.POST['listamedidas']



    # mensaje_success = ("haz iniciado sesion correctamente!")
    # messages.success(request, mensaje_success)
    # print ("usuario loggeado")

    # return render(request, 'capturar.html')



def registros(request):
    registros = Almacen.objects.all()
    return render(request, 'registro.html', {'registros': registros})

def ver_registro(request, pk):
    if request.user.is_authenticated:
        #Ver registro
        registro = Almacen.objects.get(id=pk)
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no ha iniciado sesion para ver esa pagina")
        return redirect('home')
    return render(request, 'ver_registro.html', {'registro': registro})
