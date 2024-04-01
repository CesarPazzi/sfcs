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
def inventarios_registros(request):
    if request.user.is_authenticated:
        registros = Almacen.objects.all()
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no ha iniciado sesion para ver esa pagina")
        return redirect('home')
    return render(request, 'inventarios/registro.html', {'registros': registros})


# VER REGISTRO INDIVIDUAL
def inventarios_ver_registro(request, pk):
    if request.user.is_authenticated:
        registro = Almacen.objects.get(id=pk)
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no ha iniciado sesion para ver esa pagina")
        return redirect('home')
    return render(request, 'inventarios/ver_registro.html', {'registro': registro})

# BORRAR REGISTRO
def inventarios_borrar_registro(request, pk):
    if request.user.is_authenticated:
        registro = Almacen.objects.get(id=pk)
        registro.delete()
        messages.error(request, "Registro eliminado correctamente!")
        print ("registro borrado")
        return redirect('inventarios_registros')
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no ha iniciado sesion para ver esa pagina")
        return redirect('home')

# CAPTURAR REGISTRO
def inventarios_agregar_registro(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                agregar_registro = form.save()
                messages.success(request, "Registro agregado correctamente!")
                return redirect('inventarios_registros')
        return render(request, 'inventarios/agregar_registro.html', {'form': form})
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no se ha iniciado sesion para ver esa pagina")
        return redirect('home')
    
def inventarios_home(request):
    return render(request, 'inventarios/inventarios.html', {})

# EDITAR REGISTRO
def inventarios_editar_registro(request, pk):
    if request.user.is_authenticated:
        registro = Almacen.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=registro)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro editado correctamente!")
            return redirect('../%d' % registro.id)
        return render(request, 'inventarios/editar_registro.html', {'form':form, 'registro': registro})
    else:
        messages.error(request, "Debes de iniciar sesion!")
        print ("no ha iniciado sesion para ver esa pagina")
        return redirect('home')
    
def inventarios_buscar_registro(request):
    if request.user.is_authenticated:
        form = AddRecordForm(request.POST or None)
        if form.is_valid():
            pass
        return render(request, 'inventarios/buscar.html', {})
    else:
        # Si el usuario no esta autenticado
        pass