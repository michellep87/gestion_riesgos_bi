from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.urls import reverse
from django.template import Context
from django.contrib.auth import authenticate, login as auth_login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers  import make_password
from django.contrib.auth.models import *
from .models import *


#from general.models import *
from administracion.forms import *

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 


@login_required
def menu_administracion(request):
	return render(request, 'menu_administracion.html', {})

@login_required
def tipo_area(request):
	ctx={}
	formulario = TipoAreaForm()
	listado = Tipoareas.objects.all()
	if request.POST:
		try:

			campos = Tipoareas()
			campos.desctipoarea = request.POST.get('desctipoarea')
			campos.save()

			mensaje = 'exito'
		except Exception as e:
			mensaje = e

		ctx = {
				'formulario': formulario,
				'mensaje': mensaje,
				'listado': listado,
		}
	else:
		#formulario.fields['desctipoarea'] = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
		ctx = {
				'formulario': formulario,
				'listado': listado,
		}
				
	return render(request,'tipo_area_ingreso.html', ctx)

@login_required
def tipo_area_editar(request, id):
	ctx = {}
	instancia = Tipoareas.objects.get(pk=id)
	formularios = TipoAreaForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Tipoareas.objects.get(pk=id)
			campos.desctipoarea = request.POST.get('desctipoarea')
			campos.save()
			

			formularios = TipoAreaForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			raise
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('tipo_area'))

	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'tipo_area_editar.html', ctx)

@login_required
def areas(request):
	ctx = {}
	formulario = AreasForm()
	tipoarea = TipoAreaEditarForm()
	listado = Areas.objects.all()
	if request.POST:
		try:
			campos = Areas()
			campos.descarea = request.POST.get('descarea')
			campos.codtipoarea = None if request.POST.get('codtipoarea') == '' else Tipoareas.objects.get(pk=request.POST.get('codtipoarea'))
			campos.save()

			mensaje = 'exito'
		except Exception as e:
			mensaje = e

		ctx = {
				'formulario': formulario,
				'mensaje': mensaje,
				'listado': listado,
				'tipoarea': tipoarea
		}
	else:
		ctx = {
				'formulario': formulario,
				'listado': listado,
				'tipoarea': tipoarea
		}
	return render(request,'area_ingreso.html', ctx)

@login_required
def areas_editar(request, id):
	ctx = {}
	instancia = Areas.objects.get(pk=id)
	formularios = AreasForm(instance= instancia)
	tipoarea = TipoAreaEditarForm()
	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Areas.objects.get(pk=id)
			campos.descarea = request.POST.get('descarea')
			campos.codtipoarea = None if request.POST.get('codtipoarea') == '' else Tipoareas.objects.get(pk=request.POST.get('codtipoarea'))
			campos.save()
			

			formularios = AreasForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
				'tipoarea': tipoarea,
		}

		return HttpResponseRedirect(reverse('areas'))

	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
				'tipoarea': tipoarea,
		}	
		return render(request,'area_editar.html', ctx)

@login_required
def puestos(request):
	ctx = {}
	formulario = PuestosForm()
	areas = AreasEditarForm()
	listado = Puestos.objects.all()

	if request.POST:
		try:
			campos = Puestos()
			campos.descpuesto = request.POST.get('descpuesto')
			campos.codarea = None if request.POST.get('codarea') == '' else Areas.objects.get(pk=request.POST.get('codarea'))
			campos.save()
			mensaje='exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formulario,
				'areas': areas,
				'listado': listado,
				'mensaje': mensaje,

		}

	else:
		ctx = {
				'formulario': formulario,
				'areas': areas,
				'listado': listado,
		}
	return render(request, 'puesto_ingreso.html',ctx)

@login_required
def puestos_editar(request, id):
	ctx = {}
	instancia = Puestos.objects.get(pk=id)
	formularios = PuestosForm(instance= instancia)
	areas = AreasEditarForm()
	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Puestos.objects.get(pk=id)
			campos.descpuesto = request.POST.get('descpuesto')
			campos.codarea = None if request.POST.get('codarea') == '' else Areas.objects.get(pk=request.POST.get('codarea'))
			campos.save()
			

			formularios = PuestosForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
				'areas': areas,
		}
		return HttpResponseRedirect(reverse('puestos'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
				'areas': areas,
		}	
		return render(request,'puestos_editar.html', ctx)
	
@login_required
def tipoproceso(request):
	formulario = TipoProcesoForm()
	listado = Tipoproceso.objects.all()
	ctx = {}

	if request.POST:
		try:
			campos = Tipoproceso()
			campos.desctipoproceso = request.POST.get('desctipoproceso')
			campos.save()
			mensaje = 'exito'

		except Exception as e:
			mensaje = e

		ctx = {
				'formulario': formulario,
				'listado': listado,
				'mensaje': mensaje,
		}
	else:
			ctx = {
				'formulario': formulario,
				'listado': listado,
			}
	return render(request,'tipo_proceso_ingreso.html',ctx)

@login_required
def tipoproceso_editar(request, id):
	ctx = {}
	instancia = Tipoproceso.objects.get(pk=id)
	formularios = TipoProcesoForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Tipoproceso.objects.get(pk=id)
			campos.desctipoproceso = request.POST.get('desctipoproceso')
			campos.save()
			

			formularios = TipoProcesoForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('tipoproceso'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'tipo_proceso_editar.html', ctx)

@login_required
def tipoactividad(request):
	formulario = TipoActividadForm()
	listado = Tipoactividad.objects.all()
	ctx = {}

	if request.POST:
		try:
			campos = Tipoactividad()
			campos.desctipoactividad = request.POST.get('desctipoactividad')
			campos.save()
			mensaje = 'exito'

		except Exception as e:
			mensaje = e

		ctx = {
				'formulario': formulario,
				'listado': listado,
				'mensaje': mensaje,
		}
	else:
			ctx = {
				'formulario': formulario,
				'listado': listado,
			}
	return render(request,'tipo_actividad_ingreso.html',ctx)

@login_required
def tipoactividad_editar(request, id):
	ctx = {}
	instancia = Tipoactividad.objects.get(pk=id)
	formularios = TipoActividadForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Tipoactividad.objects.get(pk=id)
			campos.desctipoactividad = request.POST.get('desctipoactividad')
			campos.save()
			

			formularios = TipoActividadForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('tipoactividad'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'tipo_actividad_editar.html', ctx)


@login_required
def tipocontrol(request):
	formulario = TipoControlForm()
	listado = Tipocontrol.objects.all()
	ctx = {}

	if request.POST:
		try:
			campos = Tipocontrol()
			campos.desctipocontrol = request.POST.get('desctipocontrol')
			campos.save()
			mensaje = 'exito'

		except Exception as e:
			mensaje = e

		ctx = {
				'formulario': formulario,
				'listado': listado,
				'mensaje': mensaje,
		}
	else:
			ctx = {
				'formulario': formulario,
				'listado': listado,
			}
	return render(request,'tipo_control_ingreso.html',ctx)

@login_required
def tipocontrol_editar(request, id):
	ctx = {}
	instancia = Tipocontrol.objects.get(pk=id)
	formularios = TipoControlForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Tipocontrol.objects.get(pk=id)
			campos.desctipocontrol = request.POST.get('desctipocontrol')
			campos.save()
			

			formularios = TipoControlForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('tipocontrol'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'tipo_control_editar.html', ctx)

@login_required
def tiporaci(request):
	formulario = TipoRaciForm()
	listado = Tiporaci.objects.all()
	ctx = {}

	if request.POST:
		try:
			campos = Tiporaci()
			campos.descripcion = request.POST.get('descripcion')
			campos.save()
			mensaje = 'exito'

		except Exception as e:
			mensaje = e

		ctx = {
				'formulario': formulario,
				'listado': listado,
				'mensaje': mensaje,
		}
	else:
			ctx = {
				'formulario': formulario,
				'listado': listado,
			}
	return render(request,'tipo_raci_ingreso.html',ctx)

@login_required
def tiporaci_editar(request, id):
	ctx = {}
	instancia = Tiporaci.objects.get(pk=id)
	formularios = TipoRaciForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Tiporaci.objects.get(pk=id)
			campos.descripcion = request.POST.get('descripcion')
			campos.save()
			

			formularios = TipoRaciForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('tiporaci'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'tipo_raci_editar.html', ctx)


@login_required
def tiporiesgos(request):
	formulario = TiposRiesgosForm()
	listado = Tiposriesgos.objects.all()
	ctx = {}

	if request.POST:
		try:
			campos = Tiposriesgos()
			campos.desctiporiesgo = request.POST.get('desctiporiesgo')
			campos.save()
			mensaje = 'exito'

		except Exception as e:
			mensaje = e

		ctx = {
				'formulario': formulario,
				'listado': listado,
				'mensaje': mensaje,
		}
	else:
			ctx = {
				'formulario': formulario,
				'listado': listado,
			}
	return render(request,'tipo_riesgos_ingreso.html',ctx)

@login_required
def tiporiesgos_editar(request, id):
	ctx = {}
	instancia = Tiposriesgos.objects.get(pk=id)
	formularios = TiposRiesgosForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Tiposriesgos.objects.get(pk=id)
			campos.desctiporiesgo = request.POST.get('desctiporiesgo')
			campos.save()
			

			formularios = TiposRiesgosForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('tiporiesgos'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'tipo_riesgos_editar.html', ctx)

@login_required
def riesgos(request):
	formulario = RiesgosForm()
	tiporiesgo = TiposRiesgosEditarForm()
	listado = Riesgos.objects.all()
	ctx = {}

	if request.POST:
		try:
			campos = Riesgos()
			campos.codtiporiesgo =  None if request.POST.get('codtiporiesgo') == '' else Tiposriesgos.objects.get(pk=request.POST.get('codtiporiesgo'))
			campos.descriesgo = request.POST.get('descriesgo')
			campos.save()
			mensaje = 'exito'

		except Exception as e:
			mensaje = e

		ctx = {
				'formulario': formulario,
				'listado': listado,
				'mensaje': mensaje,
		}
	else:
			ctx = {
				'formulario': formulario,
				'listado': listado,
			}
	return render(request,'riesgos_ingreso.html',ctx)

@login_required
def riesgos_editar(request, id):
	ctx = {}
	instancia = Riesgos.objects.get(pk=id)
	formularios = RiesgosForm(instance= instancia)
	tiporiesgo = TiposRiesgosEditarForm()

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Riesgos.objects.get(pk=id)
			campos.codtiporiesgo =  None if request.POST.get('codtiporiesgo') == '' else Tiposriesgos.objects.get(pk=request.POST.get('codtiporiesgo'))
			campos.descriesgo = request.POST.get('descriesgo')
			campos.save()
			

			formularios = RiesgosForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
				'tiporiesgo': tiporiesgo,
		}
		return HttpResponseRedirect(reverse('riesgos'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
				'tiporiesgo': tiporiesgo,
		}	
		return render(request,'riesgos_editar.html', ctx)

@login_required
def naturalezacontrol(request):
	formulario = NaturalezacontrolForm()
	ctx = {}
	listado = Naturalezacontrol.objects.all()

	if request.POST:
		try:
			campos = Naturalezacontrol()
			campos.descnaturaleza = request.POST.get('descnaturaleza')
			campos.save()

			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formulario,
				'listado': listado,
				'mensaje': mensaje,
		}
	else:
		ctx = {
				'formulario': formulario,
				'listado': listado,
		}
	return render (request,'naturaleza_control_ingreso.html', ctx)

@login_required
def naturalezacontrol_editar(request, id):
	ctx = {}
	instancia = Naturalezacontrol.objects.get(pk=id)
	formularios = NaturalezacontrolForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Naturalezacontrol.objects.get(pk=id)
			campos.descnaturaleza = request.POST.get('descnaturaleza')
			campos.save()
			

			formularios = NaturalezacontrolForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('naturalezacontrol'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'naturaleza_control_editar.html', ctx)

@login_required
def escenarioriesgos(request):
	formulario = EscenarioriesgosForm()
	riesgos = RiesgosEditarForm()
	ctx = {}
	listado = Escnariosriesgos.objects.all()

	if request.POST:
		try:
			campos = Escnariosriesgos()
			campos.codriesgo = None if request.POST.get('codriesgo') == '' else Riesgos.objects.get(pk=request.POST.get('codriesgo'))
			campos.descescenario = request.POST.get('descescenario')
			campos.save()

			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formulario,
				'listado': listado,
				'mensaje': mensaje,
				'riesgos': riesgos,
		}
	else:
		ctx = {
				'formulario': formulario,
				'listado': listado,
				'riesgos': riesgos,
		}
	return render (request,'escenario_riesgos_ingreso.html', ctx)

@login_required
def escenarioriesgos_editar(request, id):
	ctx = {}
	instancia = Escnariosriesgos.objects.get(pk=id)
	formularios = EscenarioriesgosForm(instance= instancia)
	riesgos = RiesgosEditarForm()
	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Escnariosriesgos.objects.get(pk=id)
			campos.codriesgo = None if request.POST.get('codriesgo') == '' else Riesgos.objects.get(pk=request.POST.get('codriesgo'))#request.POST.get('codriesgo')
			campos.descescenario = request.POST.get('descescenario')
			campos.save()
			

			formularios = EscenarioriesgosForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
				'riesgos': riesgos,
		}
		return HttpResponseRedirect(reverse('escenarioriesgos'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
				'riesgos': riesgos,
		}	
		return render(request,'escenario_riesgos_editar.html', ctx)

import json
def ajax(request):
	if request.is_ajax():
		codtipoarea = request.GET['codtipoarea']
	data = list(Tipoareas.objects.values('CodArea', 'DescArea').filter(CodTipoArea=CodTipoArea))
	return HttpResponse(json.dumps(data), content_type='application/json')