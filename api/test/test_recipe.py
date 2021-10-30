import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from api.serializers.serializer_recipe import RecipeSerializer
from cookbook.models import Chef, Recipe


class ChefTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.chef_alex = Chef.objects.create(name="Alex Atala")
        self.chef_helena = Chef.objects.create(name="Helena Rizzo")

        self.recipe_empadao = Recipe.objects.create(
            name="Empadão",
            chef=self.chef_alex,
            description="Como fazer empadão de frango: simples e fácil, receita é incrementada com ...",
            ingredients="Ingredientes - Massa 400 gramas de farinha de trigo 200 gramas de manteiga...",
            time=100,
            difficulty="3",
            method="Modo de Preparo - Recheio 1. Cozinhe o peito de frango, desfie e reserve 2. ...",
            portions=12
        )
        self.recipe_sobrecoxa = Recipe.objects.create(
            name="Sobrecoxa assada com manteiga temperada",
            chef=self.chef_alex,
            description="Receita de sobrecoxa assada com manteiga temperada é acompanhada de maionese de batatas;",
            ingredients="Ingredientes - Frango com manteiga temperada\r\n1 quilo ou 6 unidades de sobrecoxas de ...",
            time=360,
            difficulty="1",
            method="Modo de Preparo - Frango com manteiga temperada\r\n1. Numa tigela, misture 50 gramas de ...",
            portions=1
        )
        self.recipe_empadao = Recipe.objects.create(
            name="ARROZ DE BRÓCOLIS",
            chef=self.chef_helena,
            description="",
            ingredients="500 g de arroz refogado em alho cozido 100 g de alho 3 colheres de azeite",
            time=60,
            difficulty="2",
            method="Limpe o brócolis descascando os talos (retirando a pele com a faca).",
            portions=6
        )

    def test_create(self):
        """
        Testing creation of a Recipe with valid and invalid data, using the view CreateRecipe
        """
        chef_valid = {
            "name": "Esfirra de frango",
            "chef": 2,
            "description": "",
            "ingredients": "1 colher (sopa) bem cheia de fermento para pão (eu usei fermento granulado ...",
            "time": 90,
            "difficulty": "2",
            "method": "Em ma tigela grande e larga colocar o fermento em pó, o açúcar e despejar a água morna ...",
            "portions": 30
        }
        recipe_invalid = {
            "name": "",
            "chef": 1,
            "description": "",
            "ingredients": "Ingredientes - Massa",
            "time": 30,
            "difficulty": "2",
            "method": "",
            "portions": 6
        }

        response_valid = self.client.post(
            reverse('create-recipe'),
            data=json.dumps(chef_valid),
            content_type='application/json'
        )
        response_invalid = self.client.post(
            reverse('create-recipe'),
            data=json.dumps(recipe_invalid),
            content_type='application/json'
        )

        self.assertEqual(response_valid.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_invalid.status_code, status.HTTP_400_BAD_REQUEST)

    def test_detail_get(self):
        """
        Testing the method get in view DetailRecipe
        """
        recipe = Recipe.objects.get(pk=1)
        recipe_serializer = RecipeSerializer(recipe, many=False)

        response = self.client.get(reverse('detail-recipe', kwargs={'pk': 1}))
        self.assertEqual(response.data, recipe_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_delete(self):
        """
        Testing the method delete in view DetailRecipe
        """
        response = self.client.delete(reverse('detail-recipe', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_detail_put(self):
        """
        Testing the method put in view DetailRecipe
        """
        recipe_json = {
            'name': "Empadão de frango",
            "chef": 2,
            "description": "",
            "ingredients": "1 colher (sopa) bem cheia de fermento para pão (eu usei fermento granulado ...",
            "time": 90,
            "difficulty": "2",
            "method": "Em ma tigela grande e larga colocar o fermento em pó, o açúcar e despejar a água morna ...",
            "portions": 30
        }
        response = self.client.put(
            reverse('detail-recipe', kwargs={'pk': 1}),
            data=json.dumps(recipe_json),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search(self):
        """
        Testing the return da view  SearchRecipe
        """
        recipe_list = Recipe.objects.all()
        recipe_serializer = RecipeSerializer(recipe_list, many=True)
        response = self.client.get(reverse('search-Recipe'))
        self.assertEqual(response.data, recipe_serializer.data)

    def test_search_name(self):
        """
        Testing the return da view  SearchRecipe using param name
        """
        recipe_list = Recipe.objects.filter(name__icontains='frango')
        recipe_serializer = RecipeSerializer(recipe_list, many=True)
        response = self.client.get(reverse('search-Recipe'), {'name': 'frango'})
        self.assertEqual(response.data, recipe_serializer.data)

    def test_search_chef(self):
        """
        Testing the return da view  SearchRecipe using param chef
        """
        recipe_list = Recipe.objects.filter(chef_id='1')
        recipe_serializer = RecipeSerializer(recipe_list, many=True)
        response = self.client.get(reverse('search-Recipe'), {'chef': 1})
        self.assertEqual(response.data, recipe_serializer.data)

    def test_search_name_time(self):
        """
        Testing the return da view  SearchRecipe using params name and time
        """
        recipe_list = Recipe.objects.filter(name__icontains='frango', time__lte=200)
        recipe_serializer = RecipeSerializer(recipe_list, many=True)
        response = self.client.get(reverse('search-Recipe'), {'name': 'frango', 'time': 200})
        self.assertEqual(response.data, recipe_serializer.data)
