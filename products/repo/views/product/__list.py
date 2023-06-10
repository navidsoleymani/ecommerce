from rest_framework.generics import ListAPIView as APIView

from products.serializers import ProductListModelSerializer as Serializer

from . import Base


class List(Base, APIView):
    serializer_class = Serializer
