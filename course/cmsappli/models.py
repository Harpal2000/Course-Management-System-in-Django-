from django.db import models

# Create your models here.


class Admin(models.Model):
    admin_name = models.CharField(max_length=20,primary_key=True)
    admin_pass = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        db_table='admin'

class StreamPannel(models.Model):   #not in use
    id_number = models.FloatField(primary_key=True)
    Stream_name = models.CharField(max_length=30, blank=True, null=True)
    class Meta:
        db_table='streampannel'


class UserDetails(models.Model):
    user_name = models.CharField(primary_key=True, max_length=30)
    user_email = models.CharField(max_length=35, blank=True, null=True)
    user_psswd = models.CharField(max_length=30, blank=True, null=True)
    class Meta:
        db_table='userdetails'


class CourseDetails(models.Model):
    c_id = models.CharField(primary_key=True, max_length=30)
    c_name= models.CharField(max_length=35, blank=True, null=True)
    s_name = models.CharField(max_length=30, blank=True, null=True)
    class Meta:
        db_table='add_c'

class StreamDetails(models.Model):
    s_id = models.CharField(primary_key=True, max_length=30)
    s_name = models.CharField(max_length=30, blank=True, null=True)
    class Meta:
        db_table='add_s'
