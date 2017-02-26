from django.db import models
import random
import string

'''	
	Run these two after any changes here:
		1) python manage.py makemigrations
		2) python manage.py migrate
'''

# Create your models here.

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
	# new_code = ""
	# for _ in range(size):
	# 	new_code += random.choice(chars)
	# return new_code
	return ''.join(random.choice(chars) for _ in range(size))

class MiniURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, unique=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def save(self, *args, **kwargs):
		self.shortcode = code_generator()
		super(MiniURL, self).save(*args, *kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)
