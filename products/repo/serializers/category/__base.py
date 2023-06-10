from rest_framework.serializers import ModelSerializer

from products.models import ProductCategoryModel as Model


class Base(ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'
