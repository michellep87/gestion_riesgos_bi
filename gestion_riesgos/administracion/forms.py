# -*- coding: utf-8 -*-
from .models import *
from administracion.models import *
from procesos.models import *
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
	descpuesto = forms.ModelMultipleChoiceField(queryset= Puestos.objects.all(), label="Dueño")
	class Meta:
		model = Puestos
		fields = '__all__'

		labels = {
					'descpuesto': _('Dueño'),
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
	letra = forms.ModelChoiceField(queryset=Tiporaci.objects.all())
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

class RiesgoInstitucionalForm(ModelForm):
	
	class Meta:
		model = RiesgoInstitucional
		fields = '__all__'

		labels = {
					'descripcion': _('Riesgo')
		}

class RiesgoInstitucionalEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset= RiesgoInstitucional.objects.all(), label='Riesgo Institucional')
	class Meta:
		model = RiesgoInstitucional
		fields = '__all__'

class RiesgoReputacionalForm(ModelForm):
	
	class Meta:
		model = RiesgoReputacional
		fields = '__all__'

		labels = {
					'descripcion': _('Riesgo')
		}

class RiesgoReputacionalEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset= RiesgoReputacional.objects.all(), label='Riesgo Reputacional')
	class Meta:
		model = RiesgoReputacional
		fields = '__all__'

class FrecuenciaActividadesRelacionadasRiesgoForm(ModelForm):
	
	class Meta:
		model = FrecuenciaActividadesRelacionadasRiesgo
		fields = '__all__'

		labels = {
					'descripcion': _('Frecuencia')
		}

class FrecuenciaActividadesRelacionadasRiesgoEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset= FrecuenciaActividadesRelacionadasRiesgo.objects.all())
	class Meta:
		model = FrecuenciaActividadesRelacionadasRiesgo
		fields = '__all__'


class FrecuenciaControlForm(ModelForm):
	
	class Meta:
		model = FrecuenciaControl
		fields = '__all__'

		labels = {
					'descripcion': _('Frecuencia')
		}

class FrecuenciaControlEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset= FrecuenciaControl.objects.all(), label='Frecuencia de las actividades relacionadas con el riesgo')
	class Meta:
		model = FrecuenciaControl
		fields = '__all__'

class AreasInvolucradasForm(ModelForm):
	
	class Meta:
		model = AreasInvolucradas
		fields = '__all__'

		labels = {
					'descripcion': _('Areas')
		}

class AreasInvolucradasEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset= AreasInvolucradas.objects.all(), label='Áreas Involucradas')
	class Meta:
		model = AreasInvolucradas
		fields = '__all__'


class ObservacionesAuditoriaForm(ModelForm):
	
	class Meta:
		model = ObservacionesAuditoria
		fields = '__all__'

		labels = {
					'descripcion': _('Descripcion')
		}

class ObservacionesAuditoriaEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset= ObservacionesAuditoria.objects.all())
	class Meta:
		model = ObservacionesAuditoria
		fields = '__all__'

class DefinicionProcesoForm(ModelForm):
	
	class Meta:
		model = DefinicionProceso
		fields = '__all__'

		labels = {
					'descripcion': _('Definicion')
		}

class DefinicionProcesoEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset= DefinicionProceso.objects.all(), label='Definición de un proceso')
	class Meta:
		model = DefinicionProceso
		fields = '__all__'

class CumplimientoNormativoForm(ModelForm):
	
	class Meta:
		model = CumplimientoNormativo
		fields = '__all__'

		labels = {
					'descripcion': _('Descripcion')
		}

class CumplimientoNormativoEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset= CumplimientoNormativo.objects.all(), label='Cumplimiento normativo')
	class Meta:
		model = CumplimientoNormativo
		fields = '__all__'

class EventosRiesgoForm(ModelForm):
	
	class Meta:
		model = EventosRiesgo
		fields = '__all__'

		labels = {
					'descripcion': _('Evento')
		}

class EventosRiesgoEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset= EventosRiesgo.objects.all(), label='Eventos de Riesgo ultimos 12 meses')
	class Meta:
		model = EventosRiesgo
		fields = '__all__'


class TransaccionesEstadosFinancierosForm(ModelForm):
	
	class Meta:
		model = TransaccionesEstadosFinancieros
		fields = '__all__'

		labels = {
					'descripcion': _('Transaccion')
		}

class TransaccionesEstadosFinancierosEditarForm(ModelForm):
	descripcion = forms.ModelChoiceField(queryset= TransaccionesEstadosFinancieros.objects.all(), label='Transacciones relacionadas a los Estados Financieros')
	class Meta:
		model = EventosRiesgo
		fields = '__all__'

class CriteriosControlForm(ModelForm):
	
	class Meta:
		model = Puntajescriterioscontrol
		fields = '__all__'

class CriteriosImpactoForm(ModelForm):
	
	class Meta:
		model = PuntajesCriteriosImpacto
		fields = '__all__'


class CriteriosProbabilidadForm(ModelForm):
	
	class Meta:
		model = PuntajesCriteriosProbabilidad
		fields = '__all__'

class EscalaControldForm(ModelForm):
	
	class Meta:
		model = EscalaControl
		fields = '__all__'

class EscalaControlEspecialForm(ModelForm):
	
	class Meta:
		model = EscalaControlEspecial
		fields = '__all__'

class EscalaImpactoForm(ModelForm):
	
	class Meta:
		model = Escalaimpacto
		fields = '__all__'

class EscalaImpactoEspecialForm(ModelForm):
	
	class Meta:
		model = EscalaImpactoEspecial
		fields = '__all__'

class EscalaProbabilidadForm(ModelForm):
	
	class Meta:
		model = Escalaprobabilidad
		fields = '__all__'

class EscalaProbabilidadEspecialForm(ModelForm):
	
	class Meta:
		model = EscalaProbabilidadEspecial
		fields = '__all__'

class ZonariesgoForm(ModelForm):
	class Meta:
		model = Zonariesgo
		fields= '__all__'

class ZonaRiesgoEspecialForm(ModelForm):
	class Meta:
		model = ZonaRiesgoEspecial
		fields= '__all__'

class CategoriaRiesgosForm(ModelForm):
	class Meta:
		model = CategoriaRiesgos
		fields= '__all__'

		labels = {
					'codcategoria': _('Codigo de Categoria')
		}


		




		





