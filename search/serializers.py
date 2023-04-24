from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import ProductsDocument
from product.models import Product

class SearchProductSerializer(DocumentSerializer):
 
    class Meta:
        model = Product
        document = ProductsDocument
        fields = ['title','description']
        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}