from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from account.models import User

from .models import Customer, CustomerPayment


class CustomerTest(APITestCase):
    
    def setUp(self) -> None:
        # | Create user for authentication |
        self.auth_user_dict = {
            'first_name': 'Osayi',
            'last_name': 'Akoko',
            'email': 'test@email.com',
            'password': 'password123',
        }
        User.objects.create_user(**self.auth_user_dict)

        # | Create customer for testing |
        self.setup_customer_dict = {
            'name': 'Foo Bar',
            'email': 'FooBar@email.com',
            'phone': '08103012345',
            'address': '5 Brown street',
            'city': 'Test city',
            'state': 'Edo',
        }
        self.setup_customer = Customer.objects.create(**self.setup_customer_dict)
        
        return super().setUp()

    def test_create_customer(self):
        """
        Test creating a customer
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )

        customer_data = {
            'name': 'Osayi Akoko',
            'email': 'test@email.com',
            'phone': '08103002244',
            'address': 'No. 1, Test Street',
            'city': 'Ikeja',
            'state': 'Lagos',
        }

        url = reverse('customer:v1:customer-list')
        response = self.client.post(url, customer_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fetch_customers(self):
        """
        Test fetching all customers
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )
        url = reverse('customer:v1:customer-list')
        response = self.client.get(url)

        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetch_customer(self):
        """
        Test fetching a customer
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )

        url = reverse('customer:v1:customer-detail', kwargs={'pk':self.setup_customer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_customer(self):
        """
        Test updating a customer
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )

        req_data = {
            'name': 'John Doe',
            'email': 'JohnD@gmail.com',
        }

        url = reverse('customer:v1:customer-detail', kwargs={'pk':self.setup_customer.id})
        response = self.client.patch(url, req_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], req_data['name'])
        self.assertEqual(response.data['email'], req_data['email'])
    
    def test_delete_customer(self):
        """
        Test deleting a customer
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )

        url = reverse('customer:v1:customer-detail', kwargs={'pk':self.setup_customer.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.filter(id=self.setup_customer.id).exists(), False)


class PaymentTest(APITestCase):
    
    def setUp(self) -> None:
        # | Create user for authentication |
        self.auth_user_dict = {
            'first_name': 'Osayi',
            'last_name': 'Akoko',
            'email': 'test@email.com',
            'password': 'password123',
        }
        User.objects.create_user(**self.auth_user_dict)

        # | Create customer 1 for testing |
        self.customer1_dict = {
            'name': 'Foo Bar',
            'email': 'FooBar@email.com',
            'phone': '08103012345',
            'address': '5 Brown street',
            'city': 'Test city',
            'state': 'Edo',
        }
        self.customer1 = Customer.objects.create(**self.customer1_dict)

        # | Create customer1 payment for testing |
        self.payment1_dict = {
            'customer_id': self.customer1.id,
            'amount': '500000.00',
            'payment_type': 'cash',
            'ref_code': 'ICE-77332',
            'description': '2KVA inverter installation',
        }
        self.payment1 = CustomerPayment.objects.create(**self.payment1_dict)

        # | Create customer 2 for testing |
        self.customer2_dict = {
            'name': 'Osayi Akoko',
            'email': 'test@email.com',
            'phone': '08103002244',
            'address': 'No. 1, Test Street',
            'city': 'Ikeja',
            'state': 'Lagos',
        }
        self.customer2 = Customer.objects.create(**self.customer2_dict)

        # | Create customer2 payment for testing |
        self.payment2_dict = {
            'customer_id': self.customer2.id,
            'amount': '800000.00',
            'payment_type': 'bank deposit',
            'ref_code': 'ICE-88776',
            'description': '5KVA inverter installation',
        }
        self.payment2 = CustomerPayment.objects.create(**self.payment2_dict)
        
        return super().setUp()

    def test_create_payment(self):
        """
        Test creating a payment
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )

        payment_data = {
            'customer': self.customer2.id,
            'amount': '300000.00',
            'payment_type': 'bank deposit',
            'ref_code': 'ICE-88776',
            'description': 'Inverter battery wet cell 12V',
        }

        url = reverse('customer:v1:customerpayment-list')
        response = self.client.post(url, payment_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fetch_payments(self):
        """
        Test fetching all payments
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )
        url = reverse('customer:v1:customerpayment-list')
        response = self.client.get(url)

        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetch_customer_payments(self):
        """
        Test fetching all payments for a customer
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )
        url = reverse('customer:v1:customerpayment-list')
        response = self.client.get(url, {'customer_id': self.customer2.id})
        

        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fetch_payment(self):
        """
        Test fetching a payment
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )

        url = reverse('customer:v1:customerpayment-detail', kwargs={'pk':self.payment1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_payment(self):
        """
        Test updating a payment
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )

        req_data = {
            'payment_type': 'credit card',
            'amount': '550000.00',
        }

        url = reverse('customer:v1:customerpayment-detail', kwargs={'pk':self.payment1.id})
        response = self.client.patch(url, req_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['payment_type'], req_data['payment_type'])
        self.assertEqual(response.data['amount'], req_data['amount'])
    
    def test_delete_payment(self):
        """
        Test deleting a payment
        """
        self.client.login(
            username=self.auth_user_dict['email'], 
            password=self.auth_user_dict['password']
        )

        url = reverse('customer:v1:customerpayment-detail', kwargs={'pk':self.payment1.id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomerPayment.objects.filter(id=self.payment1.id).exists(), False)
