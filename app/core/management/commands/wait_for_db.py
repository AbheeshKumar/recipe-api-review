"""
Django command to wait for database to be available
"""

import time
from django.core.management import BaseCommand
from django.db import OperationalError
from psycopg2 import OperationalError as Psycopg2Error

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Wait for Database...")
        db_up = False

        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2Error, OperationalError):
                self.stdout.write("Database Unvailable")

        self.stdout.write(self.style.SUCCESS("Database Available"))