from django.contrib import admin

# Register your models here.
from .models import *
class ManagerModelAdmin(admin.ModelAdmin):
	list_display=["manager_id","name","password","image"]
	list_display_links=["manager_id"]
	list_filter=["manager_id","name"]
	list_editable=["name"]
	search_fields=["manager_id","name"]
	class Meta:
		model=Manager

admin.site.register(Manager,ManagerModelAdmin)

class EmployeeModelAdmin(admin.ModelAdmin):
	list_display=["employee_id","name","managed_by","phone_number","address","email","image","phone_model","imei"]
	list_display_links=["employee_id"]
	list_filter=["employee_id","name"]
	list_editable=["name","phone_number","phone_model","address","email","imei"]
	search_fields=["employee_id","name"]
	class Meta:
		model=Employee

admin.site.register(Employee,EmployeeModelAdmin)

class DeviceModelAdmin(admin.ModelAdmin):
	list_display=["owner","activity","battery","latitude","longitude","timestamp","current_location"]
	list_display_links=["owner"]
	list_filter=["owner","current_location"]
	search_fields=["owner","current_location"]
	class Meta:
		model=Device

admin.site.register(Device,DeviceModelAdmin)
