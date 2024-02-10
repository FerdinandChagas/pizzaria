from rest_framework import serializers
from menu.models import Pizza, Kalzone

class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = "__all__" # ['id', 'flavor','border','border_flavor', 'price', 'sweet']

class PizzaOnlyFlavorAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = ['flavor']

class KalzoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kalzone
        fields = ['pasta','flavor']