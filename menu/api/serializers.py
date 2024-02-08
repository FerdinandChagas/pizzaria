from rest_framework import serializers
from menu.models import Pizza, Kalzone

class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = "__all__"

class KalzoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kalzone
        fields = ['pasta','flavor']