from django.urls import path, include

app_name = 'products'
urlpatterns = [
    path('categories/', include('products.repo.urls.category')),
    path('', include('products.repo.urls.product')),
]
