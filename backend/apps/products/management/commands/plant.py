from os.path import sep

from django.apps import apps
from django.core.management import BaseCommand, call_command
from tqdm import tqdm


class Command(BaseCommand):
    help = "Create plantuml diagrams"

    def handle(self, *args, **options):
        folder = "v1"
        entities = [
            "products",
            "orders",
            "common",
            "users",
        ]

        for e in entities:
            call_command(
                "generate_puml",
                "--file",
                self.get_path(file_name=e),
                "--include",
                e,
                "--add-help",
                "--add-choices",
                "--add-legend",
                "--add-omitted-headers",
            )

    def get_path(self, file_name, folder=None):
        return f"{file_name}.puml"
