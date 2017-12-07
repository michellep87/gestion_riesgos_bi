from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^procesos/ingreso/$', views.procesos, name= 'procesos'),
	url(r'^procesos/editar/(?P<id>.+)/$', views.procesos_editar, name= 'procesos_editar'),
	url(r'^procesos/cedulanormativa/$',views.cedula_normativa, name='cedula_normativa'),
	url(r'^procesos/indicadoresdesempenio/$',views.indicadores_desempenio, name='indicadores_desempenio'),
	url(r'^procesos/diagramasubprocesos/(?P<id>.+)/$',views.diagrama_subproceso, name='diagrama_subproceso'),
	url(r'^procesos/subprocesos/verdiagrama/(?P<id>.+)/$', views.ver_diagramas, name= 'ver_diagramas'),
	url(r'^procesos/indicadoresdesempenio/editar/(?P<id>.+)/$',views.indicadores_desempenio_editar, name='indicadores_desempenio_editar'),
	
	url(r'^procesos/cedulanormativa/editar/(?P<id>.+)/$',views.cedula_normativa_editar, name='cedula_normativa_editar'),
	# url(r'^procesos/listado/$', views.procesos_listado, name= 'procesos_listado'),
	url(r'^procesos/subprocesos/ingreso/(?P<id>.+)/$', views.subprocesos, name= 'subprocesos'),
	url(r'^procesos/subprocesos/editar/(?P<id>.+)/$', views.subprocesos_editar, name= 'subprocesos_editar'),
	url(r'^procesos/subprocesos/agregar/(?P<id>.+)/$', views.subprocesos_ingreso, name= 'subprocesos_ingreso'),
	url(r'^procesos/subprocesos/Info_General/(?P<id>.+)/$', views.infogeneral, name= 'infogeneral'),
	url(r'^procesos/subprocesos/narrativa/(?P<id>.+)/$', views.narrativa, name= 'narrativa'),
	url(r'^procesos/subprocesos/escenarioriesgo/ingreso/(?P<id>.+)/$', views.matrizriesgo_ingreso, name= 'matrizriesgo_ingreso'),
	url(r'^procesos/subprocesos/controles/editar/(?P<id>.+)/$', views.matrizcontrol_editar, name= 'matrizcontrol_editar'),
	url(r'^procesos/subprocesos/escenarioriesgo/detalle/(?P<id>.+)/$', views.detalle_matriz_riesgo, name= 'detalle_matriz_riesgo'),
	url(r'^procesos/subprocesos/escenarioriesgo/editar/(?P<id>.+)/$', views.matrizriesgo_editar, name= 'matrizriesgo_editar'),
	url(r'^procesos/subprocesos/controles/ingreso/$', views.control_ingreso, name= 'control_ingreso'),
	url(r'^procesos/subprocesos/controles/detalle/(?P<id>.+)/$', views.detalle_matriz_control, name= 'detalle_matriz_control'),
	url(r'^procesos/subprocesos/actividades/descripcion/(?P<id>.+)/$', views.actividades_descripcion, name= 'actividades_descripcion'),
	url(r'^procesos/subprocesos/actividades/anexo/(?P<id>.+)/$', views.actividades_anexo, name= 'actividades_anexo'),
	url(r'^procesos/subprocesos/actividades/editar/(?P<id>.+)/$', views.actividades_editar, name= 'actividades_editar'),


	#Ajax
	url(r'^ajaxproceso/$', views.ajaxproceso, name='ajaxproceso'),
	url(r'^ajaxactividad/$', views.ajaxactividad, name='ajaxactividad'),
	url(r'^ajaxsubprocesos/$', views.ajaxsubprocesos, name='ajaxsubprocesos'),
	url(r'^ajaxPuestos/$', views.ajaxPuestos, name='ajaxPuestos'),
	url(r'^ajaxActividades/$', views.ajaxActividades, name='ajaxActividades'),
	url(r'^ajaxTipoRiesgo/$', views.ajaxTipoRiesgo, name='ajaxTipoRiesgo'),
	url(r'^ajaxCategoriaRiesgo/$', views.ajaxCategoriaRiesgo, name='ajaxCategoriaRiesgo'),
	url(r'^ajaxProbabilidad/$', views.ajaxProbabilidad, name='ajaxProbabilidad'),
	url(r'^ajaxProbabilidadEdicion/$', views.ajaxProbabilidadEdicion, name='ajaxProbabilidadEdicion'),
	url(r'^ajaxImpacto/$', views.ajaxImpacto, name='ajaxImpacto'),
	url(r'^ajaxImpactoEdicion/$', views.ajaxImpactoEdicion, name='ajaxImpactoEdicion'),
	url(r'^ajaxSumaProbabilidad/$', views.ajaxSumaProbabilidad, name='ajaxSumaProbabilidad'),
	url(r'^ajaxSumaImpacto/$', views.ajaxSumaImpacto, name='ajaxSumaImpacto'),
	url(r'^ajaxUnidadMedida/$', views.ajaxUnidadMedida, name='ajaxUnidadMedida'),
	url(r'^ajaxDuenios/$', views.ajaxDuenios, name='ajaxDuenios'),
	url(r'^ajaxControles/$', views.ajaxControles, name='ajaxControles'),
	url(r'^ajaxControlesEdicion/$', views.ajaxControlesEdicion, name='ajaxControlesEdicion'),
	url(r'^ajaxPonderacion/$', views.ajaxPonderacion, name='ajaxPonderacion'),
	url(r'^ajaxSumaControl/$', views.ajaxSumaControl, name='ajaxSumaControl'),
	url(r'^ajaxEscenarios/$', views.ajaxEscenarios, name='ajaxEscenarios'),
	url(r'^ajaxTablaActividades/$', views.ajaxTablaActividades, name='ajaxTablaActividades'),
	url(r'^ajaxCargarActividades/$', views.ajaxCargarActividades, name='ajaxCargarActividades'),
	

	
	
	# url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
 #        'document_root': settings.MEDIA_ROOT
 #    }), 
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)