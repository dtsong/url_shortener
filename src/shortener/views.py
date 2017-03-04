from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import MiniURL


def home_view_fbv(request, *args, **kwargs):
	if request.method == "POST":
		print(request.POST)
	return render(request, "shortener/home.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "shortener/home.html", {})

	def post(self, request, *args, **kwargs):
		return render(request, "shortener/home.html", {})


class MiniCBVView(View): #CBV
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(MiniURL, shortcode=shortcode)
		return HttpResponseRedirect(obj.url)
