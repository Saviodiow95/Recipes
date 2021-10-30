from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from api.serializers.serializer_recipe import RecipeSerializer
from cookbook.models import Recipe


class CreateRecipe(CreateAPIView):
    """
    View to create a Recipe
    """

    model = Recipe
    serializer_class = RecipeSerializer


class DetailRecipe(RetrieveUpdateDestroyAPIView):
    """
    View to show details, update and delete a Recipe
    """

    serializer_class = RecipeSerializer
    queryset = Recipe


class SearchRecipes(ListAPIView):
    """
        View to search Recipes
    """

    serializer_class = RecipeSerializer

    def get_queryset(self):
        """
        Overriding get_queryset method, filtering according to get parameters
        :param: name, chef, difficulty, time, portions
        :return: queryset
        """

        params = self.request.query_params

        queryset = Recipe.objects.all()

        if params.get('name'):
            queryset = queryset.filter(name__icontains=params.get('name'))
        if params.get('chef'):
            queryset = queryset.filter(chef__id=params.get('chef'))
        if params.get('difficulty'):
            queryset = queryset.filter(difficulty=params.get('difficulty'))
        if params.get('time'):
            queryset = queryset.filter(time__lte=params.get('time'))
        if params.get('portions'):
            queryset = queryset.filter(portions=params.get('portions'))

        return queryset
