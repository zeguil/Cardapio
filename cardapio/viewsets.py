from rest_framework import status, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from cardapio.models import Cardapio
from .serializers import CardapioSerializer, CardapioNutriSerializer
from django.shortcuts import get_object_or_404

class CardapioViewSet(viewsets.ModelViewSet):
 
    serializer_class = CardapioSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('nome', 'valor')
    # lookup_field = 'id'

    def get_queryset(self):
        # id = self.request.query_params.get('id', None)
        # nome = self.request.query_params.get('nome', None)
        # valor = self.request.query_params.get('valor', None)
        queryset = Cardapio.objects.all()
        # if id:
        #     queryset = Cardapio.objects.filter(pk=id)
        # if nome:
        #     queryset = queryset.filter(nome__iexact=nome)
        # if valor:
        #     queryset = queryset.filter(valor__iexact=valor)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(CardapioViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(CardapioViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(CardapioViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        prato = get_object_or_404(queryset, id=pk)
        serializer = CardapioNutriSerializer(prato)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        return super(CardapioViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(CardapioViewSet, self).partial_update(request, *args, **kwargs)
