# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Actividades(models.Model):
    codactividad = models.AutoField(db_column='CodActividad', primary_key=True)  # Field name made lowercase.
    codsubproceso = models.ForeignKey('Subprocesos', models.DO_NOTHING, db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    ordenactividad = models.IntegerField(db_column='OrdenActividad', blank=True, null=True)  # Field name made lowercase.
    codtipoactividad = models.ForeignKey('Tipoactividad', models.DO_NOTHING, db_column='CodTipoActividad', blank=True, null=True)  # Field name made lowercase.
    descripcionactividad = models.TextField(db_column='DescripcionActividad', blank=True, null=True)  # Field name made lowercase.
    tiempo = models.IntegerField(db_column='Tiempo', blank=True, null=True)  # Field name made lowercase.
    unidadmedida = models.ForeignKey('Unidadesmedida', models.DO_NOTHING, db_column='UnidadMedida', blank=True, null=True)  # Field name made lowercase.
    nombreactividad = models.CharField(db_column='NombreActividad', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    fechacontrol = models.DateTimeField(db_column='FechaControl', blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField()
    anexo = models.CharField(db_column='Anexo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    anexoimg = models.BinaryField(db_column='AnexoImg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Actividades'


class ActividadesAudit(models.Model):
    codactividad = models.IntegerField(db_column='CodActividad', blank=True, null=True)  # Field name made lowercase.
    codsubproceso = models.IntegerField(db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    ordenactividad = models.IntegerField(db_column='OrdenActividad', blank=True, null=True)  # Field name made lowercase.
    codtipoactividad = models.IntegerField(db_column='CodTipoActividad', blank=True, null=True)  # Field name made lowercase.
    descripcionactividad = models.TextField(db_column='DescripcionActividad', blank=True, null=True)  # Field name made lowercase.
    tiempo = models.IntegerField(db_column='Tiempo', blank=True, null=True)  # Field name made lowercase.
    unidadmedida = models.IntegerField(db_column='UnidadMedida', blank=True, null=True)  # Field name made lowercase.
    nombreactividad = models.CharField(db_column='NombreActividad', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fechacontrol = models.DateTimeField(db_column='FechaControl', blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField()
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    anexo = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Actividades_Audit'


class Areas(models.Model):
    codarea = models.AutoField(db_column='CodArea', primary_key=True)  # Field name made lowercase.
    descarea = models.CharField(db_column='DescArea', max_length=75, blank=True, null=True)  # Field name made lowercase.
    codtipoarea = models.ForeignKey('Tipoareas', models.DO_NOTHING, db_column='CodTipoArea', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Areas'


class Areasinvolucradas(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcionareasinvolucradas = models.CharField(db_column='DescripcionAreasInvolucradas', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AreasInvolucradas'


class AreasinvolucradasAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    descripcionareasinvolucradas = models.CharField(db_column='DescripcionAreasInvolucradas', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AreasInvolucradas_Audit'


class AreasAudit(models.Model):
    codarea = models.IntegerField(db_column='CodArea', blank=True, null=True)  # Field name made lowercase.
    descarea = models.CharField(db_column='DescArea', max_length=75, blank=True, null=True)  # Field name made lowercase.
    codtipoarea = models.IntegerField(db_column='CodTipoArea', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Areas_Audit'


class Categoriariesgos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codcategoria = models.CharField(db_column='CodCategoria', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descripcioncategoria = models.CharField(db_column='DescripcionCategoria', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoriaRiesgos'


class CategoriariesgosAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    codcategoria = models.CharField(db_column='CodCategoria', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descripcioncategoria = models.CharField(db_column='DescripcionCategoria', max_length=300, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CategoriaRiesgos_Audit'


class Cedulanormativa(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codproceso = models.IntegerField(db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    circular = models.CharField(db_column='Circular', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CedulaNormativa'


class CedulanormativaAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    codproceso = models.IntegerField(db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    circular = models.CharField(db_column='Circular', max_length=300, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'CedulaNormativa_Audit'


class Controles(models.Model):
    codcontrol = models.AutoField(db_column='CodControl', primary_key=True)  # Field name made lowercase.
    codactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='CodActividad', blank=True, null=True)  # Field name made lowercase.
    codtipocontrol = models.ForeignKey('Tipocontrol', models.DO_NOTHING, db_column='CodTipoControl', blank=True, null=True)  # Field name made lowercase.
    efectividad = models.DecimalField(db_column='Efectividad', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    nivelriesgoresidual = models.IntegerField(db_column='NivelRiesgoResidual', blank=True, null=True)  # Field name made lowercase.
    riesgoresidual = models.IntegerField(db_column='RiesgoResidual', blank=True, null=True)  # Field name made lowercase.
    codnaturaleza = models.ForeignKey('Naturalezacontrol', models.DO_NOTHING, db_column='CodNaturaleza', blank=True, null=True)  # Field name made lowercase.
    realiza = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Realiza', blank=True, null=True)  # Field name made lowercase.
    ejecuta = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Ejecuta', blank=True, null=True)  # Field name made lowercase.
    revisa = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Revisa', blank=True, null=True)  # Field name made lowercase.
    fechaimplementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    frecuencia = models.ForeignKey('Frecuenciacontrol', models.DO_NOTHING, db_column='Frecuencia', blank=True, null=True)  # Field name made lowercase.
    observacionesauditoria = models.ForeignKey('Observacionesauditoria', models.DO_NOTHING, db_column='ObservacionesAuditoria', blank=True, null=True)  # Field name made lowercase.
    zonariesgo = models.ForeignKey('Zonariesgo', models.DO_NOTHING, db_column='ZonaRiesgo', blank=True, null=True)  # Field name made lowercase.
    valoracioncontrol = models.DecimalField(db_column='ValoracionControl', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    codsubprocesoescenario = models.ForeignKey('Subprocesosxescenarios', models.DO_NOTHING, db_column='CodSubProcesoEscenario', blank=True, null=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    especial = models.NullBooleanField(db_column='Especial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Controles'


class ControlesAudit(models.Model):
    codcontrol = models.IntegerField(db_column='CodControl', blank=True, null=True)  # Field name made lowercase.
    codactividad = models.IntegerField(db_column='CodActividad', blank=True, null=True)  # Field name made lowercase.
    codtipocontrol = models.IntegerField(db_column='CodTipoControl', blank=True, null=True)  # Field name made lowercase.
    efectividad = models.DecimalField(db_column='Efectividad', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    nivelriesgoresidual = models.IntegerField(db_column='NivelRiesgoResidual', blank=True, null=True)  # Field name made lowercase.
    riesgoresidual = models.IntegerField(db_column='RiesgoResidual', blank=True, null=True)  # Field name made lowercase.
    codnaturaleza = models.IntegerField(db_column='CodNaturaleza', blank=True, null=True)  # Field name made lowercase.
    realiza = models.IntegerField(db_column='Realiza', blank=True, null=True)  # Field name made lowercase.
    ejecuta = models.IntegerField(db_column='Ejecuta', blank=True, null=True)  # Field name made lowercase.
    revisa = models.IntegerField(db_column='Revisa', blank=True, null=True)  # Field name made lowercase.
    fechaimplementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    frecuencia = models.IntegerField(db_column='Frecuencia', blank=True, null=True)  # Field name made lowercase.
    observacionesauditoria = models.IntegerField(db_column='ObservacionesAuditoria', blank=True, null=True)  # Field name made lowercase.
    zonariesgo = models.IntegerField(db_column='ZonaRiesgo', blank=True, null=True)  # Field name made lowercase.
    valoracioncontrol = models.DecimalField(db_column='ValoracionControl', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    codsubprocesoescenario = models.IntegerField(db_column='CodSubProcesoEscenario', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    especial = models.NullBooleanField(db_column='Especial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Controles_Audit'


class Criterios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Criterios'


class CriteriosAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Criterios_Audit'


class Cumplimientonormativo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcioncumplimientonormativo = models.CharField(db_column='DescripcionCumplimientoNormativo', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CumplimientoNormativo'


class CumplimientonormativoAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    descripcioncumplimientonormativo = models.CharField(db_column='DescripcionCumplimientoNormativo', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CumplimientoNormativo_Audit'


class Definicionproceso(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripciondefinicionproceso = models.CharField(db_column='DescripcionDefinicionProceso', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DefinicionProceso'


class DefinicionprocesoAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    descripciondefinicionproceso = models.CharField(db_column='DescripcionDefinicionProceso', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DefinicionProceso_Audit'


class Duenosxsubproceso(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codsubprocreso = models.ForeignKey('Subprocesos', models.DO_NOTHING, db_column='CodSubprocreso', blank=True, null=True)  # Field name made lowercase.
    codpuesto = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='CodPuesto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DuenosXSubProceso'


class DuenosxsubprocesoAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    codsubprocreso = models.IntegerField(db_column='CodSubprocreso', blank=True, null=True)  # Field name made lowercase.
    codpuesto = models.IntegerField(db_column='CodPuesto', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'DuenosXSubProceso_Audit'


class Empleadoxareas(models.Model):
    codempeladoxarea = models.AutoField(db_column='CodEmpeladoXArea', primary_key=True)  # Field name made lowercase.
    codarea = models.ForeignKey(Areas, models.DO_NOTHING, db_column='CodArea', blank=True, null=True)  # Field name made lowercase.
    codempleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='CodEmpleado', blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafinal = models.DateTimeField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmpleadoXAreas'


class EmpleadoxareasAudit(models.Model):
    codempeladoxarea = models.IntegerField(db_column='CodEmpeladoXArea', blank=True, null=True)  # Field name made lowercase.
    codarea = models.IntegerField(db_column='CodArea', blank=True, null=True)  # Field name made lowercase.
    codempleado = models.IntegerField(db_column='CodEmpleado', blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateTimeField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fechafinal = models.DateTimeField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EmpleadoXAreas_Audit'


class Empleados(models.Model):
    codempleado = models.AutoField(db_column='CodEmpleado', primary_key=True)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=75, blank=True, null=True)  # Field name made lowercase.
    usuarioad = models.CharField(db_column='UsuarioAD', max_length=75, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=75, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=75, blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empleados'


class EmpleadosAudit(models.Model):
    codempleado = models.IntegerField(db_column='CodEmpleado', blank=True, null=True)  # Field name made lowercase.
    nombrecompleto = models.CharField(db_column='NombreCompleto', max_length=75, blank=True, null=True)  # Field name made lowercase.
    usuarioad = models.CharField(db_column='UsuarioAD', max_length=75, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=75, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=75, blank=True, null=True)  # Field name made lowercase.
    fechaingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Empleados_Audit'


class Escalacontrol(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscalaControl'


class Escalacontrolespecial(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscalaControlEspecial'


class EscalacontrolespecialAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EscalaControlEspecial_Audit'


class EscalacontrolAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EscalaControl_Audit'


class Escalaimpacto(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscalaImpacto'


class Escalaimpactoespecial(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscalaImpactoEspecial'


class EscalaimpactoespecialAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EscalaImpactoEspecial_Audit'


class EscalaimpactoAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EscalaImpacto_Audit'


class Escalaprobabilidad(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscalaProbabilidad'


class Escalaprobabilidadespecial(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscalaProbabilidadEspecial'


class EscalaprobabilidadespecialAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EscalaProbabilidadEspecial_Audit'


class EscalaprobabilidadAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EscalaProbabilidad_Audit'


class Escnariosriesgos(models.Model):
    codescenarioriesgo = models.AutoField(db_column='CodEscenarioRiesgo', primary_key=True)  # Field name made lowercase.
    codriesgo = models.ForeignKey('Riesgos', models.DO_NOTHING, db_column='CodRiesgo', blank=True, null=True)  # Field name made lowercase.
    descescenario = models.TextField(db_column='DescEscenario', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscnariosRiesgos'


class EscnariosriesgosAudit(models.Model):
    codescenarioriesgo = models.IntegerField(db_column='CodEscenarioRiesgo', blank=True, null=True)  # Field name made lowercase.
    codriesgo = models.IntegerField(db_column='CodRiesgo', blank=True, null=True)  # Field name made lowercase.
    descescenario = models.TextField(db_column='DescEscenario', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EscnariosRiesgos_Audit'


class Estados(models.Model):
    codestado = models.AutoField(db_column='CodEstado', primary_key=True)  # Field name made lowercase.
    descestado = models.CharField(db_column='DescEstado', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estados'


class EstadosAudit(models.Model):
    codestado = models.IntegerField(db_column='CodEstado', blank=True, null=True)  # Field name made lowercase.
    descestado = models.CharField(db_column='DescEstado', max_length=75, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Estados_Audit'


class Eventosriesgo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcioneventoriesgo = models.CharField(db_column='DescripcionEventoRiesgo', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventosRiesgo'


class EventosriesgoAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    descripcioneventoriesgo = models.CharField(db_column='DescripcionEventoRiesgo', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EventosRiesgo_Audit'


class Formatos(models.Model):
    codformato = models.AutoField(db_column='CodFormato', primary_key=True)  # Field name made lowercase.
    codcontrol = models.ForeignKey(Controles, models.DO_NOTHING, db_column='CodControl', blank=True, null=True)  # Field name made lowercase.
    anexo = models.CharField(db_column='Anexo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.
    realiza = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Realiza', blank=True, null=True)  # Field name made lowercase.
    ejecuta = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Ejecuta', blank=True, null=True)  # Field name made lowercase.
    revisa = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Revisa', blank=True, null=True)  # Field name made lowercase.
    fechaimplementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Formatos'


class FormatosAudit(models.Model):
    codformato = models.IntegerField(db_column='CodFormato', blank=True, null=True)  # Field name made lowercase.
    codcontrol = models.IntegerField(db_column='CodControl', blank=True, null=True)  # Field name made lowercase.
    anexo = models.CharField(db_column='Anexo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.
    realiza = models.IntegerField(db_column='Realiza', blank=True, null=True)  # Field name made lowercase.
    ejecuta = models.IntegerField(db_column='Ejecuta', blank=True, null=True)  # Field name made lowercase.
    revisa = models.IntegerField(db_column='Revisa', blank=True, null=True)  # Field name made lowercase.
    fechaimplementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Formatos_Audit'


class Frecuenciaactividadesrelacionadasriesgo(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcionfrecuencia = models.CharField(db_column='DescripcionFrecuencia', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FrecuenciaActividadesRelacionadasRiesgo'


class FrecuenciaactividadesrelacionadasriesgoAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    descripcionfrecuencia = models.CharField(db_column='DescripcionFrecuencia', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FrecuenciaActividadesRelacionadasRiesgo_Audit'


class Frecuenciacontrol(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcionfrecuenciacontrol = models.CharField(db_column='DescripcionFrecuenciaControl', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FrecuenciaControl'


class FrecuenciacontrolAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    descripcionfrecuenciacontrol = models.CharField(db_column='DescripcionFrecuenciaControl', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FrecuenciaControl_Audit'


class HistoricoTransacciones(models.Model):
    tipotrn = models.CharField(db_column='TipoTrn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tabla = models.CharField(db_column='Tabla', max_length=128, blank=True, null=True)  # Field name made lowercase.
    pk = models.CharField(db_column='PK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    campo = models.CharField(db_column='Campo', max_length=128, blank=True, null=True)  # Field name made lowercase.
    valororiginal = models.CharField(db_column='ValorOriginal', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    valornuevo = models.CharField(db_column='ValorNuevo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    fechatrn = models.DateTimeField(db_column='FechaTrn', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Historico_Transacciones'


class HistoricoTransaccionesAudit(models.Model):
    tipotrn = models.CharField(db_column='TipoTrn', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tabla = models.CharField(db_column='Tabla', max_length=128, blank=True, null=True)  # Field name made lowercase.
    pk = models.CharField(db_column='PK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    campo = models.CharField(db_column='Campo', max_length=128, blank=True, null=True)  # Field name made lowercase.
    valororiginal = models.CharField(db_column='ValorOriginal', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    valornuevo = models.CharField(db_column='ValorNuevo', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    fechatrn = models.DateTimeField(db_column='FechaTrn', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='Usuario', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Historico_Transacciones_Audit'


class Imagenesxsubprocesos(models.Model):
    codsubproceso = models.ForeignKey('Subprocesos', models.DO_NOTHING, db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    diagrama = models.CharField(db_column='Diagrama', max_length=150, blank=True, null=True)  # Field name made lowercase.
    imagendiagrama = models.BinaryField(db_column='ImagenDiagrama', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImagenesXSubprocesos'


class ImagenesxsubprocesosAudit(models.Model):
    codsubproceso = models.IntegerField(db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    diagrama = models.CharField(db_column='Diagrama', max_length=150, blank=True, null=True)  # Field name made lowercase.
    imagendiagrama = models.BinaryField(db_column='ImagenDiagrama', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ImagenesXSubprocesos_Audit'


class Indicadoresdesempenio(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codproceso = models.IntegerField(db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    definicion = models.CharField(db_column='Definicion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    aceptable = models.CharField(db_column='Aceptable', max_length=500, blank=True, null=True)  # Field name made lowercase.
    inaceptable = models.CharField(db_column='Inaceptable', max_length=500, blank=True, null=True)  # Field name made lowercase.
    periodomedicion = models.CharField(db_column='PeriodoMedicion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IndicadoresDesempenio'


class IndicadoresdesempenioAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    codproceso = models.IntegerField(db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    definicion = models.CharField(db_column='Definicion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    aceptable = models.CharField(db_column='Aceptable', max_length=500, blank=True, null=True)  # Field name made lowercase.
    inaceptable = models.CharField(db_column='Inaceptable', max_length=500, blank=True, null=True)  # Field name made lowercase.
    periodomedicion = models.CharField(db_column='PeriodoMedicion', max_length=200, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    descripcion = models.CharField(db_column='Descripcion', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IndicadoresDesempenio_Audit'


class Informaciongeneral(models.Model):
    introduccion = models.TextField(db_column='Introduccion', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    alcance = models.TextField(db_column='Alcance', blank=True, null=True)  # Field name made lowercase.
    responsabilidad = models.TextField(db_column='Responsabilidad', blank=True, null=True)  # Field name made lowercase.
    revision = models.TextField(db_column='Revision', blank=True, null=True)  # Field name made lowercase.
    cumplimiento = models.TextField(db_column='Cumplimiento', blank=True, null=True)  # Field name made lowercase.
    excepciones = models.TextField(db_column='Excepciones', blank=True, null=True)  # Field name made lowercase.
    codproceso = models.ForeignKey('Procesos', models.DO_NOTHING, db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    definiciones = models.TextField(db_column='Definiciones', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InformacionGeneral'


class InformaciongeneralAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    introduccion = models.TextField(db_column='Introduccion', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    alcance = models.TextField(db_column='Alcance', blank=True, null=True)  # Field name made lowercase.
    responsabilidad = models.TextField(db_column='Responsabilidad', blank=True, null=True)  # Field name made lowercase.
    revision = models.TextField(db_column='Revision', blank=True, null=True)  # Field name made lowercase.
    cumplimiento = models.TextField(db_column='Cumplimiento', blank=True, null=True)  # Field name made lowercase.
    excepciones = models.TextField(db_column='Excepciones', blank=True, null=True)  # Field name made lowercase.
    codproceso = models.IntegerField(db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    definiciones = models.TextField(db_column='Definiciones', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'InformacionGeneral_Audit'


class Naturalezacontrol(models.Model):
    codnaturaleza = models.AutoField(db_column='CodNaturaleza', primary_key=True)  # Field name made lowercase.
    descnaturaleza = models.CharField(db_column='DescNaturaleza', max_length=150, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NaturalezaControl'


class NaturalezacontrolAudit(models.Model):
    codnaturaleza = models.IntegerField(db_column='CodNaturaleza', blank=True, null=True)  # Field name made lowercase.
    descnaturaleza = models.CharField(db_column='DescNaturaleza', max_length=150, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NaturalezaControl_Audit'


class Observacionesauditoria(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcionobservacionesauditoria = models.CharField(db_column='DescripcionObservacionesAuditoria', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObservacionesAuditoria'


class ObservacionesauditoriaAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    descripcionobservacionesauditoria = models.CharField(db_column='DescripcionObservacionesAuditoria', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ObservacionesAuditoria_Audit'


class Procesos(models.Model):
    codproceso = models.AutoField(db_column='CodProceso', primary_key=True)  # Field name made lowercase.
    codtipoproceso = models.ForeignKey('Tipoproceso', models.DO_NOTHING, db_column='CodTipoProceso', blank=True, null=True)  # Field name made lowercase.
    nombreproceso = models.CharField(db_column='NombreProceso', max_length=75, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    idduenoproceso = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='IdDuenoProceso', blank=True, null=True)  # Field name made lowercase.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    fechaimplementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    logoimagen = models.CharField(db_column='LogoImagen', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Procesos'


class ProcesosAudit(models.Model):
    codproceso = models.IntegerField(db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    codtipoproceso = models.IntegerField(db_column='CodTipoProceso', blank=True, null=True)  # Field name made lowercase.
    nombreproceso = models.CharField(db_column='NombreProceso', max_length=75, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    idduenoproceso = models.IntegerField(db_column='IdDuenoProceso', blank=True, null=True)  # Field name made lowercase.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    fechaimplementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    logoimagen = models.CharField(db_column='LogoImagen', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Procesos_Audit'


class Puestos(models.Model):
    codpuesto = models.AutoField(db_column='CodPuesto', primary_key=True)  # Field name made lowercase.
    codarea = models.ForeignKey(Areas, models.DO_NOTHING, db_column='CodArea', blank=True, null=True)  # Field name made lowercase.
    descpuesto = models.CharField(db_column='DescPuesto', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Puestos'


class PuestosAudit(models.Model):
    codpuesto = models.IntegerField(db_column='CodPuesto', blank=True, null=True)  # Field name made lowercase.
    codarea = models.IntegerField(db_column='CodArea', blank=True, null=True)  # Field name made lowercase.
    descpuesto = models.CharField(db_column='DescPuesto', max_length=75, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Puestos_Audit'


class Puntajescriterioscontrol(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PuntajesCriteriosControl'


class PuntajescriterioscontrolAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PuntajesCriteriosControl_Audit'


class Puntajescriteriosimpacto(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PuntajesCriteriosImpacto'


class PuntajescriteriosimpactoAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PuntajesCriteriosImpacto_Audit'


class Puntajescriteriosprobabilidad(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PuntajesCriteriosProbabilidad'


class PuntajescriteriosprobabilidadAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=200)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'PuntajesCriteriosProbabilidad_Audit'


class Puntajesxcriterios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    codcriterio = models.ForeignKey(Criterios, models.DO_NOTHING, db_column='CodCriterio', blank=True, null=True)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    puntajeespecial = models.DecimalField(db_column='PuntajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'PuntajesXCriterios'


class PuntajesxcriteriosAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    codcriterio = models.IntegerField(db_column='CodCriterio', blank=True, null=True)  # Field name made lowercase.
    puntaje = models.DecimalField(db_column='Puntaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    puntajeespecial = models.DecimalField(db_column='PuntajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'PuntajesXCriterios_Audit'


class Raci(models.Model):
    idraci = models.AutoField(db_column='IdRaci', primary_key=True)  # Field name made lowercase.
    codactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='CodActividad', blank=True, null=True)  # Field name made lowercase.
    codraci = models.ForeignKey('Tiporaci', models.DO_NOTHING, db_column='CodRaci', blank=True, null=True)  # Field name made lowercase.
    codpuesto = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='CodPuesto', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RACI'


class RaciAudit(models.Model):
    idraci = models.IntegerField(db_column='IdRaci', blank=True, null=True)  # Field name made lowercase.
    codactividad = models.IntegerField(db_column='CodActividad', blank=True, null=True)  # Field name made lowercase.
    codraci = models.IntegerField(db_column='CodRaci', blank=True, null=True)  # Field name made lowercase.
    codpuesto = models.IntegerField(db_column='CodPuesto', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'RACI_Audit'


class Riesgoinstitucional(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcionriesgoinstitucional = models.CharField(db_column='DescripcionRiesgoInstitucional', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RiesgoInstitucional'


class RiesgoinstitucionalAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    descripcionriesgoinstitucional = models.CharField(db_column='DescripcionRiesgoInstitucional', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RiesgoInstitucional_Audit'


class Riesgoreputacional(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripcionriesgorepudial = models.CharField(db_column='DescripcionRiesgoRepudial', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RiesgoReputacional'


class RiesgoreputacionalAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    descripcionriesgorepudial = models.CharField(db_column='DescripcionRiesgoRepudial', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RiesgoReputacional_Audit'


class Riesgos(models.Model):
    codriesgo = models.AutoField(db_column='CodRiesgo', primary_key=True)  # Field name made lowercase.
    codtiporiesgo = models.ForeignKey('Tiposriesgos', models.DO_NOTHING, db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    descriesgo = models.CharField(db_column='DescRiesgo', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Riesgos'


class RiesgosAudit(models.Model):
    codriesgo = models.IntegerField(db_column='CodRiesgo', blank=True, null=True)  # Field name made lowercase.
    codtiporiesgo = models.IntegerField(db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    descriesgo = models.CharField(db_column='DescRiesgo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Riesgos_Audit'


class Subprocesos(models.Model):
    codsubproceso = models.AutoField(db_column='CodSubproceso', primary_key=True)  # Field name made lowercase.
    codproceso = models.ForeignKey(Procesos, models.DO_NOTHING, db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    descsubproceso = models.TextField(db_column='DescSubProceso', blank=True, null=True)  # Field name made lowercase.
    duenosubproceso = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='DuenoSubProceso', blank=True, null=True)  # Field name made lowercase.
    ordensubproceso = models.IntegerField(db_column='OrdenSubproceso', blank=True, null=True)  # Field name made lowercase.
    diagrama = models.CharField(db_column='Diagrama', max_length=150, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    anexo = models.CharField(db_column='Anexo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    codestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='CodEstado', blank=True, null=True)  # Field name made lowercase.
    fechaimplementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    narrativa = models.TextField(db_column='Narrativa', blank=True, null=True)  # Field name made lowercase.
    imagendiagrama = models.BinaryField(db_column='ImagenDiagrama', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubProcesos'


class Subprocesosxescenarios(models.Model):
    codsubprocesosxescenarios = models.AutoField(db_column='CodSubProcesosXEscenarios', primary_key=True)  # Field name made lowercase.
    codsubproceso = models.IntegerField(db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    probabilidad = models.IntegerField(db_column='Probabilidad', blank=True, null=True)  # Field name made lowercase.
    impacto = models.IntegerField(db_column='Impacto', blank=True, null=True)  # Field name made lowercase.
    nivelriesgoinherente = models.IntegerField(db_column='NivelRiesgoInherente', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lineanegocionivel1 = models.CharField(db_column='LineaNegocioNivel1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lineanegocionivel2 = models.CharField(db_column='LineaNegocioNivel2', max_length=150, blank=True, null=True)  # Field name made lowercase.
    categoriariesgo = models.ForeignKey(Categoriariesgos, models.DO_NOTHING, db_column='CategoriaRiesgo', blank=True, null=True)  # Field name made lowercase.
    codtiporiesgo = models.IntegerField(db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    zonariesgo = models.ForeignKey('Zonariesgo', models.DO_NOTHING, db_column='ZonaRiesgo', blank=True, null=True)  # Field name made lowercase.
    escenarioriesgo = models.CharField(db_column='EscenarioRiesgo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    frecuenciaactividad = models.ForeignKey(Frecuenciaactividadesrelacionadasriesgo, models.DO_NOTHING, db_column='FrecuenciaActividad', blank=True, null=True)  # Field name made lowercase.
    definicionproceso = models.ForeignKey(Definicionproceso, models.DO_NOTHING, db_column='DefinicionProceso', blank=True, null=True)  # Field name made lowercase.
    areasinvolucradas = models.ForeignKey(Areasinvolucradas, models.DO_NOTHING, db_column='AreasInvolucradas', blank=True, null=True)  # Field name made lowercase.
    eventoriesgo = models.ForeignKey(Eventosriesgo, models.DO_NOTHING, db_column='EventoRiesgo', blank=True, null=True)  # Field name made lowercase.
    riesgoinstitucional = models.ForeignKey(Riesgoinstitucional, models.DO_NOTHING, db_column='RiesgoInstitucional', blank=True, null=True)  # Field name made lowercase.
    riesgoreputacional = models.ForeignKey(Riesgoreputacional, models.DO_NOTHING, db_column='RiesgoReputacional', blank=True, null=True)  # Field name made lowercase.
    transaccionesestadosfinancieros = models.ForeignKey('Transaccionesestadosfinancieros', models.DO_NOTHING, db_column='TransaccionesEstadosFinancieros', blank=True, null=True)  # Field name made lowercase.
    cumplimientonormativo = models.ForeignKey(Cumplimientonormativo, models.DO_NOTHING, db_column='CumplimientoNormativo', blank=True, null=True)  # Field name made lowercase.
    tipoproceso = models.ForeignKey('Tipoproceso', models.DO_NOTHING, db_column='TipoProceso', blank=True, null=True)  # Field name made lowercase.
    efectividad = models.DecimalField(db_column='Efectividad', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    totalprobabilidad = models.DecimalField(db_column='TotalProbabilidad', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    totalimpacto = models.DecimalField(db_column='TotalImpacto', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    escalaprobabilidad = models.IntegerField(db_column='EscalaProbabilidad', blank=True, null=True)  # Field name made lowercase.
    clasificacionprobabilidad = models.CharField(db_column='ClasificacionProbabilidad', max_length=200, blank=True, null=True)  # Field name made lowercase.
    escalaimpacto = models.IntegerField(db_column='EscalaImpacto', blank=True, null=True)  # Field name made lowercase.
    clasificacionimpacto = models.CharField(db_column='ClasificacionImpacto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fechaimplementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    especial = models.NullBooleanField(db_column='Especial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubProcesosXEscenarios'


class SubprocesosxescenariosAudit(models.Model):
    codsubprocesosxescenarios = models.IntegerField(db_column='CodSubProcesosXEscenarios', blank=True, null=True)  # Field name made lowercase.
    codsubproceso = models.IntegerField(db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    probabilidad = models.IntegerField(db_column='Probabilidad', blank=True, null=True)  # Field name made lowercase.
    impacto = models.IntegerField(db_column='Impacto', blank=True, null=True)  # Field name made lowercase.
    nivelriesgoinherente = models.IntegerField(db_column='NivelRiesgoInherente', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lineanegocionivel1 = models.CharField(db_column='LineaNegocioNivel1', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lineanegocionivel2 = models.CharField(db_column='LineaNegocioNivel2', max_length=150, blank=True, null=True)  # Field name made lowercase.
    categoriariesgo = models.IntegerField(db_column='CategoriaRiesgo', blank=True, null=True)  # Field name made lowercase.
    codtiporiesgo = models.IntegerField(db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    zonariesgo = models.IntegerField(db_column='ZonaRiesgo', blank=True, null=True)  # Field name made lowercase.
    escenarioriesgo = models.CharField(db_column='EscenarioRiesgo', max_length=200, blank=True, null=True)  # Field name made lowercase.
    frecuenciaactividad = models.IntegerField(db_column='FrecuenciaActividad', blank=True, null=True)  # Field name made lowercase.
    definicionproceso = models.IntegerField(db_column='DefinicionProceso', blank=True, null=True)  # Field name made lowercase.
    areasinvolucradas = models.IntegerField(db_column='AreasInvolucradas', blank=True, null=True)  # Field name made lowercase.
    eventoriesgo = models.IntegerField(db_column='EventoRiesgo', blank=True, null=True)  # Field name made lowercase.
    riesgoinstitucional = models.IntegerField(db_column='RiesgoInstitucional', blank=True, null=True)  # Field name made lowercase.
    riesgoreputacional = models.IntegerField(db_column='RiesgoReputacional', blank=True, null=True)  # Field name made lowercase.
    transaccionesestadosfinancieros = models.IntegerField(db_column='TransaccionesEstadosFinancieros', blank=True, null=True)  # Field name made lowercase.
    cumplimientonormativo = models.IntegerField(db_column='CumplimientoNormativo', blank=True, null=True)  # Field name made lowercase.
    tipoproceso = models.IntegerField(db_column='TipoProceso', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    efectividad = models.DecimalField(db_column='Efectividad', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    totalprobabilidad = models.DecimalField(db_column='TotalProbabilidad', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    totalimpacto = models.DecimalField(db_column='TotalImpacto', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    escalaprobabilidad = models.IntegerField(db_column='EscalaProbabilidad', blank=True, null=True)  # Field name made lowercase.
    clasificacionprobabilidad = models.CharField(db_column='ClasificacionProbabilidad', max_length=200, blank=True, null=True)  # Field name made lowercase.
    escalaimpacto = models.IntegerField(db_column='EscalaImpacto', blank=True, null=True)  # Field name made lowercase.
    clasificacionimpacto = models.CharField(db_column='ClasificacionImpacto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fechaimplementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    especial = models.NullBooleanField(db_column='Especial')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubProcesosXEscenarios_Audit'


class SubprocesosAudit(models.Model):
    codsubproceso = models.IntegerField(db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    codproceso = models.IntegerField(db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    descsubproceso = models.TextField(db_column='DescSubProceso', blank=True, null=True)  # Field name made lowercase.
    duenosubproceso = models.IntegerField(db_column='DuenoSubProceso', blank=True, null=True)  # Field name made lowercase.
    ordensubproceso = models.IntegerField(db_column='OrdenSubproceso', blank=True, null=True)  # Field name made lowercase.
    diagrama = models.CharField(db_column='Diagrama', max_length=150, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    anexo = models.CharField(db_column='Anexo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    codestado = models.IntegerField(db_column='CodEstado', blank=True, null=True)  # Field name made lowercase.
    fechaimplementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    narrativa = models.TextField(db_column='Narrativa', blank=True, null=True)  # Field name made lowercase.
    imagendiagrama = models.BinaryField(db_column='ImagenDiagrama', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SubProcesos_Audit'


class Tipoactividad(models.Model):
    codtipoactividad = models.AutoField(db_column='CodTipoActividad', primary_key=True)  # Field name made lowercase.
    desctipoactividad = models.CharField(db_column='DescTipoActividad', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoActividad'


class TipoactividadAudit(models.Model):
    codtipoactividad = models.IntegerField(db_column='CodTipoActividad', blank=True, null=True)  # Field name made lowercase.
    desctipoactividad = models.CharField(db_column='DescTipoActividad', max_length=150, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TipoActividad_Audit'


class Tipoareas(models.Model):
    codtipoarea = models.AutoField(db_column='CodTipoArea', primary_key=True)  # Field name made lowercase.
    desctipoarea = models.CharField(db_column='DescTipoArea', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoAreas'


class TipoareasAudit(models.Model):
    codtipoarea = models.IntegerField(db_column='CodTipoArea', blank=True, null=True)  # Field name made lowercase.
    desctipoarea = models.CharField(db_column='DescTipoArea', max_length=75, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TipoAreas_Audit'


class Tipocontrol(models.Model):
    codtipocontrol = models.AutoField(db_column='CodTipoControl', primary_key=True)  # Field name made lowercase.
    desctipocontrol = models.CharField(db_column='DescTipoControl', max_length=150, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoControl'


class TipocontrolAudit(models.Model):
    codtipocontrol = models.IntegerField(db_column='CodTipoControl', blank=True, null=True)  # Field name made lowercase.
    desctipocontrol = models.CharField(db_column='DescTipoControl', max_length=150, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoControl_Audit'


class Tipoproceso(models.Model):
    codtipoproceso = models.AutoField(db_column='CodTipoProceso', primary_key=True)  # Field name made lowercase.
    desctipoproceso = models.CharField(db_column='DescTipoProceso', max_length=75, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoProceso'


class TipoprocesoAudit(models.Model):
    codtipoproceso = models.IntegerField(db_column='CodTipoProceso', blank=True, null=True)  # Field name made lowercase.
    desctipoproceso = models.CharField(db_column='DescTipoProceso', max_length=75, blank=True, null=True)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoProceso_Audit'


class Tiporaci(models.Model):
    codraci = models.AutoField(db_column='CodRaci', primary_key=True)  # Field name made lowercase.
    letra = models.CharField(db_column='Letra', max_length=1, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoRACI'


class TiporaciAudit(models.Model):
    codraci = models.IntegerField(db_column='CodRaci', blank=True, null=True)  # Field name made lowercase.
    letra = models.CharField(db_column='Letra', max_length=1, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TipoRACI_Audit'


class Tiporiesgoxsubprocesosxescenarios(models.Model):
    codtiporiesgo = models.ForeignKey('Tiposriesgos', models.DO_NOTHING, db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    codsubprocesosxescenarios = models.ForeignKey(Subprocesosxescenarios, models.DO_NOTHING, db_column='CodSubProcesosXEscenarios', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoRiesgoXSubProcesosXEscenarios'


class TiporiesgoxsubprocesosxescenariosAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    codtiporiesgo = models.IntegerField(db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    codsubprocesosxescenarios = models.IntegerField(db_column='CodSubProcesosXEscenarios', blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TipoRiesgoXSubProcesosXEscenarios_Audit'


class Tiposriesgos(models.Model):
    codtiporiesgo = models.AutoField(db_column='CodTipoRiesgo', primary_key=True)  # Field name made lowercase.
    desctiporiesgo = models.CharField(db_column='DescTipoRiesgo', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposRiesgos'


class TiposriesgosAudit(models.Model):
    codtiporiesgo = models.IntegerField(db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    desctiporiesgo = models.CharField(db_column='DescTipoRiesgo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'TiposRiesgos_Audit'


class Transaccionesestadosfinancieros(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    descripciontransaccionesestadosfinancieros = models.CharField(db_column='DescripcionTransaccionesEstadosFinancieros', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransaccionesEstadosFinancieros'


class TransaccionesestadosfinancierosAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    descripciontransaccionesestadosfinancieros = models.CharField(db_column='DescripcionTransaccionesEstadosFinancieros', max_length=150)  # Field name made lowercase.
    porcentaje = models.DecimalField(db_column='Porcentaje', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacion = models.DecimalField(db_column='Ponderacion', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.
    porcentajeespecial = models.DecimalField(db_column='PorcentajeEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    ponderacionespecial = models.DecimalField(db_column='PonderacionEspecial', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    periodo = models.DateTimeField(db_column='Periodo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TransaccionesEstadosFinancieros_Audit'


class Unidadesmedida(models.Model):
    descripcionunidadmedida = models.CharField(db_column='DescripcionUnidadMedida', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnidadesMedida'


class UnidadesmedidaAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    descripcionunidadmedida = models.CharField(db_column='DescripcionUnidadMedida', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'UnidadesMedida_Audit'


class Zonariesgo(models.Model):
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZonaRiesgo'


class Zonariesgoespecial(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZonaRiesgoEspecial'


class ZonariesgoespecialAudit(models.Model):
    id = models.IntegerField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ZonaRiesgoEspecial_Audit'


class ZonariesgoAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ZonaRiesgo_Audit'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=80)
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_group_Audit'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthGroupPermissionsAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_group_permissions_Audit'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthPermissionAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_permission_Audit'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_user_Audit'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserGroupsAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_user_groups_Audit'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthUserUserPermissionsAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions_Audit'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoAdminLogAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'django_admin_log_Audit'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoContentTypeAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'django_content_type_Audit'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoMigrationsAudit(models.Model):
    id = models.IntegerField(blank=True, null=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'django_migrations_Audit'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSessionAudit(models.Model):
    session_key = models.CharField(max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'django_session_Audit'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)


class SysdiagramsAudit(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)
    auditdatastate = models.CharField(db_column='AuditDataState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    auditdmlaction = models.CharField(db_column='AuditDMLAction', max_length=10, blank=True, null=True)  # Field name made lowercase.
    audituser = models.CharField(db_column='AuditUser', max_length=128, blank=True, null=True)  # Field name made lowercase.
    auditdatetime = models.DateTimeField(db_column='AuditDateTime', blank=True, null=True)  # Field name made lowercase.
    updatecolumns = models.TextField(db_column='UpdateColumns', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sysdiagrams_Audit'


class Zona(models.Model):
    id = models.AutoField()
    escala = models.IntegerField(db_column='Escala', blank=True, null=True)  # Field name made lowercase.
    desde = models.DecimalField(db_column='Desde', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    hasta = models.DecimalField(db_column='Hasta', max_digits=5, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    clasificacion = models.CharField(db_column='Clasificacion', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'zona'
