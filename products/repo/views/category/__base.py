from products.models import ProductCategoryModel as Model


class Base:
    queryset = Model.objects.all()
