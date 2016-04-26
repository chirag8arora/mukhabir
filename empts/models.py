from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from datetime import datetime
def upload_location(instance,filename):
	return "%s/%s" % (instance,filename)

class Manager(models.Model):
	manager_id=models.CharField(max_length=120,primary_key=True)
	name=models.CharField(max_length=120)
	password=models.CharField(max_length=120)
	image=models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	class Meta:
		db_table='empts_manager'
	def __str__(self):
		return self.name
	def __str__(self):
		return self.manager_id


class Employee(models.Model):
	employee_id=models.CharField(max_length=120,primary_key=True)
	managed_by=models.ForeignKey(Manager)
	name=models.CharField(max_length=120)
	phone_number=models.IntegerField()
	address=models.CharField(max_length=200)
	image=models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
	height_field=models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	email=models.EmailField(max_length=30)
	phone_model=models.CharField(max_length=120)
	imei=models.IntegerField()
	class Meta:
		db_table='empts_employee'
	def __str__(self):
		return self.name
	def __str__(self):
		return self.employee_id
	def __str__(self):
		return self.managed_by
	def __str__(self):
		return self.address
	def __str__(self):
		return self.email
	def __str__(self):
		return self.phone_model

class Device(models.Model):
	owner=models.ForeignKey(Employee)
	activity=models.CharField(max_length=120)
	battery=models.IntegerField()
	latitude=models.DecimalField(max_digits=9, decimal_places=6)
	longitude=models.DecimalField(max_digits=9, decimal_places=6)
	timestamp=models.DateTimeField(default=datetime.now)
	current_location=models.CharField(max_length=120)
	class Meta:
		db_table='empts_device'
	def __str__(self):
		return self.activity
	def __str__(self):
		return self.current_location
	