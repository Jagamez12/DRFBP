# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Access(models.Model):
    id_access = models.SmallAutoField(primary_key=True)
    id_user = models.SmallIntegerField()
    date = models.DateField()
    hour = models.TimeField()

    class Meta:
        managed = False
        db_table = 'access'


class IpAccess(models.Model):
    id_ip_access = models.SmallAutoField(primary_key=True)
    id_user = models.ForeignKey('Users', models.DO_NOTHING, db_column='id_user')
    id_ip = models.ForeignKey('RegisterIp', models.DO_NOTHING, db_column='id_ip')
    id_access = models.ForeignKey(Access, models.DO_NOTHING, db_column='id_access')

    class Meta:
        managed = False
        db_table = 'ip_access'


class Permissions(models.Model):
    idpermissions = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    idrol = models.ForeignKey('Roles', models.DO_NOTHING, db_column='Idrol')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permissions'


class References(models.Model):
    id_reference = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'references'


class RegisterIp(models.Model):
    id_ip = models.SmallAutoField(primary_key=True)
    ip = models.CharField(max_length=30)
    iduser = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'register_ip'


class Roles(models.Model):
    id_rol = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'roles'


class Users(models.Model):
    idusers = models.SmallAutoField(primary_key=True)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    message = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    idrol = models.ForeignKey(Roles, models.DO_NOTHING, db_column='idrol')
    idreference = models.ForeignKey(References, models.DO_NOTHING, db_column='idreference')

    class Meta:
        managed = False
        db_table = 'users'
