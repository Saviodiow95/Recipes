from django.urls import path

from .views.chef import CreateChef, DetailChef, ListChef
from .views.recipes import CreateRecipe, DetailRecipe, SearchRecipes

urlpatterns = [
    path('chef', CreateChef.as_view(), name='create-chef'),
    path('chef/<int:pk>', DetailChef.as_view(), name='detail-chef'),
    path('chef/list', ListChef.as_view(), name='list-chef'),
    path('recipe', CreateRecipe.as_view(), name='create-recipe'),
    path('recipe/<int:pk>', DetailRecipe.as_view(), name='detail-recipe'),
    path('recipe/search', SearchRecipes.as_view(), name='search-Recipe'),
]
