from django.db import models

'''	
	Run these two after any changes here:
		1) python manage.py makemigrations
		2) python manage.py migrate
'''

# Create your models here.

class MiniURL(models.Model):
	url = models.CharField(max_length=220, )

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)
