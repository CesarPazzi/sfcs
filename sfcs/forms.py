from django.contrib.auth.models import User
from django import forms
from .models import Almacen


class AddRecordForm(forms.ModelForm):
    codigo = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}))
    medida = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Medida")
    clase = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Clase")
    unidad = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Unidad")
    descripcion = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Descripción")
    valor = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Valor")
    lista_medidas = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Lista Medidas")

    class Meta:
        model = Almacen
        exclude = ("user",)
