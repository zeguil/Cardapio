from rest_framework.viewsets import ModelViewSet
from .models import Nutricional
from .serializers import NutricionalSerializer

class NutricionalViewSet(ModelViewSet):
    queryset = Nutricional.objects.all()
    serializer_class = NutricionalSerializer