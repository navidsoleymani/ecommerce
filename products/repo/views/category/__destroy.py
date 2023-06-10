from rest_framework.generics import DestroyAPIView as APIView

from products.serializers import ProductCategoryDestroyModelSerializer as Serializer

from . import Base


class Destroy(Base, APIView):
    serializer_class = Serializer
