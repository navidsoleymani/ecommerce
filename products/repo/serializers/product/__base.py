from rest_framework.serializers import ModelSerializer

from products.models import ProductModel as Model


class Base(ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'
