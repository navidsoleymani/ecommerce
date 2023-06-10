from rest_framework.generics import UpdateAPIView as APIView

from products.serializers import ProductUpdateModelSerializer as Serializer

from . import Base


class Update(Base, APIView):
    serializer_class = Serializer
