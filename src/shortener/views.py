from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import MiniURL

def mini_redirect_view(request, shortcode=None, *args, **kwargs): #FBV
	obj = get_object_or_404(MiniURL, shortcode=shortcode)
	return HttpResponse("hello {sc}".format(sc=obj.url))


class MiniCBVView(View): #CBV
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(MiniURL, shortcode=shortcode)
		return HttpResponse("hello again {sc}".format(sc=obj.shortcode))

