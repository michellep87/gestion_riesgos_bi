# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from administracion.models import *
from .models import *

# Create your models here.

class Procesos(models.Model):
    codproceso = models.AutoField(db_column='CodProceso', primary_key=True)  # Field name made lowercase.
    codtipoproceso = models.ForeignKey(Tipoproceso, models.DO_NOTHING, db_column='CodTipoProceso', blank=True, null=True)  # Field name made lowercase.
    nombre_proceso = models.CharField(db_column='NombreProceso', max_length=75, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    idduenoproceso = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='IdDuenoProceso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    fecha_implementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    logoimagen = models.FileField(db_column='LogoImagen',upload_to='upload/', max_length=150, blank=True, null=True)
    class Meta:
        #managed = False
        db_table = 'Procesos'
    def __unicode__(self):
        return u'%s' % (self.nombre_proceso)

class Subprocesos(models.Model):
    codsubproceso = models.AutoField(db_column='CodSubproceso', primary_key=True)  # Field name made lowercase.
    codproceso = models.ForeignKey(Procesos, models.DO_NOTHING, db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    descsubproceso = models.TextField(db_column='DescSubProceso', blank=True, null=True)  # Field name made lowercase.
    due_osubproceso = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='DuenoSubProceso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    orden_subproceso = models.IntegerField(db_column='OrdenSubproceso', blank=True, null=True)  # Field name made lowercase.
    diagrama = models.FileField(db_column='Diagrama', upload_to='upload/', blank=True, null=True, max_length=150)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    anexo = models.CharField(db_column='Anexo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    codestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='CodEstado', blank=True, null=True)  # Field name made lowercase.
    fecha_implementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    narrativa = models.TextField(db_column='Narrativa', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubProcesos'
    def __unicode__(self):
        return u'%s - %s' % (self.codproceso, self.descsubproceso)

class Subprocesosxescenarios(models.Model):
    codsubprocesosxescenarios = models.AutoField(db_column='CodSubProcesosXEscenarios', primary_key=True)  # Field name made lowercase.
    escenario= models.CharField(db_column='EscenarioRiesgo',max_length=200,blank=True,null=True)
    # codescenarioriesgo = models.ForeignKey(Escnariosriesgos, models.DO_NOTHING, db_column='CodEscenarioRiesgo', blank=True, null=True)  # Field name made lowercase.
    codsubproceso = models.ForeignKey(Subprocesos, models.DO_NOTHING, db_column='CodSubproceso', blank=True, null=True, related_name='riesgo_sub')  # Field name made lowercase.
    probabilidad = models.IntegerField(db_column='Probabilidad', blank=True, null=True)  # Field name made lowercase.
    impacto = models.IntegerField(db_column='Impacto', blank=True, null=True)  # Field name made lowercase.
    nivel_riesgo_inherente = models.IntegerField(db_column='NivelRiesgoInherente', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.
    linea_negocio_nivel1 = models.CharField(db_column='LineaNegocioNivel1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    linea_negocio_nivel2 = models.CharField(db_column='LineaNegocioNivel2', max_length=150, blank=True, null=True)  # Field name made lowercase.
    categoria_riesgo = models.ForeignKey(CategoriaRiesgos, models.DO_NOTHING, db_column='CategoriaRiesgo', blank=True, null=True)  # Field name made lowercase.
    tipo_riesgo = models.ForeignKey(Tiposriesgos, models.DO_NOTHING, db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    zonariesgo = models.ForeignKey(Zonariesgo,db_column='ZonaRiesgo', max_length=100, blank=True, null=True) 
    frecuencia_actividad = models.ForeignKey(FrecuenciaActividadesRelacionadasRiesgo, models.DO_NOTHING, db_column='FrecuenciaActividad', blank=True, null=True)  # Field name made lowercase.
    definicion_proceso = models.ForeignKey(DefinicionProceso, models.DO_NOTHING, db_column='DefinicionProceso', blank=True, null=True)  # Field name made lowercase.
    areas_involucradas = models.ForeignKey(AreasInvolucradas, models.DO_NOTHING, db_column='AreasInvolucradas', blank=True, null=True)  # Field name made lowercase.
    evento_riesgo = models.ForeignKey(EventosRiesgo, models.DO_NOTHING, db_column='EventoRiesgo', blank=True, null=True)  # Field name made lowercase.
    riesgo_institucional = models.ForeignKey(RiesgoInstitucional, models.DO_NOTHING, db_column='RiesgoInstitucional', blank=True, null=True)  # Field name made lowercase.
    riesgo_reputacional = models.ForeignKey(RiesgoReputacional, models.DO_NOTHING, db_column='RiesgoReputacional', blank=True, null=True)  # Field name made lowercase.
    transacciones_estados_financieros = models.ForeignKey(TransaccionesEstadosFinancieros, models.DO_NOTHING, db_column='TransaccionesEstadosFinancieros', blank=True, null=True)  # Field name made lowercase.
    cumplimiento_normativo = models.ForeignKey(CumplimientoNormativo, models.DO_NOTHING, db_column='CumplimientoNormativo', blank=True, null=True)  # Field name made lowercase.
    tipo_proceso = models.ForeignKey(Tipoproceso, models.DO_NOTHING, db_column='TipoProceso', blank=True, null=True)  # Field name made lowercase.
    efectividad = models.DecimalField(db_column='Efectividad', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    total_probabilidad = models.DecimalField(db_column='TotalProbabilidad', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    total_impacto = models.DecimalField(db_column='TotalImpacto', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    escala_probabilidad = models.IntegerField(db_column='EscalaProbabilidad', blank=True, null=True)  # Field name made lowercase.
    clasificacion_probabilidad = models.CharField(db_column='ClasificacionProbabilidad', max_length=200, blank=True, null=True)
    escala_impacto = models.IntegerField(db_column='EscalaImpacto', blank=True, null=True)  # Field name made lowercase.
    clasificacion_impacto = models.CharField(db_column='ClasificacionImpacto', max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SubProcesosXEscenarios'
    def __unicode__(self):
        return u'%s - %s' % (self.codsubproceso, self.escenario)



class Actividades(models.Model):
    codactividad = models.AutoField(db_column='CodActividad', primary_key=True)  # Field name made lowercase.
    codsubproceso = models.ForeignKey(Subprocesos, models.DO_NOTHING, db_column='CodSubproceso', blank=True, null=True, related_name='actividad_sub')  # Field name made lowercase.
    ordenactividad = models.IntegerField(db_column='OrdenActividad', blank=True, null=True)  # Field name made lowercase.
    codtipoactividad = models.ForeignKey(Tipoactividad, models.DO_NOTHING, db_column='CodTipoActividad', blank=True, null=True)  # Field name made lowercase.
    nombreactividad = models.CharField(db_column='NombreActividad',max_length=2000, blank=True, null=True)  # Field name made lowercase.
    descripcionactividad = models.TextField(db_column='DescripcionActividad', blank=True, null=True)  # Field name made lowercase.
    tiempo = models.IntegerField(db_column='Tiempo', blank=True, null=True)
    unidadmedida = models.ForeignKey('UnidadesMedida', db_column='UnidadMedida', blank=True, null=True) 
    fecha_control = models.DateTimeField(db_column='FechaControl', blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField()
    anexo = models.FileField(db_column='Anexo', upload_to='upload/', max_length=150, blank=True, null=True)
    anexoimg = models.BinaryField(db_column='AnexoImg', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Actividades'
    def __unicode__(self):
        return u'%s' % (self.descripcionactividad)



class Raci(models.Model):
    idraci = models.AutoField(db_column='IdRaci', primary_key=True)  # Field name made lowercase.
    codactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='CodActividad', blank=True, null=True)  # Field name made lowercase.
    codraci = models.ForeignKey(Tiporaci, models.DO_NOTHING, db_column='CodRaci', blank=True, null=True)  # Field name made lowercase.
    codpuesto = models.ForeignKey(Puestos, models.DO_NOTHING,db_column='CodPuesto', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RACI'
    def __unicode__(self):
        return u'%s' % (self.idraci)


class Controles(models.Model):
    codcontrol = models.AutoField(db_column='CodControl', primary_key=True)  # Field name made lowercase.
    codactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='CodActividad', blank=True, null=True)  # Field name made lowercase.
    codtipocontrol = models.ForeignKey(Tipocontrol, models.DO_NOTHING, db_column='CodTipoControl', blank=True, null=True)  # Field name made lowercase.
    efectividad = models.DecimalField(db_column='Efectividad', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    nivel_riesgo_residual = models.IntegerField(db_column='NivelRiesgoResidual', blank=True, null=True)  # Field name made lowercase.
    codnaturaleza = models.ForeignKey(Naturalezacontrol, models.DO_NOTHING, db_column='CodNaturaleza', blank=True, null=True)  # Field name made lowercase.
    realiza = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='Realiza', blank=True, null=True, related_name='realiza')  # Field name made lowercase.
    ejecuta = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='Ejecuta', blank=True, null=True, related_name='ejecuta')  # Field name made lowercase.
    revisa = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='Revisa', blank=True, null=True, related_name='revisa')  # Field name made lowercase.
    fecha_implementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    frecuencia = models.ForeignKey(FrecuenciaControl, models.DO_NOTHING, db_column='Frecuencia', blank=True, null=True)  # Field name made lowercase.
    observaciones_auditoria = models.ForeignKey(ObservacionesAuditoria, models.DO_NOTHING, db_column='ObservacionesAuditoria', blank=True, null=True)  # Field name made lowercase.
    zona_riesgo = models.ForeignKey(Zonariesgo,db_column='ZonaRiesgo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valoracion_control = models.DecimalField(db_column='ValoracionControl', max_digits=5, decimal_places=1, blank=True, null=True)
    escenario = models.ForeignKey('Subprocesosxescenarios', models.DO_NOTHING, db_column='CodSubProcesoEscenario', blank=True, null=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=200, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'Controles'
    def __unicode__(self):
        return u'%s' % (self.descripcion)

class InformacionGeneral(models.Model):
    introduccion = models.TextField(db_column='Introduccion', blank=True, null=True)  # Field name made lowercase.
    objetivos = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    alcance = models.TextField(db_column='Alcance', blank=True, null=True)  # Field name made lowercase.
    responsabilidad = models.TextField(db_column='Responsabilidad', blank=True, null=True)  # Field name made lowercase.
    revision = models.TextField(db_column='Revision', blank=True, null=True)  # Field name made lowercase.
    cumplimiento = models.TextField(db_column='Cumplimiento', blank=True, null=True)  # Field name made lowercase.
    excepciones = models.TextField(db_column='Excepciones', blank=True, null=True)  # Field name made lowercase.
    proceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    definiciones = models.TextField(db_column='Definiciones', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'InformacionGeneral'

class UnidadesMedida(models.Model):
    descripcion = models.CharField( db_column='DescripcionUnidadMedida', max_length=100,blank=True,null=True)

    class Meta:
        db_table = 'UnidadesMedida'

    def __unicode__(self):
        return u'%s' % (self.descripcion)

class TipoRiesgoSubprocesosEscenarios(models.Model):
    codtiporiesgo = models.ForeignKey(Tiposriesgos, models.DO_NOTHING, db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    codsubprocesosxescenarios = models.ForeignKey(Subprocesosxescenarios, models.DO_NOTHING, db_column='CodSubProcesosXEscenarios', blank=True, null=True, related_name='riesg_escenario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoRiesgoXSubProcesosXEscenarios'

class DuenosSubproceso(models.Model):
   
    subproceso = models.ForeignKey('Subprocesos', models.DO_NOTHING, db_column='CodSubprocreso', blank=True, null=True)  # Field name made lowercase.
    puesto = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='CodPuesto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DuenosXSubProceso'

class CedulaNormativa(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codproceso = models.IntegerField(db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    circular = models.CharField(db_column='Circular', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CedulaNormativa'

class IndicadoresDesempenio(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codproceso = models.IntegerField(db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    definicion = models.CharField(db_column='Definicion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    aceptable = models.CharField(db_column='Aceptable', max_length=500, blank=True, null=True)  # Field name made lowercase.
    inaceptable = models.CharField(db_column='Inaceptable', max_length=500, blank=True, null=True)  # Field name made lowercase.
    periodo_medicion = models.CharField(db_column='PeriodoMedicion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'IndicadoresDesempenio'

class ImagenesSubprocesos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    subproceso = models.ForeignKey('Subprocesos', models.DO_NOTHING, db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    diagrama = models.FileField(db_column='Diagrama',upload_to='upload/', max_length=150, blank=True, null=True)  # Field name made lowercase.
    imagen_diagrama = models.BinaryField(db_column='ImagenDiagrama', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImagenesXSubprocesos'






















