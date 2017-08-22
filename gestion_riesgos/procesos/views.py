from django.shortcuts import render
# -*- coding: utf-8 -*-
# Create your views here.
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
from administracion.models import *
from procesos.models import *
from procesos.forms import *

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText 
import datetime,time

@login_required
def procesos(request):
	formulario = ProcesosForm()
	TipoProceso = TipoProcesoEditarForm()
	Puesto = PuestosEditarForm()
	estado = EstadosForm()
	listado = Procesos.objects.all()
	ctx = {}

	if request.POST:
		try:
			now = datetime.datetime.now()
			campos = Procesos()
			campos.codtipoproceso = None if request.POST.get('codtipoproceso') == '' else Tipoproceso.objects.get(pk=request.POST.get('codtipoproceso'))
			campos.nombre_proceso = request.POST.get('nombre_proceso')
			campos.descripcion = request.POST.get('descripcion')
			campos.idduenoproceso = None if request.POST.get('idduenoproceso') == '' else Puestos.objects.get(pk=request.POST.get('idduenoproceso'))
			campos.estado = Estados.objects.get(pk=1) 
			campos.fecha_implementacion = now.strftime("%Y-%m-%d %H:%M:%S") #request.POST.get('fecha_implementacion1')
			# try:
   #  				campos.logo = request.FILES['logo']
  	# 		except Exception as e:
   #   				pass
   			print now.strftime("%Y-%m-%d %H:%M:%S")
			campos.save()

			mensaje = 'exito'

		except Exception as e:
			raise
			# mensaje = e
		ctx = {
				'formulario': formulario,
				'mensaje': mensaje,
				'estado': estado,
				'listado': listado,
		}
	else:
		ctx = {
				'formulario': formulario,
				'estado': estado,
				'listado': listado,
				
		}
	return render(request, 'procesos_listado.html',ctx)

@login_required
def procesos_editar(request, id):
	ctx = {}
	instancia = Procesos.objects.get(pk= id)
	formulario = ProcesosForm(instance= instancia)

	if request.POST:
		try:
			campos = Procesos.objects.get(pk= id)
			campos.codtipoproceso = None if request.POST.get('codtipoproceso') == '' else Tipoproceso.objects.get(pk=request.POST.get('codtipoproceso'))
			campos.nombre_proceso = request.POST.get('nombre_proceso')
			campos.descripcion = request.POST.get('descripcion')
			campos.idduenoproceso = None if request.POST.get('idduenoproceso') == '' else Puestos.objects.get(pk=request.POST.get('idduenoproceso'))
			campos.estado = Estados.objects.get(pk=1) 
			campos.save()

			formulario = Procesos(instance= campos)

			mensaje= 'exito'
		except Exception as e:
			raise e
			mensaje= e
		ctx = {
				'formulario': formularios,
				'mensaje': mensaje,
		}
	else:
			ctx = {
				'formulario': formularios,
			}
			return render(request,'Procesos_editar.html', ctx)

# @login_required
# def procesos_listado(request):
# 	ctx = {}
# 	listado = Procesos.objects.all()

# 	ctx = {
# 			'listado': listado
# 	}
# 	return render (request, 'procesos_listado.html', ctx)


@login_required
def subprocesos(request, id):
	ctx = {}

	#instancias
	try:
		instancia = Subprocesos.objects.filter(codproceso = id)
		
	except Subprocesos.DoesNotExist: 
		instancia = None
	instanciap = Procesos.objects.get(codproceso= id)


	#Formularios
	formulario = SubprocesosForm()	
	formularioProceso = ProcesosForm(instance= instanciap)
	formularioActividad = ActividadesForm()
	formularioEscenario = SubprocesosXEscenariosForm()
	formularioraci = RACIForm()
	tipoactividad = TipoActividadEditarForm()
	escenario = EscenarioriesgosEditarForm()
	procesos = ProcesosEditarForm()
	Puesto = PuestosEditarForm()
	actividadesedit = ActividadesEditarForm()
	tipocontrol = TipoControlEditarForm()
	naturaleza = NaturalezacontrolEditarForm()
	racie = TipoRaciEditarForm()
	# actividadesedit.fields["descripcionactividad"] = forms.ModelChoiceField(queryset=Actividades.objects.filter(codsubproceso=request.POST.get('subproc3')), label = 'Actividad')
	#Listados
	listado = Subprocesos.objects.filter(codproceso = id)
	actividades = Actividades.objects.filter(codsubproceso__isnull= False)
	escenarios = Subprocesosxescenarios.objects.filter(codsubproceso__isnull=False)
	matrizraci = Raci.objects.filter(codactividad__isnull=False)
	matrizcontrol = Controles.objects.filter(codactividad__isnull=False)
	
	

	subproceso = []

	#Subprocesos
	for sub in listado:
		array = {}
		array['pk'] = sub.pk
		array['codproceso'] = sub.codproceso
		array['descsubproceso'] = sub.descsubproceso
		array['due_osubproceso'] = sub.due_osubproceso
		array['orden_subproceso'] = sub.orden_subproceso
		array['observaciones'] = sub.observaciones
		array['anexo'] = sub.anexo
		array['observaciones'] = sub.observaciones
		array['codestado'] = sub.codestado
		array['fecha_implementacion'] = sub.fecha_implementacion
		
		#Actividades
		dic=[]
		for act in actividades:
			if act.codsubproceso.pk == sub.pk:
				
				lista = {}
				lista['codactividad'] = act.codactividad
				lista['ordenactividad'] = act.ordenactividad
				lista['codtipoactividad'] = act.codtipoactividad
				lista['descripcionactividad'] = act.descripcionactividad

				#RACI
				dic3=[]
				for raci in matrizraci:
					if raci.codactividad.pk == act.pk and raci.codactividad.codsubproceso.pk == sub.pk:

						matriz = {}
						matriz['idraci'] = raci.idraci
						matriz['codraci'] = raci.codraci
						matriz['codpuesto'] = raci.codpuesto
						matriz['observaciones'] = raci.observaciones
						matriz['codactividad'] = raci.codactividad
						dic3.append(matriz)

				lista['raci'] = dic3
				dic.append(lista)

			# #Controles
			# dic4 = []
			# for ctrl in matrizcontrol:
			# 	if ctrl.codactividad.pk == act.pk:
			# 		mcontrol = {}
			# 		mcontrol['codcontrol'] = ctrl.codcontrol
			# 		mcontrol['codtipocontrol'] = ctrl.codtipocontrol
			# 		mcontrol['efectividad'] = ctrl.efectividad
			# 		mcontrol['nivel_riesgo'] = ctrl.nivel_riesgo
			# 		mcontrol['riesgo_residual'] = ctrl.riesgo_residual
			# 		mcontrol['codnaturaleza'] = ctrl.codnaturaleza
			# 		mcontrol['realiza'] = ctrl.realiza
			# 		mcontrol['ejecuta'] = ctrl.ejecuta
			# 		mcontrol['revisa'] = ctrl.revisa
			# 		mcontrol['fecha_implementacion'] = ctrl.fecha_implementacion
			# 		mcontrol['descripcion'] = ctrl.descripcion

			# 		dic4.append(mcontrol)

			# lista['controles'] = dic4

			  

		array['actividades'] = dic
		# subproceso.append(array)

		#Escenarios
		dic2=[]
		for esc in escenarios:
			if esc.codsubproceso.pk == sub.pk:

				listescenario = {}
				listescenario['codsubprocesosxescenarios'] = esc.codsubprocesosxescenarios
				listescenario['codescenarioriesgo'] = esc.codescenarioriesgo
				listescenario['codsubproceso'] = esc.codsubproceso
				listescenario['probabilidad'] = esc.probabilidad
				listescenario['impacto'] = esc.impacto
				listescenario['nivel_riesgo_inherente'] = esc.nivel_riesgo_inherente
				listescenario['observaciones'] = esc.observaciones

				dic2.append(listescenario)
		array['escenarios'] = dic2


		subproceso.append(array)	
	
	#print  subproceso
	if request.is_ajax():
		request.session['valor'] = request.GET['valors']
		request.session['metodo'] = request.GET['metodo']
		return HttpResponse(True) 
	# procesos.fields['nombre_proceso'] = forms.ModelChoiceField(queryset = Procesos.objects.get(codproceso= id))
	if request.POST:
		if request.POST['metodo'] == 'subproceso':
			print 'subproceso'
			try:
				print 'diruriru'
				campos = Subprocesos()#.objects.filter(codproceso = id)#Subprocesos.objects.filter(codproceso = id)
				campos.codproceso = Procesos.objects.get(pk= id)#None if (request.POST.get('id'))=='' else Procesos.objects.get(codproceso = request.POST.get('id'))
				campos.descsubproceso = request.POST.get('descsubproceso')
				campos.codestado = Estados.objects.get(pk=1)#None if (request.POST.get('codestado'))=='' else Estados.objects.get(codestado = request.POST.get('codestado'))
				campos.due_osubproceso = None if (request.POST.get('descpuesto'))=='' else Puestos.objects.get(pk=request.POST.get('descpuesto'))#request.POST.get('descpuesto')
				campos.orden_subproceso = request.POST.get('orden_subproceso')
				campos.observaciones = request.POST.get('observaciones')
				campos.anexo = request.POST.get('anexo')
				#campos.fecha_implementacion = request.POST.get('fecha_implementacion')
				campos.save()
				#formulario = SubprocesosForm(instance = campos)
				mensaje = 'exito'
			except Exception as e:
				mensaje = e
			ctx = {
					'formulario': formulario,
					'formulariop': formularioProceso,
					'formularioa': formularioActividad,
					'formularioe': formularioEscenario,
					'formularior': formularioraci,
					'listado': listado,
					'tipoactividad': tipoactividad,
					'escenario': escenario,
					'subproceso': subproceso,
					'procesos': procesos,
					'mensaje': mensaje,
					'puesto':Puesto,
					'actividades_editar': actividadesedit,
					'tipocontrol': tipocontrol,
					'naturaleza': naturaleza,
					'racie': racie,

			}
			return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')
		if request.POST['metodo'] == 'editar_proceso':
			try:
				print 'Diru'
				campos = Procesos.objects.get(pk=id)
				campos.codtipoproceso = None if request.POST.get('codtipoproceso') == '' else Tipoproceso.objects.get(pk=request.POST.get('codtipoproceso'))
				campos.nombre_proceso = request.POST.get('nombre_proceso')
				campos.descripcion = request.POST.get('descripcion')
				campos.idduenoproceso = None if request.POST.get('idduenoproceso') == '' else Puestos.objects.get(pk=request.POST.get('idduenoproceso'))
				campos.estado = Estados.objects.get(pk=1)

				campos.save() 
				formularioProceso = ProcesosForm(instance= campos)

				
			except Exception as e:
				raise e
			return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')

		if request.POST['metodo'] == 'Inserta_actividad':
			try:
				
				campos = Actividades()
				campos.codtipoactividad = None if request.POST.get('desctipoactividad') == '' else Tipoactividad.objects.get(pk=request.POST.get('desctipoactividad'))
				campos.ordenactividad = request.POST.get('ordenactividad')
				campos.descripcionactividad = request.POST.get('descripcionactividad')
				campos.codsubproceso = None if request.POST.get('subproceso_id') == '' else Subprocesos.objects.get(pk=request.POST.get('subproceso_id'))
				
				campos.save() 
				

				
			except Exception as e:
				raise e
			return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')

		if request.POST['metodo'] == 'Inserta_escenario':
			try:
				
				campos = Subprocesosxescenarios()
				campos.codescenarioriesgo = None if request.POST.get('descescenario') == '' else Escnariosriesgos.objects.get(pk=request.POST.get('descescenario'))
				campos.probabilidad = request.POST.get('probabilidad')
				campos.impacto = request.POST.get('impacto')
				campos.nivel_riesgo_inherente = request.POST.get('nivel_riesgo_inherente')
				campos.observaciones = request.POST.get('observaciones')
				campos.codsubproceso = None if request.POST.get('subproceso_ide') == '' else Subprocesos.objects.get(pk=request.POST.get('subproceso_ide'))
				
				campos.save() 
				

				
			except Exception as e:
				raise e
			return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')

		if request.POST['metodo'] == 'Inserta_raci':
			try:
				
				campos = Raci()
				campos.codactividad = None if request.POST.get('actividad') == '' else Actividades.objects.get(pk=request.POST.get('actividad'))
				campos.codraci = None if request.POST.get('letra') == '' else Tiporaci.objects.get(pk=request.POST.get('letra'))
				campos.codpuesto = None if request.POST.get('descpuesto') == '' else Puestos.objects.get(pk=request.POST.get('descpuesto'))
				campos.observaciones = request.POST.get('observaciones')
				# campos.codsubproceso = None if request.POST.get('subproceso_ide') == '' else Subprocesos.objects.get(pk=request.POST.get('subproceso_ide'))
				
				campos.save() 
				

				
			except Exception as e:
				raise e
			return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')

	else:
		print 'sopitaaa'
		ctx = {
			'formulario': formulario,
			'formulariop': formularioProceso,
			'formularioa': formularioActividad,
		 	'formularioe': formularioEscenario,
		 	'formularior': formularioraci,
			'listado': listado,
			'tipoactividad': tipoactividad,
			'escenario': escenario,
			'subproceso': subproceso,
			'procesos': procesos,
			'instanciap': instanciap,
			'puesto':Puesto,
			'actividades_editar': actividadesedit,
			'tipocontrol': tipocontrol,
			'naturaleza': naturaleza,
			'racie': racie,
			
		}
			#return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id + '/' )
	#return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')
		return render(request, 'subprocesos_listado.html', ctx)


@login_required
def subprocesosescenarios(request, id):
	try:
		instancia = Subprocesosxescenarios.objects.filter(codsubproceso = id)
	except Subprocesosxescenarios.DoesNotExist: 
		instancia = None
	
	formulario = SubprocesosXEscenariosForm()
	listado = Subprocesosxescenarios.objects.filter(codsubproceso = id)
	ctx = {}
	instanciap = Subprocesos.objects.get(codsubproceso= id)
	formulariosubproceso = SubprocesosForm(instance= instanciap)
	subprocesos = SubprocesosEditarForm()
	Puesto = PuestosEditarForm()
	escenario = EscenarioriesgosEditarForm()

	if request.POST:
		if request.POST['metodo'] == 'subproceso':
			print 'subproceso'
			try:
				print 'diruriru'
				campos = Subprocesos.objects.get(pk= id)#.objects.filter(codproceso = id)#Subprocesos.objects.filter(codproceso = id)
				campos.codproceso = Procesos.objects.get(pk= id)#None if (request.POST.get('id'))=='' else Procesos.objects.get(codproceso = request.POST.get('id'))
				campos.descsubproceso = request.POST.get('descsubproceso')
				campos.codestado = Estados.objects.get(pk=1)#None if (request.POST.get('codestado'))=='' else Estados.objects.get(codestado = request.POST.get('codestado'))
				campos.due_osubproceso = None if (request.POST.get('descpuesto'))=='' else Puestos.objects.get(pk=request.POST.get('descpuesto'))#request.POST.get('descpuesto')
				campos.orden_subproceso = request.POST.get('orden_subproceso')
				campos.observaciones = request.POST.get('observaciones')
				campos.anexo = request.POST.get('anexo')
				#campos.fecha_implementacion = request.POST.get('fecha_implementacion')
				campos.save()
				formulariosubproceso = SubprocesosForm(instance= campos)
				#formulario = SubprocesosForm(instance = campos)
				mensaje = 'exito'
			except Exception as e:
				raise
				mensaje = e
			

		if request.POST['metodo'] == 'subprocesosxescenarios':
			try:
				campos = Subprocesosxescenarios()
				campos.codescenarioriesgo = None if (request.POST.get('codescenarioriesgo'))=='' else Escnariosriesgos.objects.get(pk=request.POST.get('codescenarioriesgo'))
				campos.codsubproceso = None if (request.POST.get('codsubproceso'))=='' else Subprocessos.objects.get(pk=request.POST.get('codsubproceso'))
				campos.probabilidad = request.POST.get('probabilidad')
				campos.impacto = request.POST.get('impacto')

			except Exception as e:
				raise e
			ctx = {
					'formulario': formulario,
					'formulariop': formulariosubproceso,
					'listado': listado,
					'subprocesos': subprocesos,
					'mensaje': mensaje,
					'puesto': Puesto,
					'escenario': escenario,

			}
			return HttpResponseRedirect('/procesos/subprocesosxescenarios/ingreso/'+ id +'/')
			
			
	else:
		print 'sopitaaa'
		ctx = {
			'formulario': formulario,
			'formulariop': formulariosubproceso,
			'listado': listado,
			'subprocesos': subprocesos,
			'instanciap': instanciap,
			'puesto': Puesto,
			'escenario': escenario,
		}
			
		return render(request, 'subprocesos_escenarios_ingreso.html', ctx)




@login_required
def actividades(request):
	formulario = ActividadesForm()
	listado = Actividades.objects.all()
	ctx = {}
	tipoactividad = TipoActividadEditarForm()
	subprocesos = SubprocesosEditarForm()

	if request.POST:
		try:
			campos = Actividades()
			campos.codsubproceso = None if (request.POST.get('codsubproceso'))=='' else Subprocesos.objects.get(codsubproceso = request.POST.get('codsubproceso'))
			campos.ordenactividad = request.POST.get('ordenactividad')
			campos.codtipoactividad = None if (request.POST.get('codtipoactividad'))=='' else Tipoactividad.objects.get(codtipoactividad = request.POST.get('codtipoactividad'))
			campos.descripcionactividad = request.POST.get('descripcionactividad')
			campos.save()

			mensaje = 'exito'
		except Exception as e:
			mensaje = e
		ctx = {
				'formulario': formulario,
				'listado': listado,
				'tipoactividad': tipoactividad,
				'subprocesos': subprocesos,
		}
	else:
			ctx = {
				'formulario': formulario,
				'listado': listado,
				'tipoactividad': tipoactividad,
				'subprocesos': subprocesos,
		}
	return render(request, 'actividades_ingreso.html', ctx)


import json
def ajax(request):
	if request.is_ajax():
		desctipoactividad = request.GET['desctipoactividad']
	#data = list(Tipoactividad.objects.values('CodTipoActividad', 'DescTipoActividad').filter(CodTipoActividad=desctipoactividad))
	data = Tipoactividad.objects.values('CodTipoActividad').filter(DescTipoActividad=desctipoactividad)
	return HttpResponse(json.dumps(data), content_type='application/json')

def ajaxproceso(request):
	if request.is_ajax():
		codproceso = request.GET['codproceso']
	data = dict(Procesos.objects.values('pk').get(pk=codproceso))
	return HttpResponse(json.dumps(data), content_type='application/json')

def ajaxactividad(request):
	if request.is_ajax():
		codsubproceso = request.GET['valor']
	data = list(Actividades.objects.values('pk','descripcionactividad').filter(codsubproceso=codsubproceso))
	return HttpResponse(json.dumps(data), content_type='application/json')



