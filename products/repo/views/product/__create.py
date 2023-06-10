from rest_framework.generics import CreateAPIView as APIView

from products.serializers import ProductCreateModelSerializer as Serializer

from . import Base


class Create(Base, APIView):
    serializer_class = Serializer
