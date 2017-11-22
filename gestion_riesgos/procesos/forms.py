# -*- coding: utf-8 -*-
from .models import *
from administracion.models import *
from procesos.models import *
from django.forms import ModelForm
from django.forms.widgets import *
from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import *
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import CheckboxSelectMultiple


class ProcesosForm(ModelForm):

	fecha_implementacion = forms.DateField(widgets.AdminDateWidget())
	
	class Meta:
		model = Procesos
		exclude = ['logo']

		labels = {
					'codtipoproceso': _('Tipo de Proceso'),
					'idduenoproceso': unicode('Dueño del Proceso','utf8')
		}

class ProcesosEditarForm(ModelForm):
	nombre_proceso = forms.ModelChoiceField(queryset = Procesos.objects.all())
	#fecha_implementacion = forms.DateField(widget=forms.TextInput(attrs= { 'class':'daterangepicker' }))
	
	class Meta:
		model = Procesos
		fields = '__all__'

		labels = {
					'codtipoproceso': _('Tipo de Proceso'),
					'idduenoproceso': unicode('Dueño del Proceso','utf8')
					# unicode('El usuario y/o contraseña son incorrectos','utf8'),
		}

class SubprocesosForm(ModelForm):
	due_osubproceso = forms.ModelChoiceField(queryset = Puestos.objects.all(), label='Dueño del Subproceso')
	narrativa= forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Subprocesos
		fields = '__all__'

		labels = {
					'descsubproceso': _('Descripcion de Subproceso'),
					'due_osubproceso': _('Dueño del Subproceso')
		}

class SubprocesosEditarForm(ModelForm):
	descsubproceso = forms.ModelChoiceField(queryset= Subprocesos.objects.all(), label = 'Descripcion de Subproceso')

	class Meta:
		model = Subprocesos
		fields = '__all__'

		labels = {
					'descsubproceso': _('Subproceso'),
					'due_osubproceso': _('Dueño del Subproceso')
		}


class ActividadesForm(ModelForm):
	descripcionactividad = forms.CharField(widget=forms.Textarea, label="Descripcion")
	
	class Meta:
		model = Actividades
		fields = '__all__'

		labels = {
					'nombreactividad': _('Nombre de la Actividad'),
					'ordenactividad': _('Orden de la Actividad')
		}

class ActividadesEditarForm(ModelForm):
	nombreactividad = forms.ModelChoiceField(queryset=Actividades.objects.all(), label="Actividad")
	descripcionactividad = forms.CharField(widget=forms.Textarea, label="Descripcion Actividad")	

	class Meta:
		model = Actividades
		fields = '__all__'

		labels = {
					'nombreactividad': _('Nombre de la Actividad')
					
		}

class SubprocesosXEscenariosForm(ModelForm):
	codsubproceso=forms.ModelChoiceField(queryset=Subprocesos.objects.all(), label="Subproceso")
	categoria_riesgo=forms.ModelChoiceField(queryset=CategoriaRiesgos.objects.all(), label="Categoria de Riesgos")
	class Meta:
		model = Subprocesosxescenarios
		fields = '__all__'

		label = {
				'linea_negocio_nivel1': _('Linea de Negocio 1'),
				'linea_negocio_nivel2': _('Linea de Negocio 2')
		}

class SubprocesosXEscenariosEditarForm(ModelForm):
	codsubproceso=forms.ModelChoiceField(queryset=Subprocesos.objects.all(), label="Subproceso")
	escenario = forms.ModelChoiceField(queryset=Subprocesosxescenarios.objects.all(), label="Escenario de Riesgo")
	class Meta:
		model = Subprocesosxescenarios
		fields = '__all__'

		label = {
				'linea_negocio_nivel1': _('Linea de Negocio 1'),
				'linea_negocio_nivel2': _('Linea de Negocio 2')
		}

	    

class RACIForm(ModelForm):
	class Meta:
		model = Raci
		fields = '__all__'

		labels = {
					'codRaci': _('RACI')
		}

class ControlesForm(ModelForm):
	codactividad = forms.ModelChoiceField(queryset=Actividades.objects.all(), label="Actividad")
	descripcion = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Controles
		fields = '__all__'



class InformacionForm(ModelForm):
	introduccion = forms.CharField(widget=forms.Textarea)
	objetivos = forms.CharField(widget=forms.Textarea)
	alcance = forms.CharField(widget=forms.Textarea)
	responsabilidad = forms.CharField(widget=forms.Textarea)
	revision = forms.CharField(widget=forms.Textarea)
	cumplimiento = forms.CharField(widget=forms.Textarea)
	excepciones = forms.CharField(widget=forms.Textarea)
	definiciones = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = InformacionGeneral
		fields = '__all__'

class UnidadesMedidaForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset=UnidadesMedida.objects.all(), label="Unidad de Medida")

	class Meta:
		model = UnidadesMedida
		fields = '__all__'

class UnidadesMedidaIngresoForm(ModelForm):
	

	class Meta:
		model = UnidadesMedida
		fields = '__all__'


class CedulaNormativaForm(ModelForm):
	circular = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = CedulaNormativa
		fields = '__all__'

class IndicadoresDesempenioForm(ModelForm):
	definicion = forms.CharField(widget=forms.Textarea)
	aceptable = forms.CharField(widget=forms.Textarea)
	inaceptable = forms.CharField(widget=forms.Textarea)


	class Meta:
		model = IndicadoresDesempenio
		fields = '__all__'

		labels = {
				'descripcion': _('Indicador de Gestion')
		}

class ImagenesSubprocesosForm(ModelForm):

	class Meta:
		model = ImagenesSubprocesos
		fields = '__all__'
