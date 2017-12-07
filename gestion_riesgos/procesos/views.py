
# -*- coding: utf-8 -*-
# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import *
from django.template import RequestContext
from django.urls import reverse
from django.template import Context
from django.contrib.auth import authenticate, login as auth_login, logout
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.contrib.auth.hashers  import make_password
from django.contrib.auth.models import *
from .models import *
from django.db.models import Q, F
from django.db.models import Avg, Max, Min, Count


#from general.models import *
from administracion.forms import *
from administracion.models import *
from procesos.models import *
from procesos.forms import *

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from datetime import datetime, date,time, timedelta 
import datetime,time
import math

import json
import decimal

def date_handler(obj):
	if hasattr(obj, 'isoformat'):
		return obj.isoformat()
	else:
		raise TypeError

def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)

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
			try:
    				campos.logoimagen = request.FILES['logoimagen']
  			except Exception as e:
     				pass
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

@login_required
def subprocesos(request, id):
	ctx = {}

	try:
		del request.session['proceso']
		
	except Exception as e:
		pass

	#instancias
	try:
		instancia = Subprocesos.objects.filter(codproceso = id)
				
	except Subprocesos.DoesNotExist: 
		instancia = None
		instanciaig= None
		
	instanciap = Procesos.objects.get(codproceso= id)

	# instanciaig= InformacionGeneral.objects.filter(subproceso__codproceso=id)
		

	#Formularios

	formulario = SubprocesosForm()	
	formularioProceso = ProcesosForm(instance= instanciap)
	formularioActividad = ActividadesForm()
	#formularioEscenario = SubprocesosXEscenariosForm()
	formularioraci = RACIForm()
	formularioControl = ControlesForm()
	formularioinfogeneral = InformacionForm()
	tipoactividad = TipoActividadEditarForm()
	escenario = EscenarioriesgosEditarForm()
	procesos = ProcesosEditarForm()
	Puesto = PuestosEditarForm()
	actividadesedit = ActividadesEditarForm()
	tipocontrol = TipoControlEditarForm()
	naturaleza = NaturalezacontrolEditarForm()
	#racie = TipoRaciEditarForm()
	unidad = UnidadesMedidaForm()
	
	#Listados
	listado = Subprocesos.objects.filter(codproceso = id).annotate(numact=Count('actividad_sub')).annotate(numriesg=Count('riesgo_sub'))
	actividades = Actividades.objects.filter(codsubproceso__codproceso=id)#.order_by('ordenactividad')#(codsubproceso__isnull= False)
	escenarios = Subprocesosxescenarios.objects.filter(codsubproceso__codproceso=id)
	matrizraci = Raci.objects.filter(codactividad__codsubproceso__codproceso=id)#(codactividad__codsubproceso__isnull=False)
	matrizcontrol = Controles.objects.filter(escenario__codsubproceso__codproceso=id)
	controles= Controles.objects.filter(Q(codactividad__codsubproceso__codproceso=id) | Q(escenario__codsubproceso__codproceso=id))
	informaciongeneral = InformacionGeneral.objects.filter(proceso = id)
	duenosubproceso = DuenosSubproceso.objects.filter(subproceso__codproceso=id)
	tiporiesgosubproceso = TipoRiesgoSubprocesosEscenarios.objects.filter(codsubprocesosxescenarios__codsubproceso__codproceso=id)
	controlespendientes=Controles.objects.filter(escenario__isnull=True,codactividad__codsubproceso__codproceso=id)#.annotate(tot=Count('codcontrol'))
	cedulanormativa= CedulaNormativa.objects.filter(codproceso=id)
	indicadoresdesempenio = IndicadoresDesempenio.objects.filter(codproceso=id)
	diagramassubprocesos = ImagenesSubprocesos.objects.filter(subproceso__codproceso=id)
	conteo = controlespendientes.count()
	conteoriesgos=escenarios.count()


	
	request.session['proceso'] = id

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
		array['diagrama'] = sub.diagrama
		array['numact'] = sub.numact
		# array['numriesg'] = sub.numriesg

		#Diagramas
		dicdiag=[]
		for diag in diagramassubprocesos:
			if diag.subproceso.pk == sub.pk:
				arraydiag = {}
				arraydiag['id'] = diag.pk
				arraydiag['subproceso'] = diag.subproceso
				arraydiag['codsubproceso'] = diag.subproceso.pk
				arraydiag['diagrama'] = diag.diagrama
				dicdiag.append(arraydiag)
		array['diagramas'] = dicdiag

		#Duenios de Subproceso
		dicdue=[]
		for due in duenosubproceso:
			if due.subproceso.pk == sub.pk:
				arraydue = {}
				arraydue['subproceso'] = due.subproceso
				arraydue['puesto'] = due.puesto.descpuesto
				dicdue.append(arraydue)
		array['duenios'] = dicdue
		
		#Actividades
		dic=[]
		for act in actividades:
			if act.codsubproceso.pk == sub.pk:
				
				lista = {}
				lista['codactividad'] = act.codactividad
				lista['codsubproceso'] = act.codsubproceso
				lista['ordenactividad'] = act.ordenactividad
				lista['codtipoactividad'] = act.codtipoactividad
				lista['descripcionactividad'] = act.descripcionactividad
				lista['nombreactividad'] = act.nombreactividad
				lista['tiempo'] = act.tiempo
				lista['unidadmedida'] = act.unidadmedida

				#Puestos RACI
				dicr=[]
				for r in matrizraci:
					if r.codactividad.pk == act.pk:
						if r.codraci.letra == 'R':
							racir={}
							racir['idraci'] = r.idraci
							racir['codactividad'] = r.codactividad.nombreactividad
							racir['codraci'] = r.codraci.letra
							racir['codpuesto'] = r.codpuesto.descpuesto
							dicr.append(racir)
				lista['racir'] = dicr

				dica=[]
				for r2 in matrizraci:
					if r2.codactividad.pk == act.pk:
						if r2.codraci.letra == "A":
							racia={}
							racia['idraci'] = r2.idraci
							racia['codactividad'] = r2.codactividad.nombreactividad
							racia['codraci'] = r2.codraci.letra
							racia['codpuesto'] = r2.codpuesto.descpuesto
							dica.append(racia)
				lista['racia'] = dica

				dicc=[]
				for r3 in matrizraci:
					if r3.codactividad.pk == act.pk:
						if r3.codraci.letra == "C":
							racic={}
							racic['idraci'] = r3.idraci
							racic['codactividad'] = r3.codactividad.nombreactividad
							racic['codraci'] = r3.codraci.letra
							racic['codpuesto'] = r3.codpuesto.descpuesto
							dicc.append(racic)
				lista['racic'] = dicc


				dici=[]
				for r4 in matrizraci:
					if r4.codactividad.pk == act.pk:
						if r4.codraci.letra == "I":
							racii={}
							racii['idraci'] = r4.idraci
							racii['codactividad'] = r4.codactividad.nombreactividad
							racii['codraci'] = r4.codraci.letra
							racii['codpuesto'] = r4.codpuesto.descpuesto
							dici.append(racii)
				lista['racii'] = dici

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
			  

		array['actividades'] = dic
		# subproceso.append(array)

		#Escenarios
		dic2=[]
		for esc in escenarios:
			if esc.codsubproceso.pk == sub.pk:

				listescenario = {}
				listescenario['codsubprocesosxescenarios'] = esc.codsubprocesosxescenarios
				listescenario['descsubproceso'] = esc.codsubproceso.descsubproceso		
				listescenario['escenario'] = esc.escenario #
				listescenario['codsubproceso'] = esc.codsubproceso
				listescenario['probabilidad'] = esc.probabilidad
				listescenario['impacto'] = esc.impacto
				listescenario['nivel_riesgo_inherente'] = esc.nivel_riesgo_inherente
				listescenario['observaciones'] = esc.observaciones
				listescenario['linea_negocio_nivel1'] = esc.linea_negocio_nivel1
				listescenario['linea_negocio_nivel2'] = esc.linea_negocio_nivel2
				listescenario['categoria_riesgo'] = '0' if esc.categoria_riesgo is None else esc.categoria_riesgo.codcategoria
				listescenario['riesgos'] = esc.categoria_riesgo if esc.categoria_riesgo is not None else 0
				listescenario['zonariesgo'] = esc.zonariesgo.clasificacion if esc.zonariesgo is not None else 'No Asignado'
				listescenario['zonariesgoid'] = esc.zonariesgo.pk if esc.zonariesgo is not None else 0				
				

				#Tipo de Riesgo por Escenario
				dictiporiesgo=[]	
				for tiporiesgo in tiporiesgosubproceso:
						if tiporiesgo.codsubprocesosxescenarios.codsubproceso.pk == sub.pk:
								tipriesgo={}
								tipriesgo['codtiporiesgo'] = tiporiesgo.codtiporiesgo
								tipriesgo['desctiporiesgo'] = tiporiesgo.codtiporiesgo.desctiporiesgo
								tipriesgo['codsubprocesosxescenarios'] = tiporiesgo.codsubprocesosxescenarios
								tipriesgo['codsubproceso'] = tiporiesgo.codsubprocesosxescenarios.codsubproceso.pk
								dictiporiesgo.append(tipriesgo)
				listescenario['tiporiesgosubproceso'] = dictiporiesgo	
				

				#Controles
				dic4 = []
				for ctrl in matrizcontrol:
				 	 if ctrl.escenario.pk == esc.pk:
						mcontrol = {}
						mcontrol['codcontrol'] = ctrl.codcontrol
						mcontrol['codactividad'] = ctrl.codactividad.nombreactividad if ctrl.codactividad else "No Asignada" 
						mcontrol['subproceso'] = ctrl.escenario.codsubproceso.descsubproceso if ctrl.escenario else "No Asignado"
						mcontrol['codsubproceso'] = ctrl.escenario.codsubproceso.pk if ctrl.escenario else "No Asignado"
						mcontrol['escenario'] = ctrl.escenario.escenario if ctrl.escenario else "No Asignado"
						mcontrol['escenario_efectividad'] = ctrl.escenario.efectividad if ctrl.escenario else "No Asignado"  
						mcontrol['codtipocontrol'] = ctrl.codtipocontrol.desctipocontrol if ctrl.codtipocontrol else "No Asignado"
						mcontrol['efectividad'] = ctrl.efectividad
						mcontrol['nivel_riesgo_residual'] = ctrl.nivel_riesgo_residual
						mcontrol['codnaturaleza'] = ctrl.codnaturaleza.descnaturaleza if ctrl.codnaturaleza else "No Asignado"
						mcontrol['fecha_implementacion'] = ctrl.fecha_implementacion
						mcontrol['descripcion'] = ctrl.descripcion
						mcontrol['frecuencia'] = ctrl.frecuencia
						mcontrol['observaciones_auditoria'] = ctrl.observaciones_auditoria
						mcontrol['zona_riesgo'] = ctrl.zona_riesgo.clasificacion if ctrl.zona_riesgo else 'No Asignado'
						mcontrol['zona_riesgoid'] = ctrl.zona_riesgo.pk if ctrl.zona_riesgo else 0
						mcontrol['valoracion_control'] = ctrl.valoracion_control

						dic4.append(mcontrol)

				listescenario['controles'] = dic4



				dic2.append(listescenario)



		array['escenarios'] = dic2

		#Informacion General
		dicig=[]
		for info in informaciongeneral:
			if info.proceso.pk == sub.codproceso.pk:

				listinfogeneral = {}
				listinfogeneral['proceso'] = info.proceso
				listinfogeneral['introduccion'] = info.introduccion
				listinfogeneral['objetivos'] = info.objetivos
				listinfogeneral['alcance'] = info.alcance
				listinfogeneral['responsabilidad'] = info.responsabilidad
				listinfogeneral['revision'] = info.revision
				listinfogeneral['cumplimiento'] = info.cumplimiento
				listinfogeneral['excepciones'] = info.excepciones

				dicig.append(listinfogeneral)
		array['informaciongeneral'] = dicig

		
		subproceso.append(array)

	controls=[]
	for ctrl in controles:
		# if ctrl.codactividad.codsubproceso.codproceso.pk == sub.codproceso.pk or ctrl.escenario.codsubproceso.codproceso.pk=sub.codproceso.pk:
			mcontrol = {}
			mcontrol['codcontrol'] = ctrl.codcontrol
			mcontrol['codactividad'] = ctrl.codactividad.nombreactividad if ctrl.codactividad else "No Asignada" 
			mcontrol['subproceso'] = ctrl.escenario.codsubproceso.descsubproceso if ctrl.escenario else "No Asignado"
			mcontrol['codsubproceso'] = ctrl.escenario.codsubproceso.pk if ctrl.escenario else "No Asignado"
			mcontrol['escenario'] = ctrl.escenario.escenario if ctrl.escenario else "No Asignado" 
			mcontrol['codtipocontrol'] = ctrl.codtipocontrol.desctipocontrol if ctrl.codtipocontrol else "No Asignado"
			mcontrol['efectividad'] = ctrl.efectividad
			mcontrol['nivel_riesgo_residual'] = ctrl.nivel_riesgo_residual
			mcontrol['codnaturaleza'] = ctrl.codnaturaleza.descnaturaleza if ctrl.codnaturaleza else "No Asignado"
			mcontrol['fecha_implementacion'] = ctrl.fecha_implementacion
			mcontrol['descripcion'] = ctrl.descripcion
			mcontrol['frecuencia'] = ctrl.frecuencia
			mcontrol['observaciones_auditoria'] = ctrl.observaciones_auditoria
			mcontrol['zona_riesgo'] = ctrl.zona_riesgo
			mcontrol['valoracion_control'] = ctrl.valoracion_control

			controls.append(mcontrol)



	
	#print  subproceso
	# if request.is_ajax():
	# 	request.session['valor'] = request.GET['valors']
	# 	request.session['metodo'] = request.GET['metodo']
	# 	return HttpResponse(True) 
	# procesos.fields['nombre_proceso'] = forms.ModelChoiceField(queryset = Procesos.objects.get(codproceso= id))
	if request.POST:
		if request.POST['metodo'] == 'subproceso':
			# print 'subproceso'
			try:
				print 'diruriru3'
				campos = Subprocesos()#.objects.filter(codproceso = id)#Subprocesos.objects.filter(codproceso = id)
				campos.codproceso = Procesos.objects.get(pk= id)#None if (request.POST.get('id'))=='' else Procesos.objects.get(codproceso = request.POST.get('id'))
				campos.descsubproceso = request.POST.get('descsubproceso')
				campos.codestado = Estados.objects.get(pk=1)#None if (request.POST.get('codestado'))=='' else Estados.objects.get(codestado = request.POST.get('codestado'))
				campos.due_osubproceso = None if (request.POST.get('descpuesto'))=='' else Puestos.objects.get(pk=request.POST.get('descpuesto'))#request.POST.get('descpuesto')
				campos.orden_subproceso = request.POST.get('orden_subproceso')
				campos.observaciones = request.POST.get('observaciones')
				campos.anexo = request.POST.get('anexo')
				campos.fecha_implementacion = datetime.datetime.now() #request.POST.get('fecha_implementacion')
				
				#Guardado de imagen en la Base de Datos
				# try:
    # 					campos.diagrama = request.FILES['diagrama']
    # 		# 			campos.save()
    # 		# 			# Guardar Imagen en la base de Datos
				# 		# from django.db import connection
				# 		# 	with connection.cursor() as cursor:
				# 		# 	try:
				# 		# 		llave=campos.pk	
				# 		# 		query="exec [dbo].[spGuargarImagen] %s,%s"%('Subprocesos',llave)
				# 		# 		cursor.execute(query)
				# 		# 		cursor.close()
				# 		# 	except Exception as e:
				# 		# 		print e
  		# 		except Exception as e:
    #  					pass
				campos.save()

				

				#-------Actualizar Orden------------------------------
				from django.db import connection
				with connection.cursor() as cursor:
					try:
						query="exec [dbo].[ActualizaOrden] %s,%s"%('Subprocesos',id)
						cursor.execute(query)
					except Exception as e:
						raise e
				mensaje = 'exito'
			except Exception as e:
					print e
			ctx = {
					'formulario': formulario,
					'formulariop': formularioProceso,
					'formularioa': formularioActividad,
					#'formularioe': formularioEscenario,
					'formularior': formularioraci,
					'formularioc': formularioControl,
					'formularioig':formularioinfogeneral,
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
					#'racie': racie,
					'infogeneral': informaciongeneral,
					'unidad': unidad,
					'controlespendientes': controlespendientes,
					'control': controls,
					'cedulanormativa':cedulanormativa,
					'indicadoresdesempenio':indicadoresdesempenio,
					'conteo':conteo,
					'conteoriesgos':conteoriesgos,

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
				try:
					campos.diagrama = request.FILES['logoimagen']
					campos.save()
					#Restaurar
					## Guardar Imagen en la base de Datos
					# from django.db import connection
					# with connection.cursor() as cursor:
					# 	try:
					# 		llave=campos.pk	
					# 		query="exec [dbo].[spGuargarImagen] %s,%s"%('Procesos',llave)
					# 		cursor.execute(query)
					# 		cursor.close()
					# 	except Exception as e:
					# 		print e
  				except Exception as e:
     						print e
     						campos.save()
		          
				
				
				formularioProceso = ProcesosForm(instance= campos)

				
			except Exception as e:
					raise e
			return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')

		if request.POST['metodo'] == 'Inserta_actividad':
			try:
				print 'Holaaaaa'
				# print request.POST.get('desctipoactividad')
				campos = Actividades()
				campos.codtipoactividad = None if request.POST.get('desctipoactividad') == '' else Tipoactividad.objects.get(pk=request.POST.get('desctipoactividad'))
				campos.ordenactividad = request.POST.get('ordenactividad')
				campos.descripcionactividad = request.POST.get('descripcionactividad')
				campos.nombreactividad = request.POST.get('nombreactividad')
				campos.descripcionactividad = request.POST.get('descripcionactividad')
				campos.codsubproceso = None if request.POST.get('codsubproceso') == '' else Subprocesos.objects.get(pk=request.POST.get('codsubproceso'))
				campos.tiempo = 0 if (request.POST.get('tiempo')) =='' else request.POST.get('tiempo')
				campos.unidadmedida= None if request.POST.get('descripcion') == '' else UnidadesMedida.objects.get(pk=request.POST.get('descripcion'))
				campos.fecha_control = datetime.datetime.now()
				campos.habilitado= "True" if (request.POST.get('habilitado'))=="on" else "False"
				try:
					campos.anexo = request.FILES['anexo']
					campos.save()
					#Restaurar
    				## Guardar Imagen en la base de Datos
					# from django.db import connection
					# with connection.cursor() as cursor:
					# 	try:
					# 		llave=campos.pk	
					# 		query="exec [dbo].[spGuargarImagen] %s,%s"%('Actividades',llave)
					# 		cursor.execute(query)
					# 		cursor.close()
					# 	except Exception as e:
					# 		print e
  				except Exception as e:
     					mensaje= e	
     					campos.save()
				

				

				#-------Control-----------------------------------------------

				if request.POST.get('desctipoactividad') == "1":
					print 'controool!!!!'
					print request.POST.get('desctipoactividad')
					campControl = Controles()
					campControl.codactividad= campos
					campControl.descripcion = request.POST.get('nombreactividad')
					# campControl.codtipocontrol= "No Asignado" #if request.POST.get('desctipoactividad') == '' else Tipoactividad.objects.get(pk=request.POST.get('desctipoactividad'))
					campControl.save()
					print "Exitosa actividad"
				#------- RACI-------------------------------------------------	
				R = request.POST.getlist('Responsable')

				for data in R:

					resp = Raci()
					resp.codactividad = campos
					resp.codraci = None if(request.POST.get('letraR'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraR'))
					resp.codpuesto = Puestos.objects.get(codpuesto=data)
					resp.save()


				A = request.POST.getlist('Acargo')	

				for dataa in A:

					ac = Raci()
					ac.codactividad = campos
					ac.codraci = None if(request.POST.get('letraA'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraA'))
					ac.codpuesto = Puestos.objects.get(codpuesto=dataa)
					ac.save()


				C = request.POST.getlist('Consultar')	
				for datac in C:

					con = Raci()
					con.codactividad = campos
					con.codraci = None if(request.POST.get('letraC'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraC'))
					con.codpuesto = Puestos.objects.get(codpuesto=datac)
					con.save()

				I = request.POST.getlist('Informar')	
				for datai in I:

					inf = Raci()
					inf.codactividad = campos
					inf.codraci = None if(request.POST.get('letraI'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraI'))
					inf.codpuesto = Puestos.objects.get(codpuesto=datai)
					inf.save()
					

				#-------Actualizar Orden------------------------------
				from django.db import connection
				with connection.cursor() as cursor:
					try:
						
						query="exec [dbo].[ActualizaOrden] %s,%s"%('Actividades',request.POST.get('codsubproceso'))
						cursor.execute(query)
					except Exception as e:
						raise e

								
			except Exception as e:
				raise e
			return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')

	

		if request.POST['metodo'] == 'Inserta_info':
			try:
				print 'patitoooo'
				campos = InformacionGeneral()
				campos.subproceso = None if request.POST.get('subproceso_idig') == '' else Subprocesos.objects.get(pk=request.POST.get('subproceso_idig'))
				campos.introduccion = request.POST.get('introduccion')
				campos.objetivos = request.POST.get('objetivos')
				campos.alcance = request.POST.get('alcance')
				campos.responsabilidad = request.POST.get('responsabilidad')
				campos.revision = request.POST.get('revision')
				campos.cumplimiento = request.POST.get('cumplimiento')
				campos.excepciones = request.POST.get('excepciones')
				campos.save()

			except Exception as e:
				raise e
			return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')

			# Restaurar *
		# if request.POST['metodo'] == 'guardar_diagrama':
		# 	try:
		# 		print 'boloban', sub
		# 		sub = request.POST['subproceso_iddg']
		# 		campos = Subprocesos.objects.get(pk=sub)
				
		# 		try:
		# 			campos.diagrama = request.FILES['diagrama']
		# 			campos.save()
  #   				# Guardar Imagen en la base de Datos
		# 			from django.db import connection
		# 			with connection.cursor() as cursor:
		# 				try:
		# 					llave=campos.pk	
		# 					query="exec [dbo].[spGuargarImagen] %s,%s"%('Subprocesos',llave)
		# 					cursor.execute(query)
		# 					cursor.close()
		# 				except Exception as e:
		# 					print e
		# 		except Exception as e:
		# 			raise e
		# 	except Exception as e:
		# 			raise e
			return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')
			
	else:
		print 'sopitaaa'
		ctx = {
			'formulario': formulario,
			'formulariop': formularioProceso,
			'formularioa': formularioActividad,
		 	#'formularioe': formularioEscenario,
		 	'formularior': formularioraci,
		 	'formularioc': formularioControl,
		 	'formularioig':formularioinfogeneral,
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
			# 'racie': racie,
			'infogeneral': informaciongeneral,
			'unidad': unidad,
			'controlespendientes': controlespendientes,
			'control': controls,
			'cedulanormativa':cedulanormativa,
			'indicadoresdesempenio':indicadoresdesempenio,
			'conteo':conteo,
			'conteoriesgos':conteoriesgos,
			
		}
			#return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id + '/' )
	#return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')
	return render(request, 'subprocesos_listado.html', ctx)

@login_required
def subprocesos_ingreso(request, id):
	ctx = {}

	try:
		del request.session['proceso']
		
	except Exception as e:
		pass

	#instancias
	try:
		instancia = Subprocesos.objects.filter(codproceso = id)
				
	except Subprocesos.DoesNotExist: 
		instancia = None
		instanciaig= None
		
	instanciap = Procesos.objects.get(codproceso= id)

	# instanciaig= InformacionGeneral.objects.filter(subproceso__codproceso=id)
		

	#Formularios

	formulario = SubprocesosForm()	
	Puesto = PuestosEditarForm()
	
	
	#Listados
	listado = Subprocesos.objects.filter(codproceso = id)
	
	
	request.session['proceso'] = id

	
	if request.POST:
			try:
				print 'diruriru3.1'
				campos = Subprocesos()#.objects.filter(codproceso = id)#Subprocesos.objects.filter(codproceso = id)
				campos.codproceso = Procesos.objects.get(pk= id)#None if (request.POST.get('id'))=='' else Procesos.objects.get(codproceso = request.POST.get('id'))
				campos.descsubproceso = request.POST.get('descsubproceso')
				campos.codestado = Estados.objects.get(pk=1)#None if (request.POST.get('codestado'))=='' else Estados.objects.get(codestado = request.POST.get('codestado'))
				# campos.due_osubproceso = None if (request.POST.get('descpuesto'))=='' else Puestos.objects.get(pk=request.POST.get('descpuesto'))#request.POST.get('descpuesto')
				campos.orden_subproceso = request.POST.get('orden_subproceso')
				campos.observaciones = request.POST.get('observaciones')
				# campos.anexo = request.POST.get('anexo')
				campos.fecha_implementacion = datetime.datetime.now()
				try:
					campos.diagrama = request.FILES['flujograma']
					# campos.save()
					# # Guardar Imagen en la base de Datos
					# from django.db import connection
					# with connection.cursor() as cursor:
					# 	try:
					# 		llave=campos.pk	
					# 		query="exec [dbo].[spGuargarImagen] %s,%s"%('Subprocesos',llave)
					# 		cursor.execute(query)
					# 		cursor.close()
					# 	except Exception as e:
					# 		print e
  				except Exception as e:
     					print e
     					mensaje = e			          
				campos.save()
				#formulario = SubprocesosForm(instance = campos)
				tr = request.POST.getlist('descpuesto')	
				for data in tr:

					duenosubproceso = DuenosSubproceso()
					duenosubproceso.subproceso = campos
					duenosubproceso.puesto = Puestos.objects.get(pk = data)
					duenosubproceso.save()

				mensaje='exito'

			except Exception as e:
				print e
			ctx = {
					'formulario': formulario,
					'listado': listado,
					'puesto':Puesto,
					'mensaje': mensaje,
			}
			
			# return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')
			# return HttpResponseRedirect(reverse('subprocesos',args=(id)))
				
						
	else:
		
		ctx = {
			'formulario': formulario,
			'puesto':Puesto,
			'listado': listado,
			
			
		}
			#return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id + '/' )
	#return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')
	return render(request, 'subprocesos_ingreso.html', ctx)

@login_required	
def subprocesos_editar(request, id):
	ctx = {}

	try:
		del request.session['proceso']
		del request.session['subproceso']
		
	except Exception as e:
		pass

	#instancias
	try:
		instancia = Subprocesos.objects.get(pk = id)
		proceso = instancia.codproceso.pk		
	except Subprocesos.DoesNotExist: 
		instancia = None
		instanciaig= None
	
	#Formularios

	formulario = SubprocesosForm(instance=instancia)	
	Puesto = PuestosEditarForm()
	
	subproc= id
		
	request.session['proceso'] = proceso
	request.session['subproceso'] = id



	if request.POST:
			try:
				print 'diruuuuuu'
				print proceso
				campos = Subprocesos.objects.get(pk = id)#.objects.filter(codproceso = id)#Subprocesos.objects.filter(codproceso = id)
				campos.codproceso = Procesos.objects.get(pk= proceso)#None if (request.POST.get('id'))=='' else Procesos.objects.get(codproceso = request.POST.get('id'))
				campos.descsubproceso = request.POST.get('descsubproceso')
				campos.codestado = Estados.objects.get(pk=1)#None if (request.POST.get('codestado'))=='' else Estados.objects.get(codestado = request.POST.get('codestado'))
				# campos.due_osubproceso = None if (request.POST.get('due_osubproceso'))=='' else Puestos.objects.get(pk=request.POST.get('due_osubproceso'))#request.POST.get('descpuesto')
				campos.orden_subproceso = request.POST.get('orden_subproceso')
				campos.observaciones = request.POST.get('observaciones')
				campos.fecha_control = datetime.datetime.now()
				# campos.narrativa = request.POST.get('narrativa')
				#campos.fecha_implementacion = request.POST.get('fecha_implementacion')
				
				#-------Actualizar Orden------------------------------
				from django.db import connection
				with connection.cursor() as cursor:
					try:
						
						query="exec [dbo].[ActualizaOrden] %s,%s"%('Subprocesos',id)
						cursor.execute(query)
					except Exception as e:
						raise e

				try:
							campos.diagrama = request.FILES['diagrama']
							campos.save()
							#Restaurar	
							## Guardar Imagen en la base de Datos
							# from django.db import connection
							# with connection.cursor() as cursor:
							# 	try:
							# 		llave=campos.pk	
							# 		query="exec [dbo].[spGuargarImagen] %s,%s"%('Subprocesos',llave)
							# 		cursor.execute(query)
							# 		cursor.close()
							# 	except Exception as e:
							# 		print e
  				except Exception as e:
     						print e		          
				
				campos.save()

				
				formulario = SubprocesosForm(instance = campos)
				DuenosSubproceso.objects.filter(subproceso= campos).delete()

				tr = request.POST.getlist('descpuesto')	
				for data in tr:

					duenosubproceso = DuenosSubproceso()
					duenosubproceso.subproceso = campos
					duenosubproceso.puesto = Puestos.objects.get(pk = data)
					duenosubproceso.save()
				print 'exitooooo'		
				mensaje='exito'

			except Exception as e:
				raise e #mensaje = e
			ctx = {
					'formulario': formulario,
					'puesto':Puesto,
					'subproc':subproc,
					'mensaje': mensaje,
			}
			# return HttpResponseRedirect(reverse('subprocesos', args=[proceso]))
			# print mensaje
				
						
	else:
		
		ctx = {
			'formulario': formulario,
			'puesto':Puesto,
			'subproc':subproc,
			
			
			
		}
			#return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id + '/' )
	#return HttpResponseRedirect('/procesos/subprocesos/ingreso/'+ id +'/')
	return render(request, 'subprocesos_editar.html', ctx)

@login_required
def actividades_editar(request,id):
	ctx={}
	instancia= Actividades.objects.get(pk=id)
	formularioa= ActividadesForm(instance=instancia)
	tipoactividad = TipoActividadEditarForm()
	proceso=request.session['proceso']
	subprocesos = SubprocesosEditarForm()
	subprocesos.fields['descsubproceso'] = forms.ModelChoiceField(queryset= Subprocesos.objects.filter(codproceso=proceso), label = 'Descripcion de Subproceso')

	if request.POST:
		try:
				
				print request.POST.get('codsubproceso')
				campos = Actividades.objects.get(pk=id)
				campos.codtipoactividad = None if request.POST.get('desctipoactividad') == '' else Tipoactividad.objects.get(pk=request.POST.get('desctipoactividad'))
				campos.ordenactividad = request.POST.get('ordenactividad')
				campos.descripcionactividad = request.POST.get('descripcionactividad')
				campos.nombreactividad = request.POST.get('nombreactividad')
				campos.descripcionactividad = request.POST.get('descripcionactividad')
				campos.codsubproceso = None if request.POST.get('codsubproceso') == '' else Subprocesos.objects.get(pk=request.POST.get('codsubproceso'))
				campos.tiempo = 0 if (request.POST.get('tiempo')) =='' else request.POST.get('tiempo')
				campos.unidadmedida= None if request.POST.get('descripcion') == '' else UnidadesMedida.objects.get(pk=request.POST.get('descripcion'))
				campos.fecha_control = datetime.datetime.now()
				campos.habilitado= "True" if (request.POST.get('habilitado'))=="on" else "False"
				try:
					campos.anexo = request.FILES['anexo']
					campos.save()
					formularioa= ActividadesForm(instance=campos)
					#Restaurar
    				## Guardar Imagen en la base de Datos
					# from django.db import connection
					# with connection.cursor() as cursor:
					# 	try:
					# 		llave=campos.pk	
					# 		query="exec [dbo].[spGuargarImagen] %s,%s"%('Actividades',llave)
					# 		cursor.execute(query)
					# 		cursor.close()
					# 	except Exception as e:
					# 		print e
  				except Exception as e:
     					mensaje= e	
     					campos.save()
     					formularioa= ActividadesForm(instance=campos)
				
     			#-------Actualizar Orden------------------------------
				from django.db import connection
				with connection.cursor() as cursor:
					try:
						print "TBBT"
						
						subproceso=request.POST.get('codsubproceso')
						query="exec [dbo].[ActualizaOrden] %s,%s"%("Actividades",subproceso)
						print query
						cursor.execute(query)
						cursor.close()
					except Exception as e:
						print e		
				

				#-------Control-----------------------------------------------
				
				#-------- Verificar si existen controles para esta actividad--------------------------------

				try:
					ctrlactividad= Controles.objects.filter(codactividad=id)
				except Controles.DoesNotExist:
					ctrlactividad= None

				if 	not (request.POST.get('habilitado'))=="on" and ctrlactividad != None:
					from django.db import connection
					with connection.cursor() as cursor:
						try:
							query="exec [dbo].[spInhabilitarcontroles] %s"%(id)
						 	cursor.execute(query)
						 	cursor.close()
						except Exception as e:
							raise e
					
				
				# if request.POST.get('desctipoactividad') == "1":
				# 	print 'controool!!!!'
				# 	print request.POST.get('desctipoactividad')
				# 	campControl = Controles()
				# 	campControl.codactividad= campos
				# 	campControl.descripcion = request.POST.get('nombreactividad')
				# 	# campControl.codtipocontrol= "No Asignado" #if request.POST.get('desctipoactividad') == '' else Tipoactividad.objects.get(pk=request.POST.get('desctipoactividad'))
				# 	campControl.save()
				# 	print "Exitosa actividad"
				#------- RACI-------------------------------------------------	
				Raci.objects.filter(codactividad=campos).delete()

				R = request.POST.getlist('Responsable')

				for data in R:

					resp = Raci()
					resp.codactividad = campos
					resp.codraci = None if(request.POST.get('letraR'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraR'))
					resp.codpuesto = Puestos.objects.get(codpuesto=data)
					resp.save()


				A = request.POST.getlist('Acargo')	

				for dataa in A:

					ac = Raci()
					ac.codactividad = campos
					ac.codraci = None if(request.POST.get('letraA'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraA'))
					ac.codpuesto = Puestos.objects.get(codpuesto=dataa)
					ac.save()


				C = request.POST.getlist('Consultar')	
				for datac in C:

					con = Raci()
					con.codactividad = campos
					con.codraci = None if(request.POST.get('letraC'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraC'))
					con.codpuesto = Puestos.objects.get(codpuesto=datac)
					con.save()

				I = request.POST.getlist('Informar')	
				for datai in I:

					inf = Raci()
					inf.codactividad = campos
					inf.codraci = None if(request.POST.get('letraI'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraI'))
					inf.codpuesto = Puestos.objects.get(codpuesto=datai)
					inf.save()
					

				

								
		except Exception as e:
				raise e
		return HttpResponseRedirect(reverse('subprocesos', args=[proceso]))

	else:
			ctx={
				'formularioa':formularioa,
				'tipoactividad':tipoactividad,
				'subprocesos':subprocesos,
				'instancia':instancia,
				'actividadid': id,
			}
	return render(request,'actividades_editar.html',ctx)

@login_required
def actividades_descripcion(request,id):
	ctx={}
	try:
		instanciag = Actividades.objects.get(pk = id)
		bandera='edita'	
	except Actividades.DoesNotExist: 
		bandera='inserta'	
		instanciag = None

	try:
		del request.session['proceso']
		
	except Exception as e:
		pass

	instancia= Procesos.objects.get(pk= instanciag.codsubproceso.codproceso.pk)
	proceso=instancia.pk
	formulario = ActividadesForm(instance= instanciag)
	request.session['proceso'] =  proceso

	if request.POST:
			try:
				if bandera=='inserta':
					print 'insert'
					campos = Actividades()
				else:
					campos = Actividades.objects.get(pk= id)
				campos.descripcionactividad = request.POST.get('descripcionactividad')
				campos.save()

				if bandera=='edita':
					print 'edit'
					formulario= ActividadesForm(instance= campos)
				mensaje='exito'
				
			except Exception as e:
				raise e
				mensaje = e
			ctx = {
					'formulario': formulario,
					'mensaje': mensaje,
					'proceso':proceso,
					
			}

			return HttpResponseRedirect(reverse('subprocesos', args=[proceso]))
	else:
			ctx = {
				'formulario': formulario,
				'proceso':proceso,
				
		}
	return render(request, 'actividades_descripcion.html', ctx)

@login_required
def actividades_anexo(request,id):
	ctx={}
	try:
		instanciag = Actividades.objects.get(pk = id)
		bandera='edita'	
	except Actividades.DoesNotExist: 
		bandera='inserta'	
		instanciag = None

	try:
		del request.session['proceso']
		
	except Exception as e:
		pass

	instancia= Procesos.objects.get(pk= instanciag.codsubproceso.codproceso.pk)
	proceso=instancia.pk
	formulario = ActividadesForm(instance= instanciag)
	request.session['proceso'] =  proceso

	if request.POST:
			try:
				if bandera=='inserta':
					print 'insert'
					campos = Actividades()
				else:
					campos = Actividades.objects.get(pk= id)
				campos.anexo = request.FILES['anexo']
				campos.save()
				# Guardar Imagen en la base de Datos
				from django.db import connection
				with connection.cursor() as cursor:
					try:
						llave=campos.pk	
						query="exec [dbo].[spGuargarImagen] %s,%s"%('Actividades',llave)
						cursor.execute(query)
						cursor.close()
					except Exception as e:
						print e

				if bandera=='edita':
					print 'edit'
					formulario= ActividadesForm(instance= campos)
				mensaje='exito'
				
			except Exception as e:
				raise e
				mensaje = e
			ctx = {
					'formulario': formulario,
					'mensaje': mensaje,
					'proceso':proceso,
					'instanciag':instanciag,
					
			}

			return HttpResponseRedirect(reverse('subprocesos', args=[proceso]))
	else:
			ctx = {
				'formulario': formulario,
				'proceso':proceso,
				'instanciag':instanciag,
				
		}
	return render(request, 'actividades_anexo.html', ctx)

@login_required
def infogeneral(request, id):
	ctx={}
	try:
		instanciag = InformacionGeneral.objects.get(proceso = id)
		bandera='edita'	
	except InformacionGeneral.DoesNotExist: 
		bandera='inserta'	
		instanciag = None

	try:
		del request.session['proceso']
		
	except Exception as e:
		pass

	instancia= Procesos.objects.get(pk= id)
	proceso=instancia.pk
	formulario = InformacionForm(instance= instanciag)
	request.session['proceso'] =  proceso

	if request.POST:
			try:
				if bandera=='inserta':
					campos = InformacionGeneral()
				else:
					campos = InformacionGeneral.objects.get(proceso= id)
				campos.proceso = None if(id)=='' else Procesos.objects.get(pk=id)
				campos.introduccion = request.POST.get('introduccion')
				campos.objetivos = request.POST.get('objetivos')
				campos.alcance = request.POST.get('alcance')
				campos.responsabilidad = request.POST.get('responsabilidad')
				campos.revision = request.POST.get('revision')
				campos.cumplimiento=request.POST.get('cumplimiento')
				campos.excepciones= request.POST.get('excepciones')
				campos.definiciones=request.POST.get('definiciones')
				campos.save()

				if bandera=='edita':
					formulario= InformacionForm(instance= campos)
				mensaje='exito'
				
			except Exception as e:
				raise e
				mensaje = e
			ctx = {
					'formulario': formulario,
					'mensaje': mensaje,
					'proceso':proceso,
					
			}

			return HttpResponseRedirect(reverse('subprocesos', args=[proceso]))
	else:
			ctx = {
				'formulario': formulario,
				'proceso':proceso,
				
		}
	return render(request, 'informacion_general.html', ctx)

@login_required
def narrativa(request, id):
	ctx={}
	try:
		instanciag = Subprocesos.objects.get(pk = id)
		bandera='edita'	
	except Subprocesos.DoesNotExist: 
		bandera='inserta'	
		instanciag = None

	try:
		del request.session['proceso']
		
	except Exception as e:
		pass

	instancia= Procesos.objects.get(pk= instanciag.codproceso.pk)
	proceso=instancia.pk
	formulario = SubprocesosForm(instance= instanciag)
	request.session['proceso'] =  proceso

	if request.POST:
			try:
				if bandera=='inserta':
					campos = Subprocesos()
				else:
					campos = Subprocesos.objects.get(pk= id)
				campos.narrativa = request.POST.get('narrativa')
				campos.save()

				if bandera=='edita':
					formulario= SubprocesosForm(instance= campos)
				mensaje='exito'
				
			except Exception as e:
				raise e
				mensaje = e
			ctx = {
					'formulario': formulario,
					'mensaje': mensaje,
					'proceso':proceso,
					
			}

			return HttpResponseRedirect(reverse('subprocesos', args=[proceso]))
	else:
			ctx = {
				'formulario': formulario,
				'proceso':proceso,
				
		}
	return render(request, 'narrativa_subproceso.html', ctx)

@login_required
def matrizriesgo_ingreso(request,id):
	ctx={}
	# instancia = Subprocesos.objects.filter(codproceso=id)
	subprocesos=SubprocesosEditarForm()
	escenarios=EscenarioriesgosEditarForm()
	tiporiesgo = TiposRiesgosEditarForm()
	frecuenciaact=FrecuenciaActividadesRelacionadasRiesgoEditarForm()

	# Probabilidad
	defproceso=DefinicionProcesoEditarForm()
	areasinvolucradas=AreasInvolucradasEditarForm()
	eventos=EventosRiesgoEditarForm()

	#Impacto
	riesgorepc = RiesgoReputacionalEditarForm()
	riesgoinst = RiesgoInstitucionalEditarForm()
	transacciones = TransaccionesEstadosFinancierosEditarForm()
	cumplimiento = CumplimientoNormativoEditarForm()
	tipoproceso = TipoProcesoEditarForm()
	subprocesos.fields['descsubproceso'] = forms.ModelChoiceField(queryset= Subprocesos.objects.filter(codproceso=id), label = 'Descripcion de Subproceso')
	

	if request.POST:
		try:
			
			probabilidad = request.POST.get('escalaprobabilidad')
			impacto = request.POST.get('escalaimpacto')
			print probabilidad
			print "&&&&&&&&&&"
			print impacto
			nivelriesgoinherente= float(probabilidad) * float(impacto)
			zonariesgo=''
				
			try:
				if request.POST.get('especial') == "on":
					zonariesgo=Zonariesgo.objects.get(desde__lte=nivelriesgoinherente,hasta__gte=nivelriesgoinherente)
				else: #request.POST.get('especial') == "Si":
					zonariesgo=ZonaRiesgoEspecial.objects.get(desde__lte=nivelriesgoinherente,hasta__gte=nivelriesgoinherente)
			except Exception as e:
				zonariesgo=0
			print request.POST.get('especial')	
			print "Nivel riesgo"
			print nivelriesgoinherente
			print "zonaaaa"	
			print zonariesgo

			# if nivelriesgoinherente == 1:
			# 	zonariesgo=1
			# elif nivelriesgoinherente == 2 or nivelriesgoinherente == 3:
			# 	zonariesgo = 2
			# elif nivelriesgoinherente == 4 or nivelriesgoinherente == 5 or nivelriesgoinherente == 6:
			# 	zonariesgo = 3
			# elif nivelriesgoinherente == 8 or nivelriesgoinherente == 9 or nivelriesgoinherente == 10 or nivelriesgoinherente == 12:
			# 	zonariesgo = 4
			# elif nivelriesgoinherente == 15 or nivelriesgoinherente == 16 or nivelriesgoinherente == 20 or nivelriesgoinherente == 25:
			# 	zonariesgo = 5
			# else:
			# 	zonariesgo=0

			campos = Subprocesosxescenarios()
			campos.escenario = request.POST.get('escenario') #None if (request.POST.get('descescenario')) =="" else Escnariosriesgos.objects.get(pk=request.POST.get('descescenario'))
			campos.codsubproceso = None if(request.POST.get('descsubproceso')) =="" else Subprocesos.objects.get(pk=request.POST.get('descsubproceso'))
			campos.probabilidad = probabilidad
			campos.impacto= impacto
			campos.nivel_riesgo_inherente = nivelriesgoinherente
			campos.linea_negocio_nivel1 = request.POST.get('linea_negocio_nivel1')
			campos.linea_negocio_nivel2 = request.POST.get('linea_negocio_nivel2')
			campos.frecuencia_actividad=None if (request.POST.get('frecuenciaactiv')) =="" else FrecuenciaActividadesRelacionadasRiesgo.objects.get(pk=request.POST.get('frecuenciaactiv'))
			campos.definicion_proceso=None if (request.POST.get('defproc')) =="" else DefinicionProceso.objects.get(pk=request.POST.get('defproc'))
			campos.areas_involucradas=None if (request.POST.get('areasinvoluc')) =="" else AreasInvolucradas.objects.get(pk=request.POST.get('areasinvoluc'))
			campos.evento_riesgo=None if (request.POST.get('eventriesgo')) =="" else EventosRiesgo.objects.get(pk=request.POST.get('eventriesgo'))
			campos.riesgo_institucional=None if (request.POST.get('riesgo_institucional')) =="" else RiesgoInstitucional.objects.get(pk=request.POST.get('riesgo_institucional'))
			campos.riesgo_reputacional=None if (request.POST.get('riesgo_reputacional')) =="" else RiesgoReputacional.objects.get(pk=request.POST.get('riesgo_reputacional'))
			campos.transacciones_estados_financieros=None if (request.POST.get('transacciones_ef')) =="" else TransaccionesEstadosFinancieros.objects.get(pk=request.POST.get('transacciones_ef'))
			campos.cumplimiento_normativo=None if (request.POST.get('cumplimiento_normativo')) =="" else CumplimientoNormativo.objects.get(pk=request.POST.get('cumplimiento_normativo'))
			campos.tipo_proceso=None if (request.POST.get('tipo_proceso')) =="" else Tipoproceso.objects.get(pk=request.POST.get('tipo_proceso'))
			campos.categoria_riesgo = None if (request.POST.get('categoriariesgo')) =="" else CategoriaRiesgos.objects.get(pk=request.POST.get('categoriariesgo'))
			campos.zonariesgo =None if (zonariesgo) == 0 else Zonariesgo.objects.get(pk=zonariesgo.pk) 
			campos.total_probabilidad = request.POST.get('totalprobabilidad')
			campos.total_impacto = request.POST.get('totalimpacto')
			campos.escala_probabilidad = request.POST.get('escalaprobabilidad')
			campos.clasificacion_probabilidad = request.POST.get('clasifprobabilidad')
			campos.escala_impacto = request.POST.get('escalaimpacto')
			campos.clasificacion_impacto = request.POST.get('clasifimpacto')
			campos.especial="True" if (request.POST.get('especial'))=="on" else "False"
			#.fecha_implementacion	=now.strftime("%Y-%m-%d %H:%M:%S")
			campos.save()

			tr = request.POST.getlist('TipoRiesgo')	
			for data in tr:

				tiporiesgo = TipoRiesgoSubprocesosEscenarios()
				tiporiesgo.codsubprocesosxescenarios = campos
				tiporiesgo.codtiporiesgo = Tiposriesgos.objects.get(pk=data)
				tiporiesgo.save()

			mensaje='exito'

		except Exception as e:
			raise e
			#mensaje= e

		ctx = {
			'subprocesos': subprocesos,
			'escenarios': escenarios,
			'tiporiesgo': tiporiesgo,
			'frecuenciaact': frecuenciaact,
			'defproceso': defproceso,
			'areasinvolucradas': areasinvolucradas,
			'eventos': eventos,
			'riesgorepc': riesgorepc,
			'riesgoinst': riesgoinst,
			'transacciones': transacciones,
			'cumplimiento': cumplimiento,
			'tipoproceso': tipoproceso,
			'mensaje': mensaje,
			
		}
		return HttpResponseRedirect(reverse('subprocesos', args=[id]))

	else:
		ctx = {
			'subprocesos': subprocesos,
			'escenarios': escenarios,
			'tiporiesgo': tiporiesgo,
			'frecuenciaact': frecuenciaact,
			'defproceso': defproceso,
			'areasinvolucradas': areasinvolucradas,
			'eventos': eventos,
			'riesgorepc': riesgorepc,
			'riesgoinst': riesgoinst,
			'transacciones': transacciones,
			'cumplimiento': cumplimiento,
			'tipoproceso': tipoproceso,

		}

	return render(request, 'escenarios_ingreso.html', ctx)

@login_required
def matrizriesgo_editar(request,id):
	ctx={}
	subprocesos=SubprocesosEditarForm()
	instancia = Subprocesosxescenarios.objects.get(pk=id)
	escenario = SubprocesosXEscenariosForm(instance=instancia)
	subproceso = Subprocesosxescenarios.objects.values('codsubproceso__pk','codsubproceso__codproceso__pk').get(pk=id)
	proceso=request.session['proceso']
	print proceso
	subprocesos.fields['descsubproceso'] = forms.ModelChoiceField(queryset= Subprocesos.objects.filter(codproceso=proceso), label = 'Descripcion de Subproceso')
	if request.POST:
		try:
						
			probabilidad = request.POST.get('escalaprobabilidad')
			impacto = request.POST.get('escalaimpacto')
			print probabilidad
			print "&&&&&&&&&&"
			print impacto
			print "&&&&&&&&&&"
			print proceso
			print request.POST.get('codsubproceso')
			nivelriesgoinherente= float(probabilidad) * float(impacto)
			zonariesgo=''

			try:
				if request.POST.get('especial') == "No":
					zonariesgo=Zonariesgo.objects.get(desde__lte=nivelriesgoinherente,hasta__gte=nivelriesgoinherente)
				elif request.POST.get('especial') == "Si":
					zonariesgo=ZonaRiesgoEspecial.objects.get(desde__lte=nivelriesgoinherente,hasta__gte=nivelriesgoinherente)
			except Exception as e:
				zonariesgo=0
			# if nivelriesgoinherente == 1:
			# 	zonariesgo=1
			# elif nivelriesgoinherente == 2 or nivelriesgoinherente == 3:
			# 	zonariesgo = 2
			# elif nivelriesgoinherente == 4 or nivelriesgoinherente == 5 or nivelriesgoinherente == 6:
			# 	zonariesgo = 3
			# elif nivelriesgoinherente == 8 or nivelriesgoinherente == 9 or nivelriesgoinherente == 10 or nivelriesgoinherente == 12:
			# 	zonariesgo = 4
			# elif nivelriesgoinherente == 15 or nivelriesgoinherente == 16 or nivelriesgoinherente == 20 or nivelriesgoinherente == 25:
			# 	zonariesgo = 5
			# else:
			# 	zonariesgo=0

			campos = Subprocesosxescenarios.objects.get(pk=id)
			campos.escenario = request.POST.get('escenario') #None if (request.POST.get('descescenario')) =="" else Escnariosriesgos.objects.get(pk=request.POST.get('descescenario'))
			campos.codsubproceso = None if(request.POST.get('descsubproceso')) =="" else Subprocesos.objects.get(pk=request.POST.get('descsubproceso'))
			campos.probabilidad = probabilidad
			campos.impacto= impacto
			campos.nivel_riesgo_inherente = nivelriesgoinherente
			campos.linea_negocio_nivel1 = request.POST.get('linea_negocio_nivel1')
			campos.linea_negocio_nivel2 = request.POST.get('linea_negocio_nivel2')
			campos.frecuencia_actividad=None if (request.POST.get('frecuenciaactiv')) =="" else FrecuenciaActividadesRelacionadasRiesgo.objects.get(pk=request.POST.get('frecuenciaactiv'))
			campos.definicion_proceso=None if (request.POST.get('defproc')) =="" else DefinicionProceso.objects.get(pk=request.POST.get('defproc'))
			campos.areas_involucradas=None if (request.POST.get('areasinvoluc')) =="" else AreasInvolucradas.objects.get(pk=request.POST.get('areasinvoluc'))
			campos.evento_riesgo=None if (request.POST.get('eventriesgo')) =="" else EventosRiesgo.objects.get(pk=request.POST.get('eventriesgo'))
			campos.riesgo_institucional=None if (request.POST.get('riesgo_institucional')) =="" else RiesgoInstitucional.objects.get(pk=request.POST.get('riesgo_institucional'))
			campos.riesgo_reputacional=None if (request.POST.get('riesgo_reputacional')) =="" else RiesgoReputacional.objects.get(pk=request.POST.get('riesgo_reputacional'))
			campos.transacciones_estados_financieros=None if (request.POST.get('transacciones_ef')) =="" else TransaccionesEstadosFinancieros.objects.get(pk=request.POST.get('transacciones_ef'))
			campos.cumplimiento_normativo=None if (request.POST.get('cumplimiento_normativo')) =="" else CumplimientoNormativo.objects.get(pk=request.POST.get('cumplimiento_normativo'))
			campos.tipo_proceso=None if (request.POST.get('tipo_proceso')) =="" else Tipoproceso.objects.get(pk=request.POST.get('tipo_proceso'))
			campos.categoria_riesgo = None if (request.POST.get('categoriariesgo')) =="" else CategoriaRiesgos.objects.get(pk=request.POST.get('categoriariesgo'))
			campos.zonariesgo =None if (zonariesgo) == 0 else Zonariesgo.objects.get(pk=zonariesgo) 
			campos.total_probabilidad = request.POST.get('totalprobabilidad')
			campos.total_impacto = request.POST.get('totalimpacto')
			campos.escala_probabilidad = request.POST.get('escalaprobabilidad')
			campos.clasificacion_probabilidad = request.POST.get('clasifprobabilidad')
			campos.escala_impacto = request.POST.get('escalaimpacto')
			campos.clasificacion_impacto = request.POST.get('clasifimpacto')
			campos.save()
			escenario = SubprocesosXEscenariosForm(instance=campos)
			TipoRiesgoSubprocesosEscenarios.objects.filter(codsubprocesosxescenarios=campos).delete()

			tr = request.POST.getlist('TipoRiesgo')	
			for data in tr:

				tiporiesgo = TipoRiesgoSubprocesosEscenarios()
				tiporiesgo.codsubprocesosxescenarios = campos
				tiporiesgo.codtiporiesgo = Tiposriesgos.objects.get(pk=data)
				tiporiesgo.save()

			mensaje='exito'

		except Exception as e:
			print e
			mensaje= e

		ctx = {
			'escenario':escenario,
			'escenarioid': id,
			'subproceso': subproceso,
			'subprocesos': subprocesos,
			'instancia': instancia,
			'mensaje': mensaje,
			
		}
		return HttpResponseRedirect(reverse('subprocesos', args=[proceso]))
	else:
		ctx = {	
				'escenario':escenario,
				'escenarioid': id,
				'subproceso': subproceso,
				'subprocesos': subprocesos,
				'instancia': instancia,		
		}
	return render(request, 'escenarios_editar.html', ctx)

@login_required
def detalle_matriz_riesgo(request,id):
	ctx={}
	instancia = Subprocesosxescenarios.objects.get(pk=id)
	escenario = SubprocesosXEscenariosForm(instance=instancia)
	subproceso = Subprocesosxescenarios.objects.values('codsubproceso__pk','codsubproceso__codproceso__pk').get(pk=id)
	ctx = {	
				'escenario':escenario,
				'escenarioid': id,
				'subproceso': subproceso,
				'instancia': instancia,		
		}

	return render(request, 'detalle_matriz_riesgos.html', ctx)

@login_required
def control_ingreso(request):
	ctx={}
	proc=request.session['proceso']
	
	if request.POST:
		try:		
			# Obtenemos el nivel de riesgo inherente del Escenario
			try:
				
				riesgo = Subprocesosxescenarios.objects.get(pk=request.POST.get('escenarioriesgo'))
				nivelriesgoinherente = riesgo.nivel_riesgo_inherente
				# promedio de los controles del escenario
				
			except Subprocesosxescenarios.DoesNotExist:
				riesgo=None
				nivelriesgoinherente = 0
				

			promedio = Controles.objects.filter(escenario=request.POST.get('escenarioriesgo'),habilitado=True).aggregate(Avg('valoracion_control')).values()[0]
			print 'prom'	
			print promedio

			if promedio == None:
				print 'piut'
				promedio = float(request.POST.get('totalcontrol'))
				avg = promedio
				
			else:
				print 'piut2'
				avg = float(promedio)

			print 'Avg'	
			print avg	
			#Se hace el calculo para obtener la efectividad
			efectividad = (avg/100)	

			print 'efectividad'	
			print efectividad
			#Habiendo obtenido el nivel de riesgo inherente y la efectividad obtenemos el Nivel de riesgo residual.

			nivelriesgoresidual=(nivelriesgoinherente * (1 - efectividad))

			nivelriesgoresidual=round(nivelriesgoresidual,0)
			print 'nivelriesgoresidual'	
			print nivelriesgoresidual

			# YA con el riesgo residual se obtiene la zona de riesgo residual

			zonariesgo=''
			try:
				if request.POST.get('especial') == "No":
					zonariesgo=Zonariesgo.objects.get(desde__lte=nivelriesgoresidual,hasta__gte=nivelriesgoresidual)
				elif request.POST.get('especial') == "Si":
					zonariesgo=ZonaRiesgoEspecial.objects.get(desde__lte=nivelriesgoresidual,hasta__gte=nivelriesgoresidual)
			except Exception as e:
				zonariesgo=0

			# zonariesgo=''
			# if nivelriesgoresidual <= 1:
			# 	zonariesgo=1
			# elif nivelriesgoresidual == 2 or nivelriesgoresidual == 3:
			# 	zonariesgo = 2
			# elif nivelriesgoresidual == 4 or nivelriesgoresidual == 5 or nivelriesgoresidual == 6 or nivelriesgoresidual == 7 :
			# 	zonariesgo = 3
			# elif nivelriesgoresidual == 8 or nivelriesgoresidual == 9 or nivelriesgoresidual == 10 or nivelriesgoresidual == 11 or nivelriesgoresidual == 12 or nivelriesgoresidual == 13 or nivelriesgoresidual == 14:
			# 	zonariesgo = 4
			# elif nivelriesgoresidual == 15 or nivelriesgoresidual == 16 or nivelriesgoresidual ==17 or nivelriesgoresidual ==18 or nivelriesgoresidual ==19 or nivelriesgoresidual ==20 or nivelriesgoresidual ==21 or nivelriesgoresidual ==22 or nivelriesgoresidual ==23 or nivelriesgoresidual ==24 or nivelriesgoresidual ==25:
			# 	zonariesgo = 5
			# else:
			# 	zonariesgo=0
			
			print zonariesgo		
			campos = Controles()
			campos.codactividad = None if(request.POST.get('codactividad'))=="" else Actividades.objects.get(pk=request.POST.get('codactividad'))
			campos.codtipocontrol = None if (request.POST.get('codtipocontrol'))=="" else Tipocontrol.objects.get(pk=request.POST.get('codtipocontrol'))
			campos.codnaturaleza = None if (request.POST.get('codnaturaleza'))=="" else Naturalezacontrol.objects.get(pk=request.POST.get('codnaturaleza'))
			campos.frecuencia = None if (request.POST.get('frecuencia'))=="" else FrecuenciaControl.objects.get(pk=request.POST.get('frecuencia'))
			campos.observaciones_auditoria = None if (request.POST.get('observaciones_auditoria'))=="" else ObservacionesAuditoria.objects.get(pk=request.POST.get('observaciones_auditoria'))
			campos.escenario = None if(request.POST.get('escenarioriesgo'))=="" else Subprocesosxescenarios.objects.get(pk=request.POST.get('escenarioriesgo'))
			campos.valoracion_control = request.POST.get('totalcontrol')
			campos.descripcion = request.POST.get('descripcion')
			campos.efectividad = request.POST.get('totalcontrol')
			campos.nivel_riesgo_residual = nivelriesgoresidual
			campos.zona_riesgo =None if (zonariesgo) == 0 else Zonariesgo.objects.get(pk=zonariesgo) 
			campos.escala = request.POST.get('escalacontrol')
			campos.clasificacion = request.POST.get('clasifcontrol')
			campos.save()
			

			#Guardar Efectividad total del escenario
			escenario = Subprocesosxescenarios.objects.get(pk=request.POST.get('escenarioriesgo'))
			escenario.efectividad= efectividad
			escenario.save()
			mensaje='exito'

		except Exception as e:
			print e
			mensaje = e
		ctx = {
			'mensaje': mensaje,
			
		}

		return HttpResponseRedirect(reverse('subprocesos',args=[proc]))
	else:
			ctx = {	
						
		}

	return render(request, 'control_ingreso.html', ctx)

@login_required
def matrizcontrol_editar(request,id):
	ctx={}
	instancia= Controles.objects.get(pk=id)
	control = ControlesForm(instance=instancia)
	subproceso = Controles.objects.values('codactividad__codsubproceso__pk','codactividad__codsubproceso__codproceso__pk','escenario__codsubproceso__pk','escenario__codsubproceso__codproceso__pk').get(codcontrol=id)
	proc=request.session['proceso']

	if request.POST:
		try:
			
			# Obtenemos el nivel de riesgo inherente del Escenario
			try:
				
				riesgo = Subprocesosxescenarios.objects.get(pk=request.POST.get('escenarioriesgo'))
				nivelriesgoinherente = riesgo.nivel_riesgo_inherente
				# promedio de los controles del escenario
				
			except Subprocesosxescenarios.DoesNotExist:
				riesgo=None
				nivelriesgoinherente = 0
				

			promedio = Controles.objects.filter(escenario=request.POST.get('escenarioriesgo'),habilitado=True).aggregate(Avg('valoracion_control')).values()[0]
			print 'prom'	
			print promedio

			if promedio == None:
				print 'piut'
				promedio = float(request.POST.get('totalcontrol'))
				avg = promedio
				
			else:
				print 'piut2'
				avg = float(promedio)

			print 'Avg'	
			print avg	
			#Se hace el calculo para obtener la efectividad
			efectividad = (avg/100)	

			print 'efectividad'	
			print efectividad
			#Habiendo obtenido el nivel de riesgo inherente y la efectividad obtenemos el Nivel de riesgo residual.

			nivelriesgoresidual=(nivelriesgoinherente * (1 - efectividad))

			nivelriesgoresidual=round(nivelriesgoresidual,0)
			print 'nivelriesgoresidual'	
			print nivelriesgoresidual

			# YA con el riesgo residual se obtiene la zona de riesgo residual

			zonariesgo=''
			try:
				if request.POST.get('especial') == "No":
					zonariesgo=Zonariesgo.objects.get(desde__lte=nivelriesgoresidual,hasta__gte=nivelriesgoresidual)
				elif request.POST.get('especial') == "Si":
					zonariesgo=ZonaRiesgoEspecial.objects.get(desde__lte=nivelriesgoresidual,hasta__gte=nivelriesgoresidual)
			except Exception as e:
				zonariesgo=0

			# if nivelriesgoresidual <= 1:
			# 	zonariesgo=1
			# elif nivelriesgoresidual == 2 or nivelriesgoresidual == 3:
			# 	zonariesgo = 2
			# elif nivelriesgoresidual == 4 or nivelriesgoresidual == 5 or nivelriesgoresidual == 6 or nivelriesgoresidual == 7 :
			# 	zonariesgo = 3
			# elif nivelriesgoresidual == 8 or nivelriesgoresidual == 9 or nivelriesgoresidual == 10 or nivelriesgoresidual == 11 or nivelriesgoresidual == 12 or nivelriesgoresidual == 13 or nivelriesgoresidual == 14:
			# 	zonariesgo = 4
			# elif nivelriesgoresidual == 15 or nivelriesgoresidual == 16 or nivelriesgoresidual ==17 or nivelriesgoresidual ==18 or nivelriesgoresidual ==19 or nivelriesgoresidual ==20 or nivelriesgoresidual ==21 or nivelriesgoresidual ==22 or nivelriesgoresidual ==23 or nivelriesgoresidual ==24 or nivelriesgoresidual ==25:
			# 	zonariesgo = 5
			# else:
			# 	zonariesgo=0
			
			print zonariesgo		
			campos = Controles.objects.get(pk=id)
			campos.codactividad = None if(request.POST.get('codactividad'))=="" else Actividades.objects.get(pk=request.POST.get('codactividad'))
			campos.codtipocontrol = None if (request.POST.get('codtipocontrol'))=="" else Tipocontrol.objects.get(pk=request.POST.get('codtipocontrol'))
			campos.codnaturaleza = None if (request.POST.get('codnaturaleza'))=="" else Naturalezacontrol.objects.get(pk=request.POST.get('codnaturaleza'))
			campos.frecuencia = None if (request.POST.get('frecuencia'))=="" else FrecuenciaControl.objects.get(pk=request.POST.get('frecuencia'))
			campos.observaciones_auditoria = None if (request.POST.get('observaciones_auditoria'))=="" else ObservacionesAuditoria.objects.get(pk=request.POST.get('observaciones_auditoria'))
			campos.escenario = None if(request.POST.get('escenarioriesgo'))=="" else Subprocesosxescenarios.objects.get(pk=request.POST.get('escenarioriesgo'))
			campos.valoracion_control = request.POST.get('totalcontrol')
			campos.descripcion = request.POST.get('descripcion')
			campos.efectividad = request.POST.get('totalcontrol')
			campos.nivel_riesgo_residual = nivelriesgoresidual
			campos.zona_riesgo =None if (zonariesgo) == 0 else Zonariesgo.objects.get(pk=zonariesgo) 
			campos.escala = request.POST.get('escalacontrol')
			campos.clasificacion = request.POST.get('clasifcontrol')
			campos.habilitado= "True" if (request.POST.get('habilitado'))=="on" else "False"
			campos.save()
			ControlesForm(instance=campos)

			#Guardar Efectividad total del escenario
			escenario = Subprocesosxescenarios.objects.get(pk=request.POST.get('escenarioriesgo'))
			escenario.efectividad= efectividad
			escenario.save()
			mensaje='exito'

		except Exception as e:
			print e
			mensaje = e
		ctx = {
			'mensaje': mensaje,
			'subproceso':subproceso,
			'control':control,
			'controlid': id,
			'instancia': instancia,
		}

		return HttpResponseRedirect(reverse('subprocesos',args=[proc]))
	else:
			ctx = {	
				'subproceso':subproceso,
				'control':control,
				'controlid': id,
				'instancia': instancia.escenario.pk,		
		}

	return render(request, 'controles_editar.html', ctx)

@login_required
def detalle_matriz_control(request,id):
	ctx={}
	instancia= Controles.objects.get(pk=id)
	control = ControlesForm(instance=instancia)
	subproceso = Controles.objects.values('codactividad__codsubproceso__pk','codactividad__codsubproceso__codproceso__pk').get(pk=id)
	proc=request.POST.get('procesoidc')

	ctx = {	
				'subproceso':subproceso,
				'control':control,
				'controlid': id,		
		}

	return render(request, 'control_detalle.html', ctx)

@login_required
def cedula_normativa(request):
	ctx={}
	formulario = CedulaNormativaForm()
	# listado=CedulaNormativa.objects.filter(codproceso=id)
	proceso = request.session['proceso']
	print 'Este es el proceso', proceso
	if request.POST:
		try:
			
			circular = request.POST.getlist('circular[]')
			print "arreglo"
			print circular
			for data in circular:
							
					campos = CedulaNormativa()
					campos.codproceso= request.session['proceso']
					campos.circular = data
					campos.save()
					mensaje = 'exito'
		except Exception as e:
			print e
			mensaje = e

		ctx = {
				'formulario': formulario,
				'mensaje': mensaje,
				# 'listado': listado,
		}
	else:
		#formulario.fields['desctipoarea'] = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
		ctx = {
				'formulario': formulario,
				# 'listado': listado,
		}
				
	return render(request,'cedula_normativa.html', ctx)

@login_required
def cedula_normativa_editar(request,id):
	print 'Este es el id', id
	ctx={}
	instancia=CedulaNormativa.objects.get(pk=id)
	formulario = CedulaNormativaForm(instance=instancia)
	proceso = request.session['proceso']

	if request.POST:
		try:
			
								
					campos = CedulaNormativa.objects.get(pk=id)
					campos.codproceso= proceso
					campos.circular = request.POST.get('circular')
					campos.save()
					formulario=CedulaNormativaForm(instance=campos)
					mensaje = 'exito'
		except Exception as e:
			print 'llllllllllllllllllllllllllllll',e
			mensaje = e

		ctx = {
				'formulario': formulario,
				'mensaje': mensaje,
				
		}
		return HttpResponseRedirect(reverse('subprocesos', args=[proceso]))
	else:
		#formulario.fields['desctipoarea'] = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
		ctx = {
				'formulario': formulario,
				
		}
				
	return render(request,'cedula_normativa_editar.html', ctx)

@login_required
def indicadores_desempenio(request):
	ctx={}
	formulario=IndicadoresDesempenioForm()
	proceso=request.session['proceso']
	if request.POST:
		try:
			#Descripcion
			# descripcion = request.POST.getlist('descripcion[]')
			
			# for data in descripcion:
							
					campos = IndicadoresDesempenio()
					campos.codproceso= proceso
					campos.descripcion= request.POST.get('descripcion')
					campos.definicion= request.POST.get('definicion')
					campos.aceptable= request.POST.get('aceptable')
					campos.inaceptable= request.POST.get('inaceptable')
					campos.periodo_medicion= request.POST.get('periodo_medicion')
					campos.save()
					
						# #aceptable
						# aceptable=request.POST.getlist('aceptable[]')
						
						# for data2 in aceptable:
										
						# 		campos2 = IndicadoresDesempenio.objects.get(pk=campos.pk)
						# 		campos2.aceptable= data2
						# 		campos2.save()
						# #inaceptable
						# inaceptable=request.POST.getlist('inaceptable[]')
						
						# for data3 in inaceptable:
										
						# 		campos3 = IndicadoresDesempenio.objects.get(pk=campos.pk)
						# 		campos3.inaceptable= data3
						# 		campos3.save()
						# #definicion
						# definicion=request.POST.getlist('definicion[]')
						
						# for data4 in definicion:
										
						# 		campos4 = IndicadoresDesempenio.objects.get(pk=campos.pk)
						# 		campos4.definicion= data4
						# 		campos4.save()
						# #periodo medicion
						# periodomedicion=request.POST.getlist('periodo_medicion[]')
						
						# for data5 in periodomedicion:
										
						# 		campos5 = IndicadoresDesempenio.objects.get(pk=campos.pk)
						# 		campos5.periodo_medicion= data5
						# 		campos5.save()
					
					mensaje = 'exito'

		except Exception as e:
			print e
			mensaje = e

		ctx = {
				'formulario': formulario,
				'mensaje': mensaje,
				
		}
	else:
		#formulario.fields['desctipoarea'] = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
		ctx = {
				'formulario': formulario,
				
		}
				
	return render(request,'indicadores_desempenio.html', ctx)

@login_required
def indicadores_desempenio_editar(request,id):
	ctx={}
	instancia=IndicadoresDesempenio.objects.get(pk=id)
	formulario=IndicadoresDesempenioForm(instance=instancia)
	proceso=request.session['proceso']

	if request.POST:
		try:
			#Descripcion
			# descripcion = request.POST.getlist('descripcion[]')
			
			# for data in descripcion:
							
					campos = IndicadoresDesempenio.objects.get(pk=id)
					campos.codproceso= proceso
					campos.descripcion= request.POST.get('descripcion')
					campos.definicion= request.POST.get('definicion')
					campos.aceptable= request.POST.get('aceptable')
					campos.inaceptable= request.POST.get('inaceptable')
					campos.periodo_medicion= request.POST.get('periodo_medicion')
					campos.save()
					formulario=IndicadoresDesempenioForm(instance=campos)
						# #aceptable
						# aceptable=request.POST.getlist('aceptable[]')
						
						# for data2 in aceptable:
										
						# 		campos2 = IndicadoresDesempenio.objects.get(pk=campos.pk)
						# 		campos2.aceptable= data2
						# 		campos2.save()
						# #inaceptable
						# inaceptable=request.POST.getlist('inaceptable[]')
						
						# for data3 in inaceptable:
										
						# 		campos3 = IndicadoresDesempenio.objects.get(pk=campos.pk)
						# 		campos3.inaceptable= data3
						# 		campos3.save()
						# #definicion
						# definicion=request.POST.getlist('definicion[]')
						
						# for data4 in definicion:
										
						# 		campos4 = IndicadoresDesempenio.objects.get(pk=campos.pk)
						# 		campos4.definicion= data4
						# 		campos4.save()
						# #periodo medicion
						# periodomedicion=request.POST.getlist('periodo_medicion[]')
						
						# for data5 in periodomedicion:
										
						# 		campos5 = IndicadoresDesempenio.objects.get(pk=campos.pk)
						# 		campos5.periodo_medicion= data5
						# 		campos5.save()
					
					mensaje = 'exito'


		except Exception as e:
			print e
			mensaje = e

		ctx = {
				'formulario': formulario,
				'mensaje': mensaje,
				
		}
		return HttpResponseRedirect(reverse('subprocesos', args=[proceso]))
	else:
		#formulario.fields['desctipoarea'] = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
		ctx = {
				'formulario': formulario,
				
		}
				
		return render(request,'indicadores_desempenio_editar.html', ctx)

#Guardar Diagramas de Subprocesos
@login_required
def diagrama_subproceso(request,id):
	ctx={}
	formulario = SubprocesosForm()
	
	# listado=CedulaNormativa.objects.filter(codproceso=id)
	subproceso = id
	proceso = Subprocesos.objects.values('codproceso').get(pk=id)
	print 'Este es el proceso', proceso
	if request.POST:
		try:
			
			diagrama = request.FILES.getlist('diagrama[]')
			print "arreglo"
			print diagrama
			for data in diagrama:
							
					campos = ImagenesSubprocesos()
					campos.subproceso=Subprocesos.objects.get(pk=id)
					campos.diagrama = data
					campos.save()
					mensaje = 'exito'
		except Exception as e:
			print e
			mensaje = e

		ctx = {
				'formulario': formulario,
				'mensaje': mensaje,
				# 'listado': listado,
		}
	else:
		#formulario.fields['desctipoarea'] = forms.ModelChoiceField(queryset=Tipoareas.objects.all(), label="Tipo de Area")
		ctx = {
				'formulario': formulario,
				# 'listado': listado,
		}
				
	return render(request,'Diagramas_Subprocesos.html', ctx)

@login_required
def ver_diagramas(request,id):
	ctx={}
	try:
		instanciag = ImagenesSubprocesos.objects.get(pk = id)
		bandera='edita'	
	except Actividades.DoesNotExist: 
		bandera='inserta'	
		instanciag = None

	try:
		del request.session['proceso']
		
	except Exception as e:
		pass

	instancia= Procesos.objects.get(pk= instanciag.subproceso.codproceso.pk)
	proceso=instancia.pk
	formulario = ImagenesSubprocesosForm(instance= instanciag)
	request.session['proceso'] =  proceso

	if request.POST:
			try:
				if bandera=='inserta':
					print 'insert'
					campos = ImagenesSubprocesos()
				else:
					campos = ImagenesSubprocesos.objects.get(pk= id)
				campos.diagrama = request.FILES['diagrama']
				campos.save()
				# Guardar Imagen en la base de Datos
				# from django.db import connection
				# with connection.cursor() as cursor:
				# 	try:
				# 		llave=campos.pk	
				# 		query="exec [dbo].[spGuargarImagen] %s,%s"%('Actividades',llave)
				# 		cursor.execute(query)
				# 		cursor.close()
				# 	except Exception as e:
				# 		print e

				if bandera=='edita':
					print 'edit'
					formulario= ImagenesSubprocesosForm(instance= campos)
				mensaje='exito'
				
			except Exception as e:
				raise e
				mensaje = e
			ctx = {
					'formulario': formulario,
					'mensaje': mensaje,
					'proceso':proceso,
					'instanciag':instanciag,
					
			}

			return HttpResponseRedirect(reverse('subprocesos', args=[proceso]))
	else:
			ctx = {
				'formulario': formulario,
				'proceso':proceso,
				'instanciag':instanciag,
				
		}
	return render(request, 'subprocesos_diagramas.html', ctx)


#===========================================================================================================================#

# @login_required
# def procesos_listado(request):
# 	ctx = {}
# 	listado = Procesos.objects.all()

# 	ctx = {
# 			'listado': listado
# 	}
# 	return render (request, 'procesos_listado.html', ctx)

# @login_required
# def subprocesosescenarios(request, id):
# 	try:
# 		instancia = Subprocesosxescenarios.objects.filter(codsubproceso = id)
# 	except Subprocesosxescenarios.DoesNotExist: 
# 		instancia = None
	
# 	formulario = SubprocesosXEscenariosForm()
# 	listado = Subprocesosxescenarios.objects.filter(codsubproceso = id)
# 	ctx = {}
# 	instanciap = Subprocesos.objects.get(codsubproceso= id)
# 	formulariosubproceso = SubprocesosForm(instance= instanciap)
# 	subprocesos = SubprocesosEditarForm()
# 	Puesto = PuestosEditarForm()
# 	escenario = EscenarioriesgosEditarForm()

# 	if request.POST:
# 		if request.POST['metodo'] == 'subproceso':
# 			print 'subproceso'
# 			try:
# 				print 'diruriru'
# 				campos = Subprocesos.objects.get(pk= id)#.objects.filter(codproceso = id)#Subprocesos.objects.filter(codproceso = id)
# 				campos.codproceso = Procesos.objects.get(pk= id)#None if (request.POST.get('id'))=='' else Procesos.objects.get(codproceso = request.POST.get('id'))
# 				campos.descsubproceso = request.POST.get('descsubproceso')
# 				campos.codestado = Estados.objects.get(pk=1)#None if (request.POST.get('codestado'))=='' else Estados.objects.get(codestado = request.POST.get('codestado'))
# 				campos.due_osubproceso = None if (request.POST.get('descpuesto'))=='' else Puestos.objects.get(pk=request.POST.get('descpuesto'))#request.POST.get('descpuesto')
# 				campos.orden_subproceso = request.POST.get('orden_subproceso')
# 				campos.observaciones = request.POST.get('observaciones')
# 				campos.anexo = request.POST.get('anexo')
# 				#campos.fecha_implementacion = request.POST.get('fecha_implementacion')
# 				campos.save()
# 				formulariosubproceso = SubprocesosForm(instance= campos)
# 				#formulario = SubprocesosForm(instance = campos)
# 				mensaje = 'exito'
# 			except Exception as e:
# 				raise
# 				mensaje = e
			

# 		if request.POST['metodo'] == 'subprocesosxescenarios':
# 			try:
# 				campos = Subprocesosxescenarios()
# 				campos.escenario = request.POST.get('escenario') #None if (request.POST.get('codescenarioriesgo'))=='' else Escnariosriesgos.objects.get(pk=request.POST.get('codescenarioriesgo'))
# 				campos.codsubproceso = None if (request.POST.get('codsubproceso'))=='' else Subprocessos.objects.get(pk=request.POST.get('codsubproceso'))
# 				campos.probabilidad = request.POST.get('probabilidad')
# 				campos.impacto = request.POST.get('impacto')

# 			except Exception as e:
# 				raise e
# 			ctx = {
# 					'formulario': formulario,
# 					'formulariop': formulariosubproceso,
# 					'listado': listado,
# 					'subprocesos': subprocesos,
# 					'mensaje': mensaje,
# 					'puesto': Puesto,
# 					'escenario': escenario,

# 			}
# 			return HttpResponseRedirect('/procesos/subprocesosxescenarios/ingreso/'+ id +'/')
			
			
# 	else:
# 		print 'sopitaaa'
# 		ctx = {
# 			'formulario': formulario,
# 			'formulariop': formulariosubproceso,
# 			'listado': listado,
# 			'subprocesos': subprocesos,
# 			'instanciap': instanciap,
# 			'puesto': Puesto,
# 			'escenario': escenario,
# 		}
			
# 		return render(request, 'subprocesos_escenarios_ingreso.html', ctx)


# @login_required
# def actividades(request):
# 	formulario = ActividadesForm()
# 	listado = Actividades.objects.all()
# 	ctx = {}
# 	tipoactividad = TipoActividadEditarForm()
# 	proceso=request.session['proceso']
# 	subprocesos = SubprocesosEditarForm()
# 	subprocesos.fields['descsubproceso'] = forms.ModelChoiceField(queryset= Subprocesos.objects.filter(codproceso=proceso), label = 'Descripcion de Subproceso')
# 	if request.POST:
# 		try:
# 			campos = Actividades()
# 			campos.codsubproceso = None if (request.POST.get('codsubproceso'))=='' else Subprocesos.objects.get(codsubproceso = request.POST.get('codsubproceso'))
# 			campos.ordenactividad = request.POST.get('ordenactividad')
# 			campos.codtipoactividad = None if (request.POST.get('codtipoactividad'))=='' else Tipoactividad.objects.get(codtipoactividad = request.POST.get('codtipoactividad'))
# 			campos.descripcionactividad = request.POST.get('descripcionactividad')
# 			campos.nombreactividad = request.POST.get('nombreactividad')
# 			campos.horas = request.POST.get('horas')
# 			campos.save()

# 			r = request.POST.getlist('Responsable')

# 			for data in r:

# 				resp = Raci()
# 				resp.codactividad = campos
# 				resp.codraci = None if(request.POST.get('letraR'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraR'))
# 				resp.codpuesto = Puestos.objects.get(id=data)
# 				resp.save()


# 			A = request.POST.getlist('Acargo')	
# 			for data in A:

# 				ac = Raci()
# 				ac.codactividad = campos
# 				ac.codraci = None if(request.POST.get('letraA'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraA'))
# 				ac.codpuesto = Puestos.objects.get(id=data)
# 				ac.save()


# 			C = request.POST.getlist('Consultar')	
# 			for data in A:

# 				con = Raci()
# 				con.codactividad = campos
# 				con.codraci = None if(request.POST.get('letraC'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraC'))
# 				con.codpuesto = Puestos.objects.get(id=data)
# 				con.save()

# 			I = request.POST.getlist('Informar')	
# 			for data in I:

# 				inf = Raci()
# 				inf.codactividad = campos
# 				inf.codraci = None if(request.POST.get('letraI'))=="" else Tiporaci.objects.get(letra=request.POST.get('letraI'))
# 				inf.codpuesto = Puestos.objects.get(id=data)
# 				inf.save()
					
# 			mensaje = 'exito'
# 		except Exception as e:
# 			mensaje = e
# 		ctx = {
# 				'formulario': formulario,
# 				'listado': listado,
# 				'tipoactividad': tipoactividad,
# 				'subprocesos': subprocesos,
# 		}
# 	else:
# 			ctx = {
# 				'formulario': formulario,
# 				'listado': listado,
# 				'tipoactividad': tipoactividad,
# 				'subprocesos': subprocesos,
# 		}
# 	return render(request, 'actividades_ingreso.html', ctx)
#============================================= AJAX ===============================================================================================

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
		procesoe = request.GET['procesoe']
	data = list(Actividades.objects.values('pk','descripcionactividad','nombreactividad').filter(codsubproceso__codproceso=procesoe))
	return HttpResponse(json.dumps(data), content_type='application/json')

def ajaxsubprocesos(request):
	if request.is_ajax():
		codproceso = request.GET['valor']
	data = list(Subprocesos.objects.values('pk','descsubproceso').filter(codproceso=codproceso))
	return HttpResponse(json.dumps(data), content_type='application/json')


def ajaxPuestos(request):
	if request.is_ajax():
		data = list(Puestos.objects.values('pk','descpuesto'))
	return HttpResponse(json.dumps(data),content_type='application/json')	

def ajaxTipoRiesgo(request):
	if request.is_ajax():
		data = list(Tiposriesgos.objects.values('pk','desctiporiesgo'))
	return HttpResponse(json.dumps(data),content_type='application/json')

def ajaxCategoriaRiesgo(request):
	if request.is_ajax():
		data = list(CategoriaRiesgos.objects.values('pk','codcategoria','descripcion'))
	return HttpResponse(json.dumps(data),content_type='application/json')

def ajaxMTiempos(request):
	if request.is_ajax():
		subproceso=dict(Subprocesos.objects.values(''))

def ajaxActividades(request):

	try:
		del request.session['subprocesos']
		del request.session['actividadess']

	except Exception as e:
		request.session['subprocesos']=''
		request.session['actividadess']=''

	if request.is_ajax():
		# proceso= Procesos.objects.filter(pk=request.GET['proceso'])
		subproceso = Subprocesos.objects.filter(codproceso=request.GET['proceso'])
		actsubproceso = Actividades.objects.filter(codsubproceso__codproceso=request.GET['proceso'])
		raciis = Raci.objects.filter(codactividad__codsubproceso__codproceso=request.GET['proceso'])
		control = Controles.objects.filter(codactividad__codsubproceso__codproceso=request.GET['proceso'])

		subprocesos = []

		for s in subproceso:
			array = {}

			array['codsubproceso'] = s.pk	
			array['codproceso'] = s.codproceso.pk
			array['descsubproceso'] = s.descsubproceso
			array['due_osubproceso'] = s.due_osubproceso.descpuesto
			array['orden_subproceso'] = s.orden_subproceso
			array['observaciones'] = s. observaciones
			array['fecha_implementacion'] = s.fecha_implementacion

			dic=[]
			for act in actsubproceso:
				if act.codsubproceso.pk == s.pk:
					actividades={}
					actividades['codactividad'] = act.pk
					actividades['codsubproceso'] = act.codsubproceso.descsubproceso
					actividades['ordenactividad'] = act.ordenactividad
					actividades['codtipoactividad'] = act.codtipoactividad.desctipoactividad
					actividades['descripcionactividad'] = act.descripcionactividad
					actividades['nombreactividad'] = act.nombreactividad
					actividades['tiempo'] = act.tiempo
					actividades['unidadmedida'] = act.unidadmedida.descripcion
					actividades['habilitado'] = act.habilitado
					dic.append(actividades)
			array['actividades'] = dic
			
			subprocesos.append(array)

		actividadess = []
		
		for act2 in actsubproceso:
			array2 = {}

			array2['codactividad'] = act2.pk
			array2['subproc'] = act2.codsubproceso.codsubproceso
			array2['codsubproceso'] = act2.codsubproceso.descsubproceso
			array2['ordenactividad'] = act2.ordenactividad
			array2['codtipoactividad'] = act2.codtipoactividad.desctipoactividad
			array2['descripcionactividad'] = act2.descripcionactividad
			array2['nombreactividad'] = act2.nombreactividad
			array2['tiempo'] = act2.tiempo
			array2['unidadmedida'] = act2.unidadmedida.descripcion

			dicr=[]
			for r in raciis:
				if r.codactividad.pk == act2.pk:
					if r.codraci.letra == 'R':
						racir={}
						racir['idraci'] = r.idraci
						racir['codactividad'] = r.codactividad.nombreactividad
						racir['codraci'] = r.codraci.letra
						racir['codpuesto'] = r.codpuesto.descpuesto
						dicr.append(racir)
			array2['racir'] = dicr

			dica=[]
			for r2 in raciis:
				if r2.codactividad.pk == act2.pk:
					if r2.codraci.letra == "A":
						racia={}
						racia['idraci'] = r2.idraci
						racia['codactividad'] = r2.codactividad.descripcionactividad
						racia['codraci'] = r2.codraci.letra
						racia['codpuesto'] = r2.codpuesto.descpuesto
						dica.append(racia)
			array2['racia'] = dica

			dicc=[]
			for r3 in raciis:
				if r3.codactividad.pk == act2.pk:
					if r3.codraci.letra == "C":
						racic={}
						racic['idraci'] = r3.idraci
						racic['codactividad'] = r3.codactividad.descripcionactividad
						racic['codraci'] = r3.codraci.letra
						racic['codpuesto'] = r3.codpuesto.descpuesto
						dicc.append(racic)
			array2['racic'] = dicc


			dici=[]
			for r4 in raciis:
				if r4.codactividad.pk == act2.pk:
					if r4.codraci.letra == "I":
						racii={}
						racii['idraci'] = r4.idraci
						racii['codactividad'] = r4.codactividad.descripcionactividad
						racii['codraci'] = r4.codraci.letra
						racii['codpuesto'] = r4.codpuesto.descpuesto
						dici.append(racii)
			array2['racii'] = dici

			dicctrl=[]
			for c in control:
				if act2.pk == c.codactividad.pk:
					ctrl={}
					ctrl['codcontrol'] = c.codcontrol
					ctrl['codactividad'] = c.codactividad.descripcionactividad
					ctrl['codtipocontrol'] = c.codtipocontrol
					ctrl['efectividad'] = c.efectividad
					ctrl['nivel_riesgo_residual'] = c.nivel_riesgo_residual
					ctrl['codnaturaleza'] = c.codnaturaleza
					ctrl['descripcion'] = c.descripcion
					ctrl['frecuencia'] = c.frecuencia
					ctrl['observacionesauditoria'] = c.observaciones_auditoria
					ctrl['zona_riesgo'] = c.zona_riesgo
					ctrl['valoracion_control'] = c.valoracion_control
					dicctrl.append(ctrl)
			array2['controles'] = dicctrl 

				# dic3=[]
				# for rr in tiporacii:
				# 	if rr.codraci.letra == r.codraci:
				# 		tiporaci={}
				# 		tiporaci['codraci']= rr.codraci
				# 		tiporaci['letra']=rr.letra
				# 		dic3.append(tiporaci)
				# raci['tiporaci'] = dic3
					
			

			actividadess.append(array2)

			request.session['subprocesos'] = subprocesos
			# request.session['proceso'] = proceso
			request.session['actividadess'] = actividadess

			
			
			data = {
			
			
			'subprocesos':list(subprocesos),
			'actividades':list(actividadess),
			
	
		}

		return HttpResponse(json.dumps(data), content_type='application/json')

def ajaxCargarActividades(request):
	if request.is_ajax():
		actividad=request.GET['actividad']
		actividades=Actividades.objects.filter(pk=actividad)
		racii = Raci.objects.filter(codactividad=actividad)

		actividadess=[]
		for data in actividades:
			array={}
			array['codactividad'] = data.codactividad
			array['codsubproceso'] = data.codsubproceso.pk
			array['ordenactividad'] = data.ordenactividad
			array['codtipoactividad'] = data.codtipoactividad.pk
			array['nombreactividad'] = data.nombreactividad
			array['descripcionactividad'] = data.descripcionactividad
			array['tiempo'] = data.tiempo
			array['unidadmedida'] = data.unidadmedida.pk if data.unidadmedida else"0"
			array['habilitado'] = data.habilitado
			

			dicr=[]
			for r in racii:
				if r.codraci.letra== 'R':
					racir={}
					racir['idraci'] = r.idraci
					racir['codactividad'] = r.codactividad.nombreactividad
					racir['codraci'] = r.codraci.letra
					racir['codpuesto'] = r.codpuesto.pk
					dicr.append(racir)
			array['racir'] = dicr

			dica=[]
			for r in racii:
				if r.codraci.letra== 'A':
					racia={}
					racia['idraci'] = r.idraci
					racia['codactividad'] = r.codactividad.nombreactividad
					racia['codraci'] = r.codraci.letra
					racia['codpuesto'] = r.codpuesto.pk
					dica.append(racia)
			array['racia'] = dica

			dicc=[]
			for r in racii:
				if r.codraci.letra== 'C':
					racic={}
					racic['idraci'] = r.idraci
					racic['codactividad'] = r.codactividad.nombreactividad
					racic['codraci'] = r.codraci.letra
					racic['codpuesto'] = r.codpuesto.pk
					dicc.append(racic)
			array['racic'] = dicc

			dici=[]
			for r in racii:
				if r.codraci.letra== 'I':
					racii={}
					racii['idraci'] = r.idraci
					racii['codactividad'] = r.codactividad.nombreactividad
					racii['codraci'] = r.codraci.letra
					racii['codpuesto'] = r.codpuesto.pk
					dici.append(racii)
			array['racii'] = dici

			actividadess.append(array)

		data = {
			'actividadess':list(actividadess),
		}

		return HttpResponse(json.dumps(data), content_type='application/json')	
def ajaxDuenios(request):
	if request.is_ajax():
		sub = request.GET['subproceso']
		data = list(DuenosSubproceso.objects.values('pk','subproceso','puesto','puesto__descpuesto').filter(subproceso=sub))
	return HttpResponse(json.dumps(data),content_type='application/json')
def ajaxTablaActividades(request):
	if request.is_ajax():

		subproceso=request.GET['subproceso']

		subprocesos = Subprocesos.objects.filter(pk=subproceso)
		duenosubproceso = DuenosSubproceso.objects.filter(subproceso=subproceso)
		actividad=Actividades.objects.filter(codsubproceso=subproceso,habilitado=True).order_by('ordenactividad')
		actividades= list(Actividades.objects.values('pk','nombreactividad','descripcionactividad','codtipoactividad__desctipoactividad','ordenactividad','tiempo','unidadmedida__descripcion','codsubproceso__due_osubproceso').filter(codsubproceso=subproceso,habilitado=True).order_by('ordenactividad'))

		subproceso = []

		#Subprocesos
		for sub in subprocesos:
			array = {}
			array['pk'] = sub.pk
			array['codproceso'] = sub.codproceso.nombre_proceso
			array['descsubproceso'] = sub.descsubproceso
			array['orden_subproceso'] = sub.orden_subproceso
			array['observaciones'] = sub.observaciones
			array['anexo'] = sub.anexo
			array['observaciones'] = sub.observaciones
			array['codestado'] = sub.codestado.descestado
			
			#Duenios de Subproceso
			dicdue=[]
			for due in duenosubproceso:
				if due.subproceso.pk == sub.pk:
					arraydue = {}
					arraydue['subproceso'] = due.subproceso
					arraydue['puesto'] = due.puesto.descpuesto
					dicdue.append(arraydue)
			array['duenios'] = dicdue	

			#Actividades
			dic=[]
			for act in actividad:
				if act.codsubproceso.pk == sub.pk:
					mactividades={}
					mactividades['pk'] = act.pk
					# mactividades['codsubproceso__due_osubproceso'] = act.codsubproceso.due_osubproceso.descpuesto
					mactividades['nombreactividad'] = act.nombreactividad
					mactividades['descripcionactividad'] = act.descripcionactividad
					mactividades['codtipoactividad__desctipoactividad'] = act.codtipoactividad.desctipoactividad
					mactividades['ordenactividad'] = act.ordenactividad
					mactividades['tiempo'] = act.tiempo
					mactividades['unidadmedida__descripcion'] = act.unidadmedida.descripcion if act.unidadmedida else "No Asignado"
					dic.append(mactividades)
			array['actividadess']=dic
			subproceso.append(array)

			# ahh ya lo probo XD

			data={
				'actividades': actividades,
				'subproceso':list(subproceso),
			}
	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json')

#=========================================== Escenarios de Riesgos==================================================================================
def ajaxEscenarios(request):
	if request.is_ajax():
		escenario=request.GET['escenario']
		escenarios = list(
			Subprocesosxescenarios.objects.values(
					'codsubproceso',
					'probabilidad',
					'impacto',
					'nivel_riesgo_inherente',
					'observaciones',
					'linea_negocio_nivel1',
					'linea_negocio_nivel2',
					'categoria_riesgo',
					'frecuencia_actividad',
					'definicion_proceso',
					'areas_involucradas',
					'evento_riesgo',
					'riesgo_institucional',
					'riesgo_reputacional',
					'transacciones_estados_financieros',
					'cumplimiento_normativo',
					'tipo_proceso',

				).filter(pk=escenario))
		tiporiesgo = list(
			TipoRiesgoSubprocesosEscenarios.objects.values(
					'codtiporiesgo',
					'codsubprocesosxescenarios',

			).filter(codsubprocesosxescenarios=escenario))

		data={
			'escenarios': escenarios,
			'tiporiesgo': tiporiesgo,
		}

	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json')	

def ajaxProbabilidad(request):
	if request.is_ajax():
		frecuencia_act= list(FrecuenciaActividadesRelacionadasRiesgo.objects.values('pk','descripcion').filter(habilitado=True))
		def_proceso=list(DefinicionProceso.objects.values('pk','descripcion').filter(habilitado=True))
		areas_involucradas=list(AreasInvolucradas.objects.values('pk','descripcion').filter(habilitado=True))
		eventos_riesgo=list(EventosRiesgo.objects.values('pk','descripcion').filter(habilitado=True))

		data ={
			'frecuencia_act': frecuencia_act,
			'def_proceso': def_proceso,
			'areas_involucradas': areas_involucradas,
			'eventos_riesgo': eventos_riesgo,
		}
	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json')

def ajaxProbabilidadEdicion(request):
	if request.is_ajax():
		escenario=request.GET['cod_escenario']
		s=Subprocesosxescenarios.objects.get(pk=escenario)
		periodo=s.fecha_implementacion.strftime('%Y-%m-%d')
		maxim=FrecuenciaActividadesRelacionadasRiesgo.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		frecuencia_act= list(FrecuenciaActividadesRelacionadasRiesgo.objects.values('pk','descripcion').filter(periodo__date=maxim))
		maxim=DefinicionProceso.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		def_proceso=list(DefinicionProceso.objects.values('pk','descripcion').filter(periodo__date=maxim))
		maxim=AreasInvolucradas.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		areas_involucradas=list(AreasInvolucradas.objects.values('pk','descripcion').filter(periodo__date=maxim))
		maxim=EventosRiesgo.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		eventos_riesgo=list(EventosRiesgo.objects.values('pk','descripcion').filter(periodo__date=maxim))

		data ={
			'frecuencia_act': frecuencia_act,
			'def_proceso': def_proceso,
			'areas_involucradas': areas_involucradas,
			'eventos_riesgo': eventos_riesgo,
		}
	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json')

def ajaxImpacto(request):
	if request.is_ajax():
		
		riesgo_reputacional=list(RiesgoReputacional.objects.values('pk','descripcion').filter(habilitado=True))
		riesgo_institucional=list(RiesgoInstitucional.objects.values('pk','descripcion').filter(habilitado=True))
		transacciones_EF=list(TransaccionesEstadosFinancieros.objects.values('pk','descripcion').filter(habilitado=True))
		cumplimiento_normativo=list(CumplimientoNormativo.objects.values('pk','descripcion').filter(habilitado=True))
		tipo_proceso=list(Tipoproceso.objects.values('pk','desctipoproceso').filter(habilitado=True))
		
		
		data ={
			'riesgo_reputacional': riesgo_reputacional,
			'riesgo_institucional': riesgo_institucional,
			'transacciones_EF': transacciones_EF,
			'cumplimiento_normativo': cumplimiento_normativo,
			'tipo_proceso': tipo_proceso,
			
		}
	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json')


def ajaxImpactoEdicion(request):
	if request.is_ajax():
		escenario=request.GET['cod_escenario']
		s=Subprocesosxescenarios.objects.get(pk=escenario)
		periodo=s.fecha_implementacion.strftime('%Y-%m-%d')
		maxim=RiesgoReputacional.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		riesgo_reputacional=list(RiesgoReputacional.objects.values('pk','descripcion').filter(periodo__date=maxim))
		maxim=RiesgoInstitucional.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		riesgo_institucional=list(RiesgoInstitucional.objects.values('pk','descripcion').filter(periodo__date=maxim))
		maxim=TransaccionesEstadosFinancieros.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		transacciones_EF=list(TransaccionesEstadosFinancieros.objects.values('pk','descripcion').filter(periodo__date=maxim))
		maxim=CumplimientoNormativo.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		cumplimiento_normativo=list(CumplimientoNormativo.objects.values('pk','descripcion').filter(periodo__date=maxim))
		maxim=Tipoproceso.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		tipo_proceso=list(Tipoproceso.objects.values('pk','desctipoproceso').filter(periodo__date=maxim))
		
		
		data ={
			'riesgo_reputacional': riesgo_reputacional,
			'riesgo_institucional': riesgo_institucional,
			'transacciones_EF': transacciones_EF,
			'cumplimiento_normativo': cumplimiento_normativo,
			'tipo_proceso': tipo_proceso,
			
		}
	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json')

def ajaxSumaProbabilidad(request):
	if request.is_ajax():
		totalprob = request.GET['suma_prob']
		especial = request.GET['especial']
		# totalprob=round(totalprob,0)
		if especial == "No":
			data =dict(Escalaprobabilidad.objects.values('escala','desde','hasta','clasificacion').get(desde__lte=totalprob,hasta__gte=totalprob))
		elif especial == "Si":
			data =dict(EscalaProbabilidadEspecial.objects.values('escala','desde','hasta','clasificacion').get(desde__lte=totalprob,hasta__gte=totalprob))
		# Escalaprobabilidad.objects.get(desde__lte=37.5,hasta__gte=37.5)

		# data ={
		# 	'escalaprobabilidad': escalaprobabilidad,
			
		# }
	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json') 

def ajaxSumaImpacto(request):
	if request.is_ajax():
		totalimpact = request.GET['suma_impact']
		especial = request.GET['especial']
		# totalimpact=round(totalimpact,0)
		if especial == "No":
			data =dict(Escalaimpacto.objects.values('escala','desde','hasta','clasificacion').get(desde__lte=totalimpact,hasta__gte=totalimpact))
		elif especial == "Si":
			data =dict(EscalaImpactoEspecial.objects.values('escala','desde','hasta','clasificacion').get(desde__lte=totalimpact,hasta__gte=totalimpact))
		# Escalaprobabilidad.objects.get(desde__lte=37.5,hasta__gte=37.5)

		# data ={
		# 	'escalaprobabilidad': escalaprobabilidad,
			
		# }
	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json') 

def ajaxUnidadMedida(request):
	if request.is_ajax():
		data = list(UnidadesMedida.objects.values('pk','descripcion'))
	return HttpResponse(json.dumps(data),content_type='application/json')



#==============================================================Controles============================================================================
def ajaxControles(request):
	if request.is_ajax():
		control = request.GET['controles']
		subproceso = request.GET['subproceso']
		#especial = request.GET['especial']
		# procesoa = request.GET['procesoa']
		procesoe = request.GET['procesoe']
		# actividades =list(Actividades.objects.values('pk','nombreactividad').filter(Q(codsubproceso__codproceso=procesoa) | Q(codsubproceso__codproceso=procesoe))
		escenarios = list(Subprocesosxescenarios.objects.values('pk','escenario').filter(codsubproceso__codproceso=procesoe))
		tipocontrol = list(Tipocontrol.objects.values('pk','desctipocontrol').filter(habilitado=True))
		naturalezacontrol=list(Naturalezacontrol.objects.values('pk','descnaturaleza').filter(habilitado=True))
		frecuenciacontrol=list(FrecuenciaControl.objects.values('pk','descripcion').filter(habilitado=True))
		observacionesauditoria=list(ObservacionesAuditoria.objects.values('pk','descripcion').filter(habilitado=True))
		# codactividad = list(Controles.objects.values('codactividad').filter(codcontrol=control))
		controlitems = list(Controles.objects.values('escenario','codactividad','codtipocontrol','efectividad','codnaturaleza','descripcion','frecuencia','observaciones_auditoria','habilitado').filter(pk=control))

		data ={
			'escenarios':escenarios,
			'tipocontrol':tipocontrol,
			'naturalezacontrol':naturalezacontrol,
			'frecuenciacontrol':frecuenciacontrol,
			'observacionesauditoria':observacionesauditoria,
			'controlitems': controlitems,
		}

	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json')

def ajaxControlesEdicion(request):
	if request.is_ajax():
		#escenario=request.GET['cod_escenario']
		control = request.GET['controles']
		s=Controles.objects.get(pk=control)
		periodo=s.fecha_implementacion.strftime('%Y-%m-%d')

		
		subproceso = request.GET['subproceso']
		#especial = request.GET['especial']
		# procesoa = request.GET['procesoa']
		procesoe = request.GET['procesoe']
		# actividades =list(Actividades.objects.values('pk','nombreactividad').filter(Q(codsubproceso__codproceso=procesoa) | Q(codsubproceso__codproceso=procesoe))
		escenarios = list(Subprocesosxescenarios.objects.values('pk','escenario').filter(codsubproceso__codproceso=procesoe))
		maxim=Tipocontrol.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		tipocontrol = list(Tipocontrol.objects.values('pk','desctipocontrol').filter(periodo__date=maxim))
		maxim=Naturalezacontrol.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		naturalezacontrol=list(Naturalezacontrol.objects.values('pk','descnaturaleza').filter(periodo__date=maxim))
		maxim=FrecuenciaControl.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		frecuenciacontrol=list(FrecuenciaControl.objects.values('pk','descripcion').filter(periodo__date=maxim))
		maxim=ObservacionesAuditoria.objects.filter(periodo__date__lte=periodo).aggregate(Max('periodo')).get('periodo__max')
		observacionesauditoria=list(ObservacionesAuditoria.objects.values('pk','descripcion').filter(periodo__date=maxim))
		# codactividad = list(Controles.objects.values('codactividad').filter(codcontrol=control))
		controlitems = list(Controles.objects.values('escenario','codactividad','codtipocontrol','efectividad','codnaturaleza','descripcion','frecuencia','observaciones_auditoria','habilitado','especial').filter(pk=control))

		data ={
			'escenarios':escenarios,
			'tipocontrol':tipocontrol,
			'naturalezacontrol':naturalezacontrol,
			'frecuenciacontrol':frecuenciacontrol,
			'observacionesauditoria':observacionesauditoria,
			'controlitems': controlitems,
		}

	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json')	

def ajaxSumaControl(request):
	if request.is_ajax():
		totalctrl = request.GET['suma_control']
		especial = request.GET['especial']
		if especial == "No":
			data =dict(EscalaControl.objects.values('desde','hasta','clasificacion').get(desde__lte=totalctrl,hasta__gte=totalctrl))
		elif especial == "Si":
			data =dict(EscalaControlEspecial.objects.values('desde','hasta','clasificacion').get(desde__lte=totalctrl,hasta__gte=totalctrl))
		# Escalaprobabilidad.objects.get(desde__lte=37.5,hasta__gte=37.5)

		# data ={
		# 	'escalaprobabilidad': escalaprobabilidad,
			
		# }
	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json') 

#=====================================================================================================================	

# Obtener los valores de ponderacion de cada criterio

def ajaxPonderacion(request):
	if request.is_ajax():
		bandera = request.GET['bandera']
		valor = request.GET['valor']
		especial= request.GET['especial']
		print "aqui va especial"
		print especial

		#TipoControl
		if bandera == "1":
			if especial == "No":
				ponderaciones = list(Tipocontrol.objects.values('pk','ponderacion').filter(pk=request.GET['valor']))
			elif especial == "Si":
				ponderaciones = list(Tipocontrol.objects.values('pk','ponderacion_especial').filter(pk=request.GET['valor']).annotate(ponderacion=F('ponderacion_especial')))	
		#Naturaleza del control	
		elif bandera == "2":
			if especial == "No":
				ponderaciones = list(Naturalezacontrol.objects.values('ponderacion').filter(pk=valor))
			if especial == "Si":
				ponderaciones = list(Naturalezacontrol.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))	
		#Frecuencia del control	
		elif bandera == "3":
			if especial == "No":
				ponderaciones = list(FrecuenciaControl.objects.values('ponderacion').filter(pk=valor))
			if especial == "Si":
				ponderaciones = list(FrecuenciaControl.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))	
		#Observaciones de Auditoria	
		elif bandera == "4":
			if especial == "No":
				ponderaciones = list(ObservacionesAuditoria.objects.values('ponderacion').filter(pk=valor))
			if especial == "Si":
				ponderaciones = list(ObservacionesAuditoria.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))
		#--------------------------------PROBABILIDAD------------------------------------------#

		#Frecuencia de la actividad	
		elif bandera == "5":
			if especial == "No":
				ponderaciones = list(FrecuenciaActividadesRelacionadasRiesgo.objects.values('ponderacion').filter(pk=valor))	
			if especial == "Si":
				ponderaciones = list(FrecuenciaActividadesRelacionadasRiesgo.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))		
		#Definicion del Proceso	
		elif bandera == "6":
			if especial == "No":
				ponderaciones = list(DefinicionProceso.objects.values('ponderacion').filter(pk=valor))		
			if especial == "Si":
				ponderaciones = list(DefinicionProceso.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))			
		#Areas Involucradas
		elif bandera == "7":
			if especial == "No":
				ponderaciones = list(AreasInvolucradas.objects.values('ponderacion').filter(pk=valor))
			if especial == "Si":
				ponderaciones = list(AreasInvolucradas.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))		

		#Eventos de Riesgo
		elif bandera == "8":
			if especial == "No":
				ponderaciones = list(EventosRiesgo.objects.values('ponderacion').filter(pk=valor))		
			if especial == "Si":
				ponderaciones = list(EventosRiesgo.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))			
		#-----------------------------------IMPACTO----------------------------------------------#
		#Riesgo Reputacional
		elif bandera == "9":
			if especial == "No":
				ponderaciones = list(RiesgoReputacional.objects.values('ponderacion').filter(pk=valor))
			if especial == "Si":
				ponderaciones = list(RiesgoReputacional.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))
		#Riesgo Institucional
		elif bandera == "10":
			if especial == "No":
				ponderaciones = list(RiesgoInstitucional.objects.values('ponderacion').filter(pk=valor))
			if especial == "Si":
				ponderaciones = list(RiesgoInstitucional.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))
		#Transacciones de Estados Financieros
		elif bandera == "11":
			if especial == "No":
				ponderaciones = list(TransaccionesEstadosFinancieros.objects.values('ponderacion').filter(pk=valor))
			if especial == "Si":
				ponderaciones = list(TransaccionesEstadosFinancieros.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))	
		#Cumplimientos Normativos
		elif bandera == "12":
			if especial == "No":
				ponderaciones = list(CumplimientoNormativo.objects.values('ponderacion').filter(pk=valor))
			if especial == "Si":
				ponderaciones = list(CumplimientoNormativo.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))
		#Tipo de Proceso
		elif bandera == "13":
			if especial == "No":
				ponderaciones = list(Tipoproceso.objects.values('ponderacion').filter(pk=valor))
			if especial == "Si":
				ponderaciones = list(Tipoproceso.objects.values('ponderacion_especial').filter(pk=valor).annotate(ponderacion=F('ponderacion_especial')))
			
		data={
			'ponderaciones': ponderaciones,
		}
	return HttpResponse(json.dumps(data, default=decimal_default), content_type='application/json')	





