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
    path('', CreateAPIView.as_view(), name='create'),
    path('', ListAPIView.as_view(), name='list'),
    path('<int:id>', RetrieveAPIView.as_view(), name='retrieve'),
    path('<int:id>', UpdateAPIView.as_view(), name='update'),
    path('<int:id>', DestroyAPIView.as_view(), name='destroy'),
]
