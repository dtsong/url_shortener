from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

def mini_redirect_view(request, *args, **kwargs): #FBV
	return HttpResponse("hello")


class MiniCBVView(View): #CBV
	def get(self, request, *args, **kwargs):
		return HttpResponse("hello again")