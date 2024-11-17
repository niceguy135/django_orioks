# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Employments(models.Model):
    structural_unit = models.OneToOneField('StructuralUnits', models.DO_NOTHING, primary_key=True)  # The composite primary key (structural_unit_id, professor_id) found, that is not supported. The first column is selected.
    professor = models.ForeignKey('Professors', models.DO_NOTHING)
    contract_number = models.IntegerField()
    wage_rate = models.DecimalField(max_digits=3, decimal_places=2)

    class Meta:
         
        db_table = 'employments'
        unique_together = (('structural_unit', 'professor'),)


class FieldComprehensions(models.Model):
    student = models.OneToOneField('Students', models.DO_NOTHING, primary_key=True)  # The composite primary key (student_id, field) found, that is not supported. The first column is selected.
    field = models.ForeignKey('Fields', models.DO_NOTHING, db_column='field')
    mark = models.IntegerField(blank=True, null=True)

    class Meta:
         
        db_table = 'field_comprehensions'
        unique_together = (('student', 'field'),)


class Fields(models.Model):
    field_id = models.UUIDField(primary_key=True)
    field_name = models.CharField(max_length=100)
    structural_unit = models.ForeignKey('StructuralUnits', models.DO_NOTHING)
    professor = models.ForeignKey('Professors', models.DO_NOTHING)
    zet = models.IntegerField()
    semester = models.IntegerField()

    class Meta:
         
        db_table = 'fields'


class Professors(models.Model):
    professor_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    degree = models.CharField(max_length=15, blank=True, null=True)
    academic_title = models.CharField(max_length=40, blank=True, null=True)
    current_position = models.CharField(max_length=40)
    experience = models.IntegerField()
    salary = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
         
        db_table = 'professors'


class StructuralUnits(models.Model):
    structural_unit_id = models.AutoField(primary_key=True)
    full_title = models.TextField()
    abbreviated_title = models.CharField(max_length=20, blank=True, null=True)
    head_of_the_unit = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
         
        db_table = 'structural_units'


class StudentIds(models.Model):
    student = models.OneToOneField('Students', models.DO_NOTHING, primary_key=True)
    issue_date = models.DateField()
    expiration_date = models.DateField()

    class Meta:
         
        db_table = 'student_ids'


class Students(models.Model):
    student_id = models.IntegerField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    students_group_number = models.ForeignKey('StudentsGroups', models.DO_NOTHING, db_column='students_group_number')
    birthday = models.DateField()
    email = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
         
        db_table = 'students'


class StudentsGroups(models.Model):
    students_group_number = models.CharField(primary_key=True, max_length=7)
    enrolment_status = models.CharField(max_length=12)
    structural_unit = models.ForeignKey(StructuralUnits, models.DO_NOTHING)

    class Meta:
         
        db_table = 'students_groups'
