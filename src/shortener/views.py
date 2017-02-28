from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def mini_redirect_view(request, *args, **kwargs):
	return HttpResponse("hello")

class MiniRedirectView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("hello again")