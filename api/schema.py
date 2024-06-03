import graphene
from graphene_django import DjangoObjectType
from .models import PageInfo, Technology, Social


class TechnologyType(DjangoObjectType):
    class Meta:
        model = Technology


class SocialType(DjangoObjectType):
    class Meta:
        model = Social

class PageInfoType(DjangoObjectType):
    class Meta:
        model = PageInfo
        exclude = ('id',)

class Query(graphene.ObjectType):
    page_info = graphene.Field(PageInfoType, slug=graphene.String())

    
    def resolve_page_info(self, info, slug):
        return PageInfo.objects.get(slug=slug)
   
schema = graphene.Schema(query=Query)