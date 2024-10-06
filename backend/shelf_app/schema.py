import graphene
from graphene_django import DjangoObjectType
from shelf_app import models


class BookType(DjangoObjectType):
    class Meta:
        model = models.Book
        
        
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    
    def resolve_all_books(root, info):
        return (
            models.Book.objects.all()
        )
        
schema = graphene.Schema(query=Query)