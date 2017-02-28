from django.core.management.base import BaseCommand, CommandError
from shortener.models import MiniURL

class Command(BaseCommand):
	help = 'Refreshes all MiniURL shortcodes'

	def handle(self, *args, **options):
		return MiniURL.objects.refresh_shortcodes()