
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('capturar/', views.capturar, name='capturar'),
    path('registros/', views.registros, name='registro'),
    path('registro/<int:pk>', views.ver_registro, name='registro')
]
