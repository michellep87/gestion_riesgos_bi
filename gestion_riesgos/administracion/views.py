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

from datetime import datetime, date,time, timedelta


#from general.models import *
from administracion.forms import *
from procesos.forms import *

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
			print "aqui ta"
			campos = Areas()
			campos.descarea = request.POST.get('descarea')
			campos.codtipoarea = None if request.POST.get('desctipoarea') == '' else Tipoareas.objects.get(pk=request.POST.get('desctipoarea'))
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
	
	listado = Tipoproceso.objects.filter(habilitado=True).order_by('-periodo')
	ctx = {}

	if request.POST:
		try:
			campos = Tipoproceso()
			campos.desctipoproceso = request.POST.get('desctipoproceso')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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

			campo = Tipoproceso.objects.get(pk=id)
			campo.habilitado= False
			campo.save()

			campos = Tipoproceso()
			campos.desctipoproceso = request.POST.get('desctipoproceso')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	
	listado = Tipocontrol.objects.filter(habilitado=True).order_by('-periodo')
	ctx = {}

	if request.POST:
		try:
			campos = Tipocontrol()
			campos.desctipocontrol = request.POST.get('desctipocontrol')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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

			campo = Tipocontrol.objects.get(pk=id)
			campo.habilitado= False
			campo.save()

			campos = Tipocontrol()
			campos.desctipocontrol = request.POST.get('desctipocontrol')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
			campos.letra = request.POST.get('letra')
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
			campos.letra = request.POST.get('letra')
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
def categoriariesgos(request):
	formulario = CategoriaRiesgosForm()
	listado = CategoriaRiesgos.objects.all()
	ctx = {}

	if request.POST:
		try:
			campos = CategoriaRiesgos()
			campos.codcategoria = request.POST.get('codcategoria') 
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
	return render(request,'riesgos_ingreso.html',ctx)

@login_required
def categoriariesgos_editar(request, id):
	ctx = {}
	instancia = CategoriaRiesgos.objects.get(pk=id)
	formularios = CategoriaRiesgosForm(instance= instancia)
	

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = CategoriaRiesgos.objects.get(pk=id)
			campos.codcategoria = request.POST.get('codcategoria') 
			campos.descripcion = request.POST.get('descripcion')
			campos.save()
			

			formularios = CategoriaRiesgosForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
				
		}
		return HttpResponseRedirect(reverse('categoriariesgos'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
				
		}	
		return render(request,'riesgos_editar.html', ctx)

@login_required
def naturalezacontrol(request):
	formulario = NaturalezacontrolForm()
	ctx = {}
	
	listado = Naturalezacontrol.objects.filter(habilitado=True).order_by('-periodo')

	if request.POST:
		try:
			campos = Naturalezacontrol()
			campos.descnaturaleza = request.POST.get('descnaturaleza')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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

			campo = Naturalezacontrol.objects.get(pk=id)
			campo.habilitado= False
			campo.save()

			campos = Naturalezacontrol()
			campos.descnaturaleza = request.POST.get('descnaturaleza')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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

@login_required
def riesgoinstitucional(request):
	formulario = RiesgoInstitucionalForm()
	ctx = {}
	listado = RiesgoInstitucional.objects.filter(habilitado=True).order_by('-periodo')

	if request.POST:
		try:
			campos = RiesgoInstitucional()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	return render (request,'RiesgoInstitucional_ingreso.html', ctx)

@login_required
def riesgoinstitucional_editar(request, id):
	ctx = {}
	instancia = RiesgoInstitucional.objects.get(pk=id)
	formularios = RiesgoInstitucionalForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:

			campo = RiesgoInstitucional.objects.get(pk=id)
			campo.habilitado= False
			campo.save()

			campos = RiesgoInstitucional()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
			campos.save()
			

			formularios = RiesgoInstitucionalForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('riesgoinstitucional'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'RiesgoInstitucional_editar.html', ctx)

@login_required
def riesgoreputacional(request):
	formulario = RiesgoReputacionalForm()
	ctx = {}
	listado = RiesgoReputacional.objects.filter(habilitado=True).order_by('-periodo')


	if request.POST:
		try:
			campos = RiesgoReputacional()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	return render (request,'RiesgoReputacional_ingreso.html', ctx)

@login_required
def riesgoreputacional_editar(request, id):
	ctx = {}
	instancia = RiesgoReputacional.objects.get(pk=id)
	formularios = RiesgoReputacionalForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:

			campo = RiesgoReputacional.objects.get(pk=id)
			campo.habilitado= False
			campo.save()

			campos = RiesgoReputacional()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
			campos.save()
			

			formularios = RiesgoReputacionalForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('riesgoreputacional'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'RiesgoReputacional_editar.html', ctx)

@login_required
def frecuenciaactividades(request):
	formulario = FrecuenciaActividadesRelacionadasRiesgoForm()
	ctx = {}
	listado = FrecuenciaActividadesRelacionadasRiesgo.objects.filter(habilitado=True).order_by('-periodo')
	
	if request.POST:
		try:
			campos = FrecuenciaActividadesRelacionadasRiesgo()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	return render (request,'frecuencia_actividades_riesgos.html', ctx)

@login_required
def frecuenciaactividades_editar(request, id):
	ctx = {}
	instancia = FrecuenciaActividadesRelacionadasRiesgo.objects.get(pk=id)
	formularios = FrecuenciaActividadesRelacionadasRiesgoForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:

			campos = FrecuenciaActividadesRelacionadasRiesgo.objects.get(pk=id)
			campos.habilitado= False
			campos.save()

			campo = FrecuenciaActividadesRelacionadasRiesgo()
			campo.descripcion = request.POST.get('descripcion')
			campo.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campo.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campo.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campo.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campo.habilitado= True
			campo.periodo = datetime.now()
			campo.save()
			

			formularios = RiesgoReputacionalForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('frecuenciaactividades'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'frecuencia_actividades_riesgos_editar.html', ctx)

@login_required
def frecuenciacontroles(request):
	formulario = FrecuenciaControlForm()
	ctx = {}
	listado = FrecuenciaControl.objects.filter(habilitado=True).order_by('-periodo')
	
	if request.POST:
		try:
			campos = FrecuenciaControl()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	return render (request,'frecuencia_control.html', ctx)

@login_required
def frecuenciacontroles_editar(request, id):
	ctx = {}
	instancia = FrecuenciaControl.objects.get(pk=id)
	formularios = FrecuenciaControlForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:


			campo = FrecuenciaControl.objects.get(pk=id)
			campo.habilitado= False
			campo.save()

			campos = FrecuenciaControl()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
			campos.save()
			

			formularios = FrecuenciaControlForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('frecuenciacontroles'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'frecuencia_control_editar.html', ctx)

@login_required
def areasinvolucradas(request):
	formulario = AreasInvolucradasForm()
	ctx = {}
	#listado = AreasInvolucradas.objects.all()
	listado = AreasInvolucradas.objects.filter(habilitado=True).order_by('-periodo')

	if request.POST:
		try:
			campos = AreasInvolucradas()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	return render (request,'areas_involucradas.html', ctx)

@login_required
def areasinvolucradas_editar(request, id):
	ctx = {}
	instancia = AreasInvolucradas.objects.get(pk=id)
	formularios = AreasInvolucradasForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = AreasInvolucradas.objects.get(pk=id)
			campos.habilitado= False
			campos.save()

			campo = AreasInvolucradas()
			campo.descripcion = request.POST.get('descripcion')
			campo.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campo.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campo.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campo.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campo.habilitado= True
			campo.periodo = datetime.now()
			campo.save()
			

			formularios = AreasInvolucradasForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
				'instancia': instancia,
		}
		return HttpResponseRedirect(reverse('areasinvolucradas'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
				'instancia': instancia,
		}	
		return render(request,'areas_involucradas_editar.html', ctx)

@login_required
def observacionesauditoria(request):
	formulario = ObservacionesAuditoriaForm()
	ctx = {}
	listado = ObservacionesAuditoria.objects.filter(habilitado=True).order_by('-periodo')
	

	if request.POST:
		try:
			campos = ObservacionesAuditoria()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	return render (request,'observaciones_auditoria.html', ctx)

@login_required
def observacionesauditoria_editar(request, id):
	ctx = {}
	instancia = ObservacionesAuditoria.objects.get(pk=id)
	formularios = ObservacionesAuditoriaForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:

			campo = ObservacionesAuditoria.objects.get(pk=id)
			campo.habilitado= False
			campo.save()

			campos = ObservacionesAuditoria()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
			campos.save()
			

			formularios = ObservacionesAuditoriaForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('observacionesauditoria'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'observaciones_auditoria_editar.html', ctx)

@login_required
def definicionproceso(request):
	formulario = DefinicionProcesoForm()
	ctx = {}
	listado = DefinicionProceso.objects.filter(habilitado=True).order_by('-periodo')


	if request.POST:
		try:
			campos = DefinicionProceso()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	return render (request,'definicion_procesos.html', ctx)

@login_required
def definicionproceso_editar(request, id):
	ctx = {}
	instancia = DefinicionProceso.objects.get(pk=id)
	formularios = DefinicionProcesoForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campo = DefinicionProceso.objects.get(pk=id)
			campo.habilitado= False
			campo.save()


			campos = DefinicionProceso()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
			campos.save()
			

			formularios = DefinicionProcesoForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('definicionproceso'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'definicion_procesos_editar.html', ctx)

@login_required
def cumplimientonormativo(request):
	formulario = CumplimientoNormativoForm()
	ctx = {}
	listado = CumplimientoNormativo.objects.filter(habilitado=True).order_by('-periodo')

	if request.POST:
		try:
			campos = CumplimientoNormativo()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	return render (request,'cumplimiento_normativo.html', ctx)

@login_required
def cumplimientonormativo_editar(request, id):
	ctx = {}
	instancia = CumplimientoNormativo.objects.get(pk=id)
	formularios = CumplimientoNormativoForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:

			campos = CumplimientoNormativo.objects.get(pk=id)
			campos.habilitado= False
			campos.save()

			campo = CumplimientoNormativo()
			campo.descripcion = request.POST.get('descripcion')
			campo.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campo.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campo.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campo.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campo.habilitado= True
			campo.periodo = datetime.now()
			campo.save()
			

			formularios = CumplimientoNormativoForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('cumplimientonormativo'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'cumplimiento_normativo_editar.html', ctx)

@login_required
def eventosriesgo(request):
	formulario = EventosRiesgoForm()
	ctx = {}
	listado = EventosRiesgo.objects.filter(habilitado=True).order_by('-periodo')


	if request.POST:
		try:
			campos = EventosRiesgo()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	return render (request,'eventos_riesgo.html', ctx)

@login_required
def eventosriesgo_editar(request, id):
	ctx = {}
	instancia = EventosRiesgo.objects.get(pk=id)
	formularios = EventosRiesgoForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campo = EventosRiesgo.objects.get(pk=id)
			campo.habilitado= False
			campo.save()

			campos = EventosRiesgo()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
			campos.save()
			

			formularios = EventosRiesgoForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('eventosriesgo'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'eventos_riesgo_editar.html', ctx)

@login_required
def transaccionesestadosfinancieros(request):
	formulario = TransaccionesEstadosFinancierosForm()
	ctx = {}
	listado = TransaccionesEstadosFinancieros.objects.filter(habilitado=True).order_by('-periodo')


	if request.POST:
		try:
			campos = TransaccionesEstadosFinancieros()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
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
	return render (request,'transacciones_estados_financieros.html', ctx)

@login_required
def transaccionesestadosfinancieros_editar(request, id):
	ctx = {}
	instancia = TransaccionesEstadosFinancieros.objects.get(pk=id)
	formularios = TransaccionesEstadosFinancierosForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:

			campo = TransaccionesEstadosFinancieros.objects.get(pk=id)
			campo.habilitado= False
			campo.save()

			campos = TransaccionesEstadosFinancieros()
			campos.descripcion = request.POST.get('descripcion')
			campos.porcentaje = None if(request.POST.get('porcentaje'))=="" else request.POST.get('porcentaje')
			campos.ponderacion = None if(request.POST.get('ponderacion'))=="" else request.POST.get('ponderacion')
			campos.porcentaje_especial= None if(request.POST.get('porcentaje_especial'))== "" else request.POST.get('porcentaje_especial')
			campos.ponderacion_especial = None if(request.POST.get('ponderacion_especial'))== "" else request.POST.get('ponderacion_especial')
			campos.habilitado= True
			campos.periodo = datetime.now()
			campos.save()
			

			formularios = TransaccionesEstadosFinancierosForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('transaccionesestadosfinancieros'))
	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'transacciones_estados_financieros_editar.html', ctx)

@login_required
def unidad_medida(request):
	ctx={}
	formulario = UnidadesMedidaIngresoForm()
	listado = UnidadesMedida.objects.all()
	if request.POST:
		try:

			campos = UnidadesMedida()
			campos.descripcion = request.POST.get('descripcion')
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
				
	return render(request,'unidad_medida_ingreso.html', ctx)

@login_required
def unidad_medida_editar(request, id):
	ctx = {}
	instancia = UnidadesMedida.objects.get(pk=id)
	formularios = UnidadesMedidaIngresoForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = UnidadesMedida.objects.get(pk=id)
			campos.descripcion = request.POST.get('descripcion')
			campos.save()
			

			formularios = UnidadesMedidaIngresoForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			raise
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('unidad_medida'))

	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'unidad_medida_editar.html', ctx)

@login_required
def criterios_control(request):
	ctx={}
	#formulario = CriteriosControlForm()
	#fechaMax=Puntajesxcriterios.objects.latest('periodo')
	listado = Puntajesxcriterios.objects.filter(criterio__tipo="CONTROL",habilitado=True).order_by('criterio',)
	if request.POST:
		try:

			# Guardar Criterio
			campo=Criterios()
			campo.criterio=request.POST.get('criterio')
			campo.tipo="CONTROL"
			campo.save()

			#Ingresar su Puntaje
			
			campos = Puntajesxcriterios()
			campos.criterio = None if(campo.pk)=="" else Criterios.objects.get(pk=campo.pk) 
			campos.puntaje=request.POST.get('puntaje')
			campos.puntaje_especial=request.POST.get('puntajeespecial')
			campos.habilitado=True
			campos.periodo = datetime.now()
			#campos.periodo=request.POST.get('periodo')
			campos.save()

			mensaje = 'exito'
		except Exception as e:
			mensaje = e

		ctx = {
				#'formulario': formulario,
				'mensaje': mensaje,
				'listado': listado,
		}
	else:
		#formulario.fields['desctipoarea'] = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
		ctx = {
				#'formulario': formulario,
				'listado': listado,
		}
				
	return render(request,'criterios_control_ingreso.html', ctx)

@login_required
def criterios_control_editar(request, id):
	ctx = {}
	instancia = Puntajesxcriterios.objects.get(pk=id)#Puntajescriterioscontrol.objects.get(pk=id)
	formularios = PuntajesxcriteriosForm(instance=instancia)#CriteriosControlForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			#Guardar Criterio
			# campo=Criterios.objects.get(pk=request.POST.get('criterio'))
			# campo.criterio=request.POST.get('criterioname')
			# campo.save()

			#Inhabilitamos la opcion anterior
			campo = Puntajesxcriterios.objects.get(pk=id)
			campo.habilitado=False
			campo.save()

			campos = Puntajesxcriterios()#Puntajesxcriterios.objects.get(pk=id)
			campos.criterio = None if(request.POST.get('criterio'))=="" else Criterios.objects.get(pk=request.POST.get('criterio')) 
			campos.puntaje=request.POST.get('puntaje')
			campos.puntaje_especial=request.POST.get('puntaje_especial')
			campos.habilitado=True
			campos.periodo = datetime.now()
			# campos.periodo=request.POST.get('periodo')
			campos.save()
			

			formularios = PuntajesxcriteriosForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			raise
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
				'instancia': instancia,
		}
		return HttpResponseRedirect(reverse('criterios_control'))

	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
				'instancia': instancia,
		}	
		return render(request,'criterios_control_editar.html', ctx)

@login_required
def criterios_impacto(request):
	ctx={}
	#formulario = CriteriosImpactoForm()
	listado = listado = Puntajesxcriterios.objects.filter(criterio__tipo="IMPACTO",habilitado=True).order_by('criterio',)
	if request.POST:
		try:

			# Guardar Criterio
			campo=Criterios()
			campo.criterio=request.POST.get('criterio')
			campo.tipo="IMPACTO"
			campo.save()

			#Ingresar su Puntaje
			
			campos = Puntajesxcriterios()
			campos.criterio = None if(campo.pk)=="" else Criterios.objects.get(pk=campo.pk) 
			campos.puntaje=request.POST.get('puntaje')
			campos.puntaje_especial=request.POST.get('puntajeespecial')
			#campos.periodo=request.POST.get('periodo')
			campos.habilitado=True
			campos.periodo = datetime.now()
			campos.save()

			mensaje = 'exito'
		except Exception as e:
			mensaje = e

		ctx = {
				#'formulario': formulario,
				'mensaje': mensaje,
				'listado': listado,
		}
	else:
		#formulario.fields['desctipoarea'] = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
		ctx = {
				#'formulario': formulario,
				'listado': listado,
		}
				
	return render(request,'criterios_impacto_ingreso.html', ctx)

@login_required
def criterios_impacto_editar(request, id):
	ctx = {}
	instancia = Puntajesxcriterios.objects.get(pk=id)
	formularios = PuntajesxcriteriosForm(instance=instancia)#CriteriosImpactoForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			#Guardar Criterio
			# campo=Criterios.objects.get(pk=request.POST.get('criterio'))
			# campo.criterio=request.POST.get('criterioname')
			# campo.save()

			#Inhabilitamos la opcion anterior
			campo = Puntajesxcriterios.objects.get(pk=id)
			campo.habilitado=False
			campo.save()

			campos = Puntajesxcriterios()
			campos.criterio = None if(request.POST.get('criterio'))=="" else Criterios.objects.get(pk=request.POST.get('criterio')) 
			campos.puntaje=request.POST.get('puntaje')
			campos.puntaje_especial=request.POST.get('puntaje_especial')
			campos.habilitado=True
			campos.periodo = datetime.now()
			#campos.periodo=request.POST.get('periodo')

			campos.save()
			

			formularios = PuntajesxcriteriosForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			raise
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
				'instancia': instancia,
		}
		return HttpResponseRedirect(reverse('criterios_impacto'))

	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
				'instancia': instancia,
		}	
		return render(request,'criterios_impacto_editar.html', ctx)

@login_required
def criterios_probabilidad(request):
	ctx={}
	#formulario = CriteriosProbabilidadForm()
	listado = listado = Puntajesxcriterios.objects.filter(criterio__tipo="PROBABILIDAD",habilitado=True).order_by('criterio',)
	#listado = PuntajesCriteriosProbabilidad.objects.all()
	if request.POST:
		try:

			# Guardar Criterio
			campo=Criterios()
			campo.criterio=request.POST.get('criterio')
			campo.tipo="PROBABILIDAD"
			campo.save()

			#Ingresar su Puntaje
			
			campos = Puntajesxcriterios()
			campos.criterio = None if(campo.pk)=="" else Criterios.objects.get(pk=campo.pk) 
			campos.puntaje=request.POST.get('puntaje')
			campos.puntaje_especial=request.POST.get('puntajeespecial')
			#campos.periodo=request.POST.get('periodo')
			campos.habilitado=True
			campos.save()

			mensaje = 'exito'
		except Exception as e:
			mensaje = e

		ctx = {
				#'formulario': formulario,
				'mensaje': mensaje,
				'listado': listado,
		}
	else:
		#formulario.fields['desctipoarea'] = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
		ctx = {
				#'formulario': formulario,
				'listado': listado,
		}
				
	return render(request,'criterios_probabilidad_ingreso.html', ctx)

@login_required
def criterios_probabilidad_editar(request, id):
	ctx = {}
	instancia = Puntajesxcriterios.objects.get(pk=id)
	formularios = PuntajesxcriteriosForm(instance=instancia)#CriteriosProbabilidadForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			#Guardar Criterio
			# campo=Criterios.objects.get(pk=request.POST.get('criterio'))
			# campo.criterio=request.POST.get('criterioname')
			# campo.save()

			#Inhabilitamos la opcion anterior
			campo = Puntajesxcriterios.objects.get(pk=id)
			campo.habilitado=False
			campo.save()

			campos = Puntajesxcriterios()
			campos.criterio = None if(request.POST.get('criterio'))=="" else Criterios.objects.get(pk=request.POST.get('criterio')) 
			campos.puntaje=request.POST.get('puntaje')
			campos.puntaje_especial=request.POST.get('puntaje_especial')
			campos.habilitado=True
			#campos.periodo=request.POST.get('periodo')

			campos.save()
			

			formularios = PuntajesxcriteriosForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			raise
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
				'instancia': instancia,
		}
		return HttpResponseRedirect(reverse('criterios_probabilidad'))

	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
				'instancia': instancia,
		}	
		return render(request,'criterios_probabilidad_editar.html', ctx)

@login_required
def zonas_ingreso(request):
	ctx={}
	formulario = ZonariesgoForm()
	listado = Zonariesgo.objects.all()
	if request.POST:
		try:

			campos = Zonariesgo()
			campos.escala = request.POST.get('escala')
			campos.clasificacion=request.POST.get('clasificacion')
			campos.desde=request.POST.get('desde')
			campos.hasta=request.POST.get('hasta')
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
				
	return render(request,'zona_riesgo.html', ctx)

@login_required
def zonas_editar(request,id):
	ctx={}
	instancia=Zonariesgo.objects.get(pk=id)
	formulario = ZonariesgoForm(instance=instancia)
	
	if request.POST:
		try:

			campos = Zonariesgo.objects.get(pk=id)
			campos.escala = request.POST.get('escala')
			campos.clasificacion=request.POST.get('clasificacion')
			campos.desde=request.POST.get('desde')
			campos.hasta=request.POST.get('hasta')
			campos.save()
			formulario = ZonariesgoForm(instance=campos)

			mensaje = 'exito'
		except Exception as e:
			mensaje = e

		ctx = {
				'formulario': formulario,
				'mensaje': mensaje,
				
		}
		return HttpResponseRedirect(reverse('zonas_ingreso'))
	else:
		#formulario.fields['desctipoarea'] = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
		ctx = {
				'formulario': formulario,
				
		}
				
	return render(request,'zona_riesgo_editar.html', ctx)

@login_required
def escala_control(request):
	ctx={}
	formulario = EscalaControldForm()
	listado = EscalaControl.objects.all()
	if request.POST:
		try:

			campos = EscalaControl()
			campos.escala = None if(request.POST.get('escala'))=="" else request.POST.get('escala')
			campos.desde=request.POST.get('desde')
			campos.hasta=request.POST.get('hasta')
			campos.clasificacion=request.POST.get('clasificacion')
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
				
	return render(request,'escala_control_ingreso.html', ctx)

@login_required
def escala_control_editar(request, id):
	ctx = {}
	instancia = EscalaControl.objects.get(pk=id)
	formularios = EscalaControldForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = EscalaControl.objects.get(pk=id)
			campos.escala = None if(request.POST.get('escala'))=='' else request.POST.get('escala')
			campos.desde=request.POST.get('desde')
			campos.hasta=request.POST.get('hasta')
			campos.clasificacion=request.POST.get('clasificacion')
			campos.save()
			

			formularios = EscalaControldForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			raise
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('escala_control'))

	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'escala_control_editar.html', ctx)


@login_required
def escala_impacto(request):
	ctx={}
	formulario = EscalaImpactoForm()
	listado = Escalaimpacto.objects.all()
	if request.POST:
		try:

			campos = Escalaimpacto()
			campos.escala = None if(request.POST.get('escala'))=="" else request.POST.get('escala')
			campos.desde=request.POST.get('desde')
			campos.hasta=request.POST.get('hasta')
			campos.clasificacion=request.POST.get('clasificacion')
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
				
	return render(request,'escala_impacto_ingreso.html', ctx)

@login_required
def escala_impacto_editar(request, id):
	ctx = {}
	instancia = Escalaimpacto.objects.get(pk=id)
	formularios = EscalaImpactoForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Escalaimpacto.objects.get(pk=id)
			campos.escala = None if(request.POST.get('escala'))=='' else request.POST.get('escala')
			campos.desde=request.POST.get('desde')
			campos.hasta=request.POST.get('hasta')
			campos.clasificacion=request.POST.get('clasificacion')
			campos.save()
			

			formularios = EscalaImpactoForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			raise
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('escala_impacto'))

	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'escala_impacto_editar.html', ctx)


@login_required
def escala_probabilidad(request):
	ctx={}
	formulario = EscalaProbabilidadForm()
	listado = Escalaprobabilidad.objects.all()
	if request.POST:
		try:

			campos = Escalaprobabilidad()
			campos.escala = None if(request.POST.get('escala'))=="" else request.POST.get('escala')
			campos.desde=request.POST.get('desde')
			campos.hasta=request.POST.get('hasta')
			campos.clasificacion=request.POST.get('clasificacion')
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
				
	return render(request,'escala_probabilidad_ingreso.html', ctx)

@login_required
def escala_probabilidad_editar(request, id):
	ctx = {}
	instancia = Escalaprobabilidad.objects.get(pk=id)
	formularios = EscalaProbabilidadForm(instance= instancia)

	if request.POST:
		print 'Paso por aqui'
		try:
			campos = Escalaprobabilidad.objects.get(pk=id)
			campos.escala = None if(request.POST.get('escala'))=='' else request.POST.get('escala')
			campos.desde=request.POST.get('desde')
			campos.hasta=request.POST.get('hasta')
			campos.clasificacion=request.POST.get('clasificacion')
			campos.save()
			

			formularios = EscalaProbabilidadForm(instance=campos)
			mensaje = 'exito'
		except Exception as e:
			raise
			mensaje = e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
		return HttpResponseRedirect(reverse('escala_probabilidad'))

	else:
		#formularios.fields['descarea'] = forms.ModelChoiceField(queryset=Areas.objects.all(), label="Area")
		ctx = {
				'formulario': formularios,
		}	
		return render(request,'escala_probabilidad_editar.html', ctx)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
import json
def ajax(request):
	if request.is_ajax():
		codtipoarea = request.GET['codtipoarea']
	data = list(Tipoareas.objects.values('CodArea', 'DescArea').filter(CodTipoArea=CodTipoArea))
	return HttpResponse(json.dumps(data), content_type='application/json')