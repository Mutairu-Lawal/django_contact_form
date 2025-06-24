from django.core.management.base import BaseCommand
from users.models import Users
from users.utils import get_counts, get_name


class Command(BaseCommand):
    def handle(self, *args, **options):
        get_name('Mt law')
        get_counts(5)
