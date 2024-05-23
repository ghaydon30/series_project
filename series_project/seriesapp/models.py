from django.db import models

"""
The Model updates the data and notifies the View of any changes (in some implementations).
"""

class TacoStandFinancialData(models.Model):
  # Stores the date for the financial data entry
  date = models.DateField()

  # Stores the daily revenue as a floating-point number
  daily_revenue = models.FloatField()

  # Stores the number of daily customers as an integer
  daily_customers = models.IntegerField()

  # Stores the number of tacos sold as an integer
  tacos_sold = models.IntegerField()

  # Stores the number of drinks sold as an integer
  drinks_sold = models.IntegerField()

  # Stores the total employee hours as a floating-point number
  total_employee_hours = models.FloatField()