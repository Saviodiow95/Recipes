from rest_framework import serializers

from cookbook.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'chef', 'description', 'ingredients', 'time', 'difficulty', 'method', 'portions',)
