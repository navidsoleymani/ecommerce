from django.urls import path

from products.views import (
    ProductCreateAPIView as CreateAPIView,
    ProductListAPIView as ListAPIView,
    ProductRetrieveAPIView as RetrieveAPIView,
    ProductUpdateAPIView as UpdateAPIView,
    ProductDestroyAPIView as DestroyAPIView,
)

app_name = 'products'
urlpatterns = [
    path('create', CreateAPIView.as_view(), name='create'),
    path('list', ListAPIView.as_view(), name='list'),
    path('retrieve/<int:id>', RetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:id>', UpdateAPIView.as_view(), name='update'),
    path('destroy/<int:id>', DestroyAPIView.as_view(), name='destroy'),
]
