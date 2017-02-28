from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def mini_redirect_view(request, shortcode=None, *args, **kwargs): #FBV
	return HttpResponse("hello {sc}".format(sc=shortcode))


class MiniCBVView(View): #CBV
	def get(self, request, shortcode=None, *args, **kwargs):
		return HttpResponse("hello again {sc}".format(sc=shortcode))