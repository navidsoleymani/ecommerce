from rest_framework.generics import RetrieveAPIView as APIView

from products.serializers import ProductRetrieveModelSerializer as Serializer

from . import Base


class Retrieve(Base, APIView):
    serializer_class = Serializer
