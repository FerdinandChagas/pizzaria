from rest_framework import serializers
from menu.models import Pizza

class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = "__all__"