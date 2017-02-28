from django.db import models
from django.conf import settings

from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class MiniURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs_main = super(MiniURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self, items=None):
		qs = MiniURL.objects.filter(id__gte=1)
		if items != None and isinstance(items, int):
			# reverses the query set based on ids
			qs = qs.order_by('-id')[:items]

		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.id)
			q.save
			new_codes += 1
		return "New Codes made: {i}".format(i=new_codes)

class MiniURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	objects = MiniURLManager() # This hooks into the MiniURLManager's method
	
	# class Meta:
	# 	ordering = 'id'

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(MiniURL, self).save(*args, *kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)
