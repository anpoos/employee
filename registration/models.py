from django.db import models

class Registration(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False)
	email = models.EmailField(max_length=50, blank=False, null=False)
	phone_no = models.IntegerField(blank=False, null=False)
	password = models.CharField(max_length=50, blank=False,null=False)
	created_date = models.DateField(null=False, auto_now_add=True)


	def __str__(self):
		return self.name