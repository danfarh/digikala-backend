from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from product.models import Product
from .serializers import SearchProductSerializer
from .documents import ProductsDocument
#elasticsearch
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)


#pagination
class SetPagination(PageNumberPagination):
	page_size = settings.PRODUCTS_PAGINATION
	page_size_query_param = 'page_size'
	max_page_size = settings.MAX_PRODUCTS_PAGINATION

class SearchProductView(DocumentViewSet): 
    queryset = Product.objects.all()
    serializer_class = SearchProductSerializer
    pagination_class = SetPagination
    
    document = ProductsDocument
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
   
    search_fields = (
        'title',
        'description'
    
    )
    multi_match_search_fields = (
       'title',
       'description'
     
    )
    filter_fields = {
       'title' : 'title',
       'description' : 'description'
    
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ( 'id'  ,) 
    