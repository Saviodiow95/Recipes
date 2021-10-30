from rest_framework import serializers

from cookbook.models import Chef


class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ('id', 'name',)
