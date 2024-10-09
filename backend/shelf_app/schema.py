import graphene
from graphene_django.types import DjangoObjectType
from shelf_app import models

class CategoryType(DjangoObjectType):
    class Meta:
        model = models.Category

class BookType(DjangoObjectType):
    class Meta:
        model = models.Book        
        
class Query(graphene.ObjectType):
    books = graphene.List(BookType, title_icontains=graphene.String())
 
    def resolve_books(self, info, title_icontains=None):
        if title_icontains:
            return models.Book.objects.filter(title__icontains=title_icontains)
        else:
            return (
             models.Book.objects.all()   
            )
        
schema = graphene.Schema(query=Query)