from django.db import models

# Create your models here.

#organizers table
class Organizers(models.Model):
    o_id = models.AutoField(primary_key=True)
    o_name = models.CharField(max_length=30, blank=True, null=True)
    specialty = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizers'

#flower table 
class Flower(models.Model):
    f_id = models.AutoField(primary_key=True)
    species = models.CharField(max_length=30, blank=True, null=True)
    size = models.FloatField(blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'flower'

#User table
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=30, blank=True, null=True)
    u_address = models.CharField(max_length=30, blank=True, null=True)
    entriesno = models.IntegerField(db_column='entriesNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'

#competition table 
class Competition(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=50, blank=True, null=True)
    c_location = models.CharField(max_length=30, blank=True, null=True)
    c_date = models.DateTimeField(blank=True, null=True)
    participantsno = models.SmallIntegerField(db_column='participantsNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'competition'

#perennials table
class Perennials(models.Model):
    perennial = models.OneToOneField(Competition, models.DO_NOTHING, primary_key=True)
    perennials = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perennials'

#annuals table
class Annuals(models.Model):
    annual = models.OneToOneField('Competition', models.DO_NOTHING, primary_key=True)
    cosmos = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'annuals'




