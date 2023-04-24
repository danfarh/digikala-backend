from django_elasticsearch_dsl import (
    Document ,
    fields,
    Index,
)
from product.models import Product
PUBLISHER_INDEX = Index('elastic_product')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)


@PUBLISHER_INDEX.doc_type
class ProductsDocument(Document):
    
    id = fields.IntegerField(attr='id')
    fielddata=True
    title = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    description = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
   

    class Django(object):
        model = Product