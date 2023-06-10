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
    path('', CreateAPIView.as_view(), name='create'),
    path('', ListAPIView.as_view(), name='list'),
    path('<int:id>', RetrieveAPIView.as_view(), name='retrieve'),
    path('<int:id>', UpdateAPIView.as_view(), name='update'),
    path('<int:id>', DestroyAPIView.as_view(), name='destroy'),
]
