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
	class Meta:
		model = Actividades
		fields = '__all__'

		labels = {
					'descripcionactividad': _('Actividad')
		}

class ActividadesEditarForm(ModelForm):
	descripcionactividad = forms.ModelChoiceField(queryset=Actividades.objects.all(), label="Actividad")

	class Meta:
		model = Actividades
		fields = '__all__'

		labels = {
					'descripcionactividad': _('Actividad')
		}

class SubprocesosXEscenariosForm(ModelForm):

	class Meta:
		model = Subprocesosxescenarios
		fields = '__all__'

	    # labels = {
	    # 			'nivel_riesgo_inherente': _('Nivel de Riesgo Inherente')
	    # }

class RACIForm(ModelForm):
	class Meta:
		model = Raci
		fields = '__all__'

		labels = {
					'codRaci': _('RACI')
		}

