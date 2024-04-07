
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('productos_terminados/agregar_registro/', views.productos_terminados_agregar_registro, name='productos_terminados_agregar_registro'),
    path('productos_terminados/registros/', views.productos_terminados, name='productos_terminados_registros'),
    path('productos_terminados/registros/<int:pk>', views.productos_terminados_ver_registro, name='productos_terminados_registro'),
    path('productos_terminados/borrar_registro/<int:pk>', views.productos_terminados_borrar_registro, name='productos_terminados_borrar_registro'),
    path('productos_terminados/', views.productos_terminados_home, name='productos_terminados'),
    path('productos_terminados/registros/<int:pk>/editar', views.productos_terminados_editar_registro, name='productos_terminados_editar_registro'),
    path('productos_terminados/buscar/', views.productos_terminados_buscar_registro, name='productos_terminados_buscar_registro'),
    path('productos_terminados/buscar/descargar_resultados', views.productos_terminados_descargar_resultados, name='productos_terminados_descargar_resultados'),
]
