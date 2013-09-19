from django.db import models

class Company(models.Model):
	name = models.CharField(max_length = 50)

class User(models.Model):
	nickname = models.CharField(max_length=12) 
	name = models.CharField(max_length = 50)
	lastname = models.CharField(max_length = 30)
	passwd = models.CharField(max_length = 40)
	company = models.ForeignKey(Company)
	
