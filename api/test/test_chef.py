import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from api.serializers.serializer_chef import ChefSerializer
from cookbook.models import Chef


class ChefTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.chef_alex = Chef.objects.create(name="Alex Atala")
        self.chef_helena = Chef.objects.create(name="Helena Rizzo")

    def test_create(self):
        """
        Testing creation of a Chef with valid and invalid data, using the view CreateChef
        """
        chef_valid = {
            'name': 'Sávio Moreira'
        }
        chef_invalid = {
            'name': ''
        }

        response_valid = self.client.post(
            reverse('create-chef'),
            data=json.dumps(chef_valid),
            content_type='application/json'
        )
        response_invalid = self.client.post(
            reverse('create-chef'),
            data=json.dumps(chef_invalid),
            content_type='application/json'
        )

        self.assertEqual(response_valid.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_invalid.status_code, status.HTTP_400_BAD_REQUEST)

    def test_detail_get(self):
        """
        Testing the method get in view DetailChef
        """
        chef = Chef.objects.get(pk=1)
        chef_serializer = ChefSerializer(chef, many=False)

        response = self.client.get(reverse('detail-chef', kwargs={'pk': 1}))
        self.assertEqual(response.data, chef_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_delete(self):
        """
        Testing the method delete in view DetailChef
        """
        response = self.client.delete(reverse('detail-chef', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_detail_put(self):
        """
        Testing the method put in view DetailChef
        """
        chef_json = {
            'name': "Pablo"
        }
        response = self.client.put(
            reverse('detail-chef', kwargs={'pk': 1}),
            data=json.dumps(chef_json),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list(self):
        """
        Testing the return da view  ListChef
        """
        chef_list = Chef.objects.all()
        chef_serializer = ChefSerializer(chef_list, many=True)
        response = self.client.get(reverse('list-chef'))
        self.assertEqual(response.data, chef_serializer.data)
