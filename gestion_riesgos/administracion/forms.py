# -*- coding: utf-8 -*-
from .models import *
from administracion.models import *
from django.forms import ModelForm
from django.forms.widgets import *
from django import forms
from django.contrib.auth.models import *
from django.utils.translation import ugettext_lazy as _



#Form para tipo de Area
class TipoAreaForm(ModelForm):

	#desctipoarea = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
	class Meta:
		model = Tipoareas
		fields = '__all__'

		labels ={
				'codtipoarea': _('Tipo de Area'),
				'desctipoarea': _('Tipo de Area')
		}
class TipoAreaEditarForm(ModelForm):

	desctipoarea = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
	class Meta:
		model = Tipoareas
		fields = '__all__'

		labels ={
				'codtipoarea': _('Tipo de Area'),
				'desctipoarea': _('Tipo de Area')
		}

#Form para Areas
class AreasForm(ModelForm):
	#descarea = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
	class Meta:
		model = Areas
		fields = '__all__'

		labels = {
					'codtipoarea': _('Tipo de Area'),
					'descarea': _('Area')
		}

class AreasEditarForm(ModelForm):
	codarea = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
	class Meta:
		model = Areas
		fields = '__all__'

		labels = {
					'codtipoarea': _('Tipo de Area'),
					'descarea': _('Area'),
					'codarea': _('Area')
		}

#Form para Puestos
class PuestosForm(ModelForm):
	#descpuesto = forms.ModelChoiceField(queryset=Puestos.objects.all(), label="Puesto")
	class Meta:
		model = Puestos
		fields = '__all__'

		labels = {
					'descpuesto': _('Puesto'),
					'codarea': _('Area')
		}

class PuestosEditarForm(ModelForm):
	descpuesto = forms.ModelChoiceField(queryset= Puestos.objects.all(), label="Dueño del Subproceso")
	class Meta:
		model = Puestos
		fields = '__all__'

		labels = {
					'descpuesto': _('Dueño del Subproceso'),
					'codarea': _('Area')
		}

class TipoProcesoForm(ModelForm):
	class Meta:
		model = Tipoproceso
		fields = '__all__'

		labels = {
					'desctipoproceso': _('Tipo de Proceso')
		}

class TipoProcesoEditarForm(ModelForm):
	desctipoproceso = forms.ModelChoiceField(queryset= Tipoproceso.objects.all(), label="Tipo de Proceso")
	class Meta:
		model = Tipoproceso
		fields = '__all__'

class TipoActividadForm(ModelForm):
	class Meta:
		model = Tipoactividad
		fields = '__all__'

		labels = {
					'desctipoactividad': _('Tipo de Actividad')
		}

class TipoActividadEditarForm(ModelForm):
	desctipoactividad = forms.ModelChoiceField(queryset= Tipoactividad.objects.all(), label="Tipo de Actividad")

	class Meta:
		model = Tipoactividad
		fields = '__all__'

class TipoControlForm(ModelForm):
	class Meta:
		model = Tipocontrol
		fields = '__all__'

		labels = {
					'desctipocontrol': _('Tipo de Control')
		}

class TipoControlEditarForm(ModelForm):
	desctipocontrol = forms.ModelChoiceField(queryset= Tipocontrol.objects.all(), label= "Tipo de Control")
	class Meta:
		model = Tipocontrol
		fields = '__all__'

class TipoRaciForm(ModelForm):
	class Meta:
		model = Tiporaci
		fields = '__all__'

class TipoRaciEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset=Tiporaci.objects.all())
	class Meta:
		model = Tiporaci
		fields = '__all__'

class TiposRiesgosForm(ModelForm):
	class Meta:
		model = Tiposriesgos
		fields = '__all__'

		labels = {
					'desctiporiesgo': _('Tipo de Riesgo')
		}

class TiposRiesgosEditarForm(ModelForm):
	desctiporiesgo = forms.ModelChoiceField(queryset= Tiposriesgos.objects.all(), label= 'Tipo de Riesgo')
	class Meta:
		model = Tiposriesgos
		fields = '__all__'

		labels = {
					'desctiporiesgo': _('Tipo de Riesgo')
		}

class EstadosForm(ModelForm):
	descestado = forms.ModelChoiceField(queryset= Estados.objects.all())

	class Meta:
		model = Estados
		fields = '__all__'

		labels = {
					'descestado': _('Estado')
		}

class NaturalezacontrolForm(ModelForm):
	
	class Meta:
		model = Naturalezacontrol
		fields = '__all__'

		labels = {
					'descnaturaleza': _('Naturaleza de Control')
		}

class NaturalezacontrolEditarForm(ModelForm):
	descnaturaleza = forms.ModelChoiceField(queryset= Naturalezacontrol.objects.all())
	class Meta:
		model = Naturalezacontrol
		fields = '__all__'

class EscenarioriesgosForm(ModelForm):

	class Meta:
		model = Escnariosriesgos
		fields = '__all__'

		labels ={
					'descescenario': _('Escenario'),
					'codriesgo': _('Riesgo')
		}

class EscenarioriesgosEditarForm(ModelForm):
	descescenario = forms.ModelChoiceField(queryset= Escnariosriesgos.objects.all())

	class Meta:
		model = Escnariosriesgos
		fields = '__all__'

		labels ={
					'descescenario': _('Escenario'),
					'codriesgo': _('Riesgo')
		}

class RiesgosForm(ModelForm):
	class Meta:
		model = Riesgos
		fields = '__all__'

		labels = {
					'descriesgo': _('Riesgos'),
					'codtiporiesgo': _('Tipo de Riesgo')
		}

class RiesgosEditarForm(ModelForm):
	descriesgo = forms.ModelChoiceField(queryset= Riesgos.objects.all())

	class Meta:
		model = Riesgos
		fields = '__all__'
		
		labels = {
					'descriesgo': _('Riesgos'),
					'codtiporiesgo': _('Tipo de Riesgo')
		}





		





