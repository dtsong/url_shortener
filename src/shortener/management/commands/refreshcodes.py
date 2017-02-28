from django.core.management.base import BaseCommand, CommandError
from shortener.models import MiniURL

class Command(BaseCommand):
	help = 'Refreshes all MiniURL shortcodes'

	def add_arguments(self, parser):
		parser.add_argument('items', type=int)

	def handle(self, *args, **options):
		return MiniURL.objects.refresh_shortcodes(items=options['items'])