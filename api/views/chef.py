from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from api.serializers.serializer_chef import ChefSerializer
from cookbook.models import Chef


class CreateChef(CreateAPIView):
    """
    View to create a Chef
    """

    model = Chef
    serializer_class = ChefSerializer


class DetailChef(RetrieveUpdateDestroyAPIView):
    """
    View to show details, update and delete a chef
    """
    
    serializer_class = ChefSerializer
    queryset = Chef


class ListChef(ListAPIView):
    """
    View to list all Chef
    """

    serializer_class = ChefSerializer
    queryset = Chef.objects.all()

