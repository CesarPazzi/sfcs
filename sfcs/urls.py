
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('inventarios/agregar_registro/', views.inventarios_agregar_registro, name='inventarios_agregar_registro'),
    path('inventarios/registros/', views.inventarios_registros, name='inventarios_registros'),
    path('inventarios/registros/<int:pk>', views.inventarios_ver_registro, name='inventarios_registro'),
    path('inventarios/borrar_registro/<int:pk>', views.inventarios_borrar_registro, name='inventarios_borrar_registro'),
    path('inventarios/', views.inventarios_home, name='inventarios'),
    path('inventarios/registros/<int:pk>/editar', views.inventarios_editar_registro, name='inventarios_editar_registro'),
    path('inventarios/buscar/', views.inventarios_buscar_registro, name='inventarios_buscar_registro'),
]
