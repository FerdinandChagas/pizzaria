from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from menu.api.serializers import PizzaSerializer, Pizza

class PizzaViewSet(ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    permission_classes = [ AllowAny ]

    @action(methods=['get'], url_path='search', detail=False)
    def search(self, request):
        pizzas = Pizza.objects.filter(border=False)
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(
            {"info":"Pizzas encontradas", "data":serializer.data}, 
            status=status.HTTP_200_OK)
