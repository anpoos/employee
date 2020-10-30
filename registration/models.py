from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

class Registration(AbstractBaseUser):
	name = models.CharField(max_length=50, blank=False, null=False)
	email = models.EmailField(max_length=50, unique=True, blank=False, null=False)
	phone_no = models.CharField(max_length=12, blank=False, null=False)
	created_date = models.DateField(null=False, auto_now_add=True)
	EMAIL_FIELD = 'email'
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['phone_no']


	def __str__(self):
		return self.name