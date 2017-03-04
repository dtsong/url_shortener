from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import MiniURL
from .forms import SubmitUrlForm


def home_view_fbv(request, *args, **kwargs):
	if request.method == "POST":
		print(request.POST)
	return render(request, "shortener/home.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title": "miniurl.co",
			"form": the_form
		}

		return render(request, "shortener/home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)

		context = {
			"title": "miniurl.co",
			"form": form
		}

		return render(request, "shortener/home.html", context)


class MiniCBVView(View): #CBV
	def get(self, request, shortcode=None, *args, **kwargs):
		obj = get_object_or_404(MiniURL, shortcode=shortcode)
		return HttpResponseRedirect(obj.url)
