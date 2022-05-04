from rest_framework.serializers import ModelSerializer
from .models import Nutricional

class NutricionalSerializer(ModelSerializer):
    class Meta:
        model = Nutricional
        fields = '__all__'