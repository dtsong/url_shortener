from django.conf.urls import url
from django.contrib import admin

from shortener.views import HomeView, MiniCBVView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^S', HomeView.as_view()),
    url(r'^b/(?P<shortcode>[\w-]+){6,15}/$', MiniCBVView.as_view()),
]
