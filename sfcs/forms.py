from django.contrib.auth.models import User
from django import forms
from .models import Almacen


class AddRecordForm(forms.ModelForm):
    codigo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Codigo", "class":"form-control"}), label="")
    medida = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Medida", "class":"form-control"}), label="")
    clase = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Clase", "class":"form-control"}), label="")
    unidad = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Unidad", "class":"form-control"}), label="")
    descripcion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Descripcion", "class":"form-control"}), label="")
    valor = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Valor", "class":"form-control"}), label="")
    lista_medidas = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Lista Medidas", "class":"form-control"}), label="")

    class Meta:
        model = Almacen
        exclude = ("user", )