from rest_framework.generics import ListAPIView as APIView

from products.serializers import ProductCategoryListModelSerializer as Serializer

from . import Base


class List(Base, APIView):
    serializer_class = Serializer
