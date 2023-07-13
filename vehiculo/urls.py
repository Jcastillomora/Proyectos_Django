from django.urls import path

from .views import (index, listar_view, login_view, logout_view, register_view,
                    vehiculo)

urlpatterns = [
    path('', index, name='index'),
    path('index/', index, name='index'),
    path('vehiculo/add/', vehiculo, name='agregar'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('listar/', listar_view, name='listar')
]
