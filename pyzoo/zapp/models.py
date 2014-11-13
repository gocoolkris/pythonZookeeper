from django.db import models

# Create your models here.

class ZooKeeperInstance(models.Model):
	name = models.CharField(max_length=512)
      	value= models.CharField(max_length=512)



	def __str__(self): return self.name
