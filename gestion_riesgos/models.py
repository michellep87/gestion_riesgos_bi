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

    class Meta:
        managed = False
        db_table = 'Actividades'


class Areas(models.Model):
    codarea = models.AutoField(db_column='CodArea', primary_key=True)  # Field name made lowercase.
    descarea = models.CharField(db_column='DescArea', max_length=75, blank=True, null=True)  # Field name made lowercase.
    codtipoarea = models.ForeignKey('Tipoareas', models.DO_NOTHING, db_column='CodTipoArea', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Areas'


class Controles(models.Model):
    codcontrol = models.AutoField(db_column='CodControl', primary_key=True)  # Field name made lowercase.
    codactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='CodActividad', blank=True, null=True)  # Field name made lowercase.
    codtipocontrol = models.ForeignKey('Tipocontrol', models.DO_NOTHING, db_column='CodTipoControl', blank=True, null=True)  # Field name made lowercase.
    efectividad = models.IntegerField(db_column='Efectividad', blank=True, null=True)  # Field name made lowercase.
    nivel_riesgo = models.IntegerField(db_column='NivelRiesgo', blank=True, null=True)  # Field name made lowercase.
    riesgo_residual = models.IntegerField(db_column='RiesgoResidual', blank=True, null=True)  # Field name made lowercase.
    codnaturaleza = models.ForeignKey('Naturalezacontrol', models.DO_NOTHING, db_column='CodNaturaleza', blank=True, null=True)  # Field name made lowercase.
    realiza = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Realiza', blank=True, null=True)  # Field name made lowercase.
    ejecuta = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Ejecuta', blank=True, null=True)  # Field name made lowercase.
    revisa = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Revisa', blank=True, null=True)  # Field name made lowercase.
    fecha_implementacion = models.IntegerField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Controles'


class Empleadoxareas(models.Model):
    codempeladoxarea = models.AutoField(db_column='CodEmpeladoXArea', primary_key=True)  # Field name made lowercase.
    codarea = models.ForeignKey(Areas, models.DO_NOTHING, db_column='CodArea', blank=True, null=True)  # Field name made lowercase.
    codempleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='CodEmpleado', blank=True, null=True)  # Field name made lowercase.
    fecha_inicio = models.DateTimeField(db_column='FechaInicio', blank=True, null=True)  # Field name made lowercase.
    fecha_final = models.DateTimeField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    habilitado = models.NullBooleanField(db_column='Habilitado')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmpleadoXAreas'


class Empleados(models.Model):
    codempleado = models.AutoField(db_column='CodEmpleado', primary_key=True)  # Field name made lowercase.
    nombre_completo = models.CharField(db_column='NombreCompleto', max_length=75, blank=True, null=True)  # Field name made lowercase.
    usuarioad = models.CharField(db_column='UsuarioAD', max_length=75, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=75, blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=75, blank=True, null=True)  # Field name made lowercase.
    fecha_ingreso = models.DateTimeField(db_column='FechaIngreso', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empleados'


class Escnariosriesgos(models.Model):
    codescenarioriesgo = models.AutoField(db_column='CodEscenarioRiesgo', primary_key=True)  # Field name made lowercase.
    codriesgo = models.ForeignKey('Riesgos', models.DO_NOTHING, db_column='CodRiesgo', blank=True, null=True)  # Field name made lowercase.
    descescenario = models.CharField(db_column='DescEscenario', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EscnariosRiesgos'


class Estados(models.Model):
    codestado = models.AutoField(db_column='CodEstado', primary_key=True)  # Field name made lowercase.
    descestado = models.CharField(db_column='DescEstado', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estados'


class Formatos(models.Model):
    codformato = models.AutoField(db_column='CodFormato', primary_key=True)  # Field name made lowercase.
    codcontrol = models.ForeignKey(Controles, models.DO_NOTHING, db_column='CodControl', blank=True, null=True)  # Field name made lowercase.
    anexo = models.CharField(db_column='Anexo', max_length=150, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.
    realiza = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Realiza', blank=True, null=True)  # Field name made lowercase.
    ejecuta = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Ejecuta', blank=True, null=True)  # Field name made lowercase.
    revisa = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Revisa', blank=True, null=True)  # Field name made lowercase.
    fecha_implementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Formatos'


class Naturalezacontrol(models.Model):
    codnaturaleza = models.AutoField(db_column='CodNaturaleza', primary_key=True)  # Field name made lowercase.
    descnaturaleza = models.CharField(db_column='DescNaturaleza', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NaturalezaControl'


class Procesos(models.Model):
    codproceso = models.AutoField(db_column='CodProceso', primary_key=True)  # Field name made lowercase.
    codtipoproceso = models.ForeignKey('Tipoproceso', models.DO_NOTHING, db_column='CodTipoProceso', blank=True, null=True)  # Field name made lowercase.
    nombreproceso = models.CharField(db_column='NombreProceso', max_length=75, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='Descripcion', blank=True, null=True)  # Field name made lowercase.
    iddue_oproceso = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='IdDue\xf1oProceso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    logo = models.BinaryField(db_column='Logo', blank=True, null=True)  # Field name made lowercase.
    estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    fecha_implementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Procesos'


class Puestos(models.Model):
    codpuesto = models.AutoField(db_column='CodPuesto', primary_key=True)  # Field name made lowercase.
    codarea = models.ForeignKey(Areas, models.DO_NOTHING, db_column='CodArea', blank=True, null=True)  # Field name made lowercase.
    descpuesto = models.CharField(db_column='DescPuesto', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Puestos'


class Raci(models.Model):
    idraci = models.AutoField(db_column='IdRaci', primary_key=True)  # Field name made lowercase.
    codactividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='CodActividad', blank=True, null=True)  # Field name made lowercase.
    codraci = models.ForeignKey('Tiporaci', models.DO_NOTHING, db_column='CodRaci', blank=True, null=True)  # Field name made lowercase.
    codpuesto = models.IntegerField(db_column='CodPuesto', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RACI'


class Riesgos(models.Model):
    codriesgo = models.AutoField(db_column='CodRiesgo', primary_key=True)  # Field name made lowercase.
    codtiporiesgo = models.ForeignKey('Tiposriesgos', models.DO_NOTHING, db_column='CodTipoRiesgo', blank=True, null=True)  # Field name made lowercase.
    descriesgo = models.CharField(db_column='DescRiesgo', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Riesgos'


class Subprocesos(models.Model):
    codsubproceso = models.AutoField(db_column='CodSubproceso', primary_key=True)  # Field name made lowercase.
    codproceso = models.ForeignKey(Procesos, models.DO_NOTHING, db_column='CodProceso', blank=True, null=True)  # Field name made lowercase.
    descsubproceso = models.TextField(db_column='DescSubProceso', blank=True, null=True)  # Field name made lowercase.
    due_osubproceso = models.ForeignKey(Puestos, models.DO_NOTHING, db_column='Due\xf1oSubProceso', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    orden_subproceso = models.IntegerField(db_column='OrdenSubproceso', blank=True, null=True)  # Field name made lowercase.
    diagrama = models.BinaryField(db_column='Diagrama', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(db_column='Observaciones', blank=True, null=True)  # Field name made lowercase.
    anexo = models.CharField(db_column='Anexo', max_length=75, blank=True, null=True)  # Field name made lowercase.
    codestado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='CodEstado', blank=True, null=True)  # Field name made lowercase.
    fecha_implementacion = models.DateTimeField(db_column='FechaImplementacion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubProcesos'


class Subprocesosxescenarios(models.Model):
    codsubprocesosxescenarios = models.AutoField(db_column='CodSubProcesosXEscenarios', primary_key=True)  # Field name made lowercase.
    codescenarioriesgo = models.ForeignKey(Escnariosriesgos, models.DO_NOTHING, db_column='CodEscenarioRiesgo', blank=True, null=True)  # Field name made lowercase.
    codsubproceso = models.ForeignKey(Subprocesos, models.DO_NOTHING, db_column='CodSubproceso', blank=True, null=True)  # Field name made lowercase.
    probabilidad = models.IntegerField(db_column='Probabilidad', blank=True, null=True)  # Field name made lowercase.
    imacto = models.IntegerField(db_column='Imacto', blank=True, null=True)  # Field name made lowercase.
    nivel_riesgo_inherente = models.IntegerField(db_column='NivelRiesgoInherente', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SubProcesosXEscenarios'


class Tipoactividad(models.Model):
    codtipoactividad = models.AutoField(db_column='CodTipoActividad', primary_key=True)  # Field name made lowercase.
    desctipoactividad = models.CharField(db_column='DescTipoActividad', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoActividad'


class Tipoareas(models.Model):
    codtipoarea = models.AutoField(db_column='CodTipoArea', primary_key=True)  # Field name made lowercase.
    desctipoarea = models.CharField(db_column='DescTipoArea', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoAreas'


class Tipocontrol(models.Model):
    codtipocontrol = models.AutoField(db_column='CodTipoControl', primary_key=True)  # Field name made lowercase.
    desctipocontrol = models.CharField(db_column='DescTipoControl', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoControl'


class Tipoproceso(models.Model):
    codtipoproceso = models.AutoField(db_column='CodTipoProceso', primary_key=True)  # Field name made lowercase.
    desctipoproceso = models.CharField(db_column='DescTipoProceso', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoProceso'


class Tiporaci(models.Model):
    codraci = models.AutoField(db_column='CodRaci', primary_key=True)  # Field name made lowercase.
    letra = models.CharField(db_column='Letra', max_length=1, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoRACI'


class Tiposriesgos(models.Model):
    codtiporiesgo = models.AutoField(db_column='CodTipoRiesgo', primary_key=True)  # Field name made lowercase.
    desctiporiesgo = models.CharField(db_column='DescTipoRiesgo', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TiposRiesgos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
