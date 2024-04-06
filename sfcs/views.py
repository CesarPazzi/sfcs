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

# VER TODOS LOS REGISTROS
def productos_terminados(request):
    if request.user.is_authenticated:
        registros = Almacen.objects.all()
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no ha iniciado sesion para ver esa pagina")
        return redirect('home')
    return render(request, 'productos_terminados/registro.html', {'registros': registros})


# VER REGISTRO INDIVIDUAL
def productos_terminados_ver_registro(request, pk):
    if request.user.is_authenticated:
        registro = Almacen.objects.get(id=pk)
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no ha iniciado sesion para ver esa pagina")
        return redirect('home')
    return render(request, 'productos_terminados/ver_registro.html', {'registro': registro})

# BORRAR REGISTRO
def productos_terminados_borrar_registro(request, pk):
    if request.user.is_authenticated:
        registro = Almacen.objects.get(id=pk)
        registro.delete()
        messages.error(request, "Registro eliminado correctamente!")
        print ("registro borrado")
        return redirect('productos_terminados')
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no ha iniciado sesion para ver esa pagina")
        return redirect('home')

# CAPTURAR REGISTRO
def productos_terminados_agregar_registro(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                agregar_registro = form.save()
                messages.success(request, "Registro agregado correctamente!")
                return redirect('productos_terminados')
        return render(request, 'productos_terminados/agregar_registro.html', {'form': form})
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no se ha iniciado sesion para ver esa pagina")
        return redirect('home')
    
def productos_terminados_home(request):
    return render(request, 'productos_terminados/productos_terminados.html', {})

# EDITAR REGISTRO
def productos_terminados_editar_registro(request, pk):
    if request.user.is_authenticated:
        registro = Almacen.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=registro)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro editado correctamente!")
            return redirect('../%d' % registro.id)
        return render(request, 'productos_terminados/editar_registro.html', {'form':form, 'registro': registro})
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no ha iniciado sesion para ver esa pagina")
        return redirect('home')
    
def productos_terminados_buscar_registro(request):
    if request.method == 'POST':
            busqueda = request.POST['busqueda']
            # busqueda exacta de la busqueda de la descripcion del registro en el modelo
            # https://docs.djangoproject.com/en/4.0/ref/models/querysets/#std-fieldlookup-exact
            resultados = Almacen.objects.filter(descripcion__contains=busqueda)
            return render(request, 'productos_terminados/buscar.html', {'busqueda':busqueda, 'resultados':resultados})
    else:
        return render(request, 'productos_terminados/buscar.html',{})