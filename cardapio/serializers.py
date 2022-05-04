from rest_framework import serializers
from .models import Cardapio
from nutricional.serializers import NutricionalSerializer

class CardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardapio
        write_only_fields = ('nutricional', )
        fields = ['id', 'nome', 'valor', 'detalhes', 'nutricional']
        
class CardapioNutriSerializer(serializers.ModelSerializer):
    nutricional  = NutricionalSerializer()
    class Meta:
        model = Cardapio
        fields = ['id', 'nome', 'valor', 'detalhes', 'nutricional']