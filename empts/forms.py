from django import forms
import re
# from django.contrib.auth.models import User
from .models import *
class ManagerForm(forms.ModelForm):
		model=Manager
		fields=[
			"manager_id",
			"name",
			"password",
			"image",

		]
		widgets={
		'manager_id':forms.TextInput(),
		'name':forms.TextInput(),
		'password':forms.PasswordInput(attrs=dict(max_length=120, render_value=False)),
		}
class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields=[
			"employee_id",
			"name",
			"phone_number",
			"address",
			"image",
			"email",
			"phone_model",
			"imei",

		]
		widgets={
		'employee_id':forms.TextInput(),
		'name':forms.TextInput(),
		'address':forms.TextInput(),
		'phone_model':forms.TextInput(),
		}

class DeviceForm(forms.ModelForm):
	class Meta:
		model=Device
		fields=[
			"owner",
			"activity",
			"battery",
			"latitude",
			"longitude",
			"timestamp",
			"current_location",

		]
		widgets={
		'activity':forms.TextInput(),
		'current_location':forms.TextInput(),

		}
