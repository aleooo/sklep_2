from django.test import TestCase
from django.urls import reverse



class OrderFormTests(TestCase):
    def setUp(self):
        self.data = {'first_name': ['alek.san=der'],
         'last_name': ['wiedenski'],
          'email': ['aleksanderwiedenskiail.com'],
           'phone_number_0': ['+48'], 'phone_number_1': ['5108657dw04'],
            'street': ['krótka'],
             'street_number': ['3'],
              'town': ['seroczyn'],
               'ZIP_code': ['08-116'],
                'country': ['poland']}

    def test_placeholder(self):
        response = self.client.get(reverse('order:order'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'first_name')
    
    def test_uppercase(self):
        response = self.client.post(reverse('order:order'), data=self.data)

        self.assertContains(response, 'First Name should start with an uppercase letter')
        self.assertContains(response, 'Last Name should start with an uppercase letter')
        self.assertContains(response, 'Town should start with an uppercase letter')
        self.assertContains(response, 'Street should start with an uppercase letter')
        self.assertContains(response, 'Country should start with an uppercase letter')
    
    def test_punctuation(self):
        response = self.client.post(reverse('order:order'), data=self.data)

        self.assertContains(response, "contain punctuation")
    
    def test_email(self):
        response = self.client.post(reverse('order:order'), data=self.data)

        self.assertContains(response, 'Enter a valid email address.')
        
