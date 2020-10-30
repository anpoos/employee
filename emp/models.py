from django.db import models
import datetime

DESIGNATION = (
				(1,'Manager'),(2,'Asst.Manager'),
				(3,'HR'),(4,'Sr.Developer'),
				(5,'Jr.Developer'),(6,'Hardware Engg'),
				(7,'Content writer'),(8,'cooridinator'),
				(9,'Store Keeper'),(10,'Assistant'),
				)
class Employee(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False)
	email = models.EmailField(max_length=50, blank=False, null=False)
	dob = models.DateField(null=False)
	salary = models.IntegerField(max_length=10, blank=True, null=True)
	position = models.IntegerField(choices=DESIGNATION)
	address = models.CharField(max_length=500, blank=True, null=True)
	is_active = models.BooleanField(default=1)
	is_deleted = models.BooleanField(default=0)
	created_date = models.DateField(null=False, auto_now_add=True)
	updated_date = models.DateField(null=True)

	def __str__(self):
		return self.name

	def age(self):
		age = (datetime.datetime.now().date() - self.dob).days//365
		return age