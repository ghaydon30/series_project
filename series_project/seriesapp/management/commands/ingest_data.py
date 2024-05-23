import csv
from django.core.management.base import BaseCommand
from seriesapp.models import TacoStandFinancialData

class Command(BaseCommand):
    help = 'Ingests data from taco_stand_financial_data_extended.csv into the database'

    def handle(self, *args, **kwargs):
        file_path = 'data/taco_stand_financial_data_extended.csv'
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                TacoStandFinancialData.objects.create(
                    date=row['date'],
                    daily_revenue=row['daily_revenue'],
                    daily_customers=row['daily_customers'],
                    tacos_sold=row['tacos_sold'],
                    drinks_sold=row['drinks_sold'],
                    total_employee_hours=row['total_employee_hours'],
                )
        self.stdout.write(self.style.SUCCESS('Data successfully ingested!'))
