from django.urls import path

from products.views import (
    ProductCategoryCreateAPIView as CreateAPIView,
    ProductCategoryListAPIView as ListAPIView,
    ProductCategoryRetrieveAPIView as RetrieveAPIView,
    ProductCategoryUpdateAPIView as UpdateAPIView,
    ProductCategoryDestroyAPIView as DestroyAPIView,
)

app_name = 'categories'
urlpatterns = [
    path('create', CreateAPIView.as_view(), name='create'),
    path('list', ListAPIView.as_view(), name='list'),
    path('retrieve/<int:id>', RetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:id>', UpdateAPIView.as_view(), name='update'),
    path('destroy/<int:id>', DestroyAPIView.as_view(), name='destroy'),
]
