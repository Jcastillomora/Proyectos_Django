import datetime
from tokenize import PseudoExtras

from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import UserRegisterForm, VehiculoForm
from .models import Vehiculo


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')

@staff_member_required()
@permission_required(perm='vehiculo.add_vehiculomodel', raise_exception=True)
def vehiculo(request):
    context = {}
    #crear el objeto form
    form = VehiculoForm(request.POST or None, request.FILES or None)
    #verificar si el formulario es valido
    if form.is_valid():
        #guardar los datos del formulario
        form.save()
        return HttpResponseRedirect('/thanks/')
    
    context['form'] = form
    return render(request, 'formulario.html', context)

#vistas para el registro de usuarios
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            content_type = ContentType.objects.get_for_model(Vehiculo)
            visualizar_catalogo = Permission.objects.get(
                codename='visualizar_catalogo',
                content_type=content_type,
            )
            #guardar los datos del formulario
            user = form.save()
            user.user_permissions.add(visualizar_catalogo)
            login(request, user)
            messages.success(request, "Registrado satisfactoriamente")
        else:
            messages.error(request, "Registro invalido. ALgunos datos ingresados no son correctos")
        return HttpResponseRedirect('/index/')
    
    form = UserRegisterForm()
    context = {'register_form': form}
    return render(request, 'registro.html', context)

#vista para el login (no proteger)
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get("password")
            #autenticar al usuario
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesion como: {username}.")
                return HttpResponseRedirect('/index/')
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
                return HttpResponseRedirect('/login/')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            return HttpResponseRedirect('/login/')
    form = AuthenticationForm()
    context = {'login_form': form}
    return render(request, 'login.html', context) 

#vista para el logout (no proteger)
def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/index')

#vista para el catalogo de vehiculos, protegida
@permission_required(perm='vehiculo.visualizar_catalogo', raise_exception=True)
def listar_view(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'listar.html', context)