from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import TacoStandFinancialData
from django.contrib.auth.models import User

# Test case for TacoStandFinancialData
class TacoStandFinancialDataTests(TestCase):
    def setUp(self):
        # Set up the test client and create a user
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Log in with new test user
        self.client.login(username='testuser', password='testpass')
        # Data object for testing
        self.taco_data = TacoStandFinancialData.objects.create(
            date='2023-01-01',
            daily_revenue=1000.0,
            daily_customers=150,
            tacos_sold=200,
            drinks_sold=100,
            total_employee_hours=20
        )

    # Test retrieving the list of financial data
    def test_get_financial_data_list(self):
        response = self.client.get(reverse('tacostandfinancialdata-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_records', response.data['results'][0])
        self.assertEqual(response.data['results'][0]['total_records'], 1)

    # Test creating a new financial data entry
    def test_create_financial_data(self):
        data = {
            'date': '2023-01-02',
            'daily_revenue': 1200.0,
            'daily_customers': 180,
            'tacos_sold': 250,
            'drinks_sold': 120,
            'total_employee_hours': 25
        }
        response = self.client.post(reverse('tacostandfinancialdata-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TacoStandFinancialData.objects.count(), 2)

    # Test updating an existing financial data entry
    def test_update_financial_data(self):
        data = {
            'date': '2023-01-01',
            'daily_revenue': 1100.0,
            'daily_customers': 160,
            'tacos_sold': 210,
            'drinks_sold': 110,
            'total_employee_hours': 21
        }
        response = self.client.put(reverse('tacostandfinancialdata-detail', args=[self.taco_data.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.taco_data.refresh_from_db()
        self.assertEqual(self.taco_data.daily_revenue, 1100.0)
        self.assertEqual(self.taco_data.daily_customers, 160)

    # Test deleting an existing financial data entry
    def test_delete_financial_data(self):
        response = self.client.delete(reverse('tacostandfinancialdata-detail', args=[self.taco_data.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TacoStandFinancialData.objects.count(), 0)

    # Test handling invalid data submission
    def test_invalid_data(self):
        data = {
            'daily_revenue': 1200.0,
            'daily_customers': 180,
            'tacos_sold': 250,
            'drinks_sold': 120,
            'total_employee_hours': 25
        }
        response = self.client.post(reverse('tacostandfinancialdata-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error']['status_code'], 400)