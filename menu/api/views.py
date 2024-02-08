from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from menu.api.serializers import PizzaSerializer, Pizza, KalzoneSerializer, Kalzone

# Classes que herdam de ModelViewSet já implementam o CRUD
class PizzaViewSet(ModelViewSet):
    # http://localhost:8000/api/pizzas/
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    permission_classes = [ AllowAny ]

    # Quando quiser adicionar uma nova funcionalidade use @action
    # http://localhost:8000/api/pizzas/search/
    @action(methods=['get'], url_path='search', detail=False)
    def search(self, request):
        pizzas = Pizza.objects.filter(border=False) #Consulta
        serializer = PizzaSerializer(pizzas, many=True) #O resultado sendo convertido com serializer
        return Response(
            {"info":"Pizzas encontradas", "data":serializer.data}, #Enviando o serializer como resposta
            status=status.HTTP_200_OK) #Definido o código HTTP da resposta.

class KalzoneViewSet(ModelViewSet):
    serializer_class = KalzoneSerializer
    queryset = Kalzone.objects.all()