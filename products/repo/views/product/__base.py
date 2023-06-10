from products.models import ProductModel as Model


class Base:
    queryset = Model.objects.all()
