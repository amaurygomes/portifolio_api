import graphene
from graphene_django import DjangoObjectType
from .models import PageInfo, Social, KnowTechs, Technology
from .converters import *


class KnowTechsType(DjangoObjectType):
    class Meta:
        model = KnowTechs


class SocialType(DjangoObjectType):
    class Meta:
        model = Social

class TechnologiesType(DjangoObjectType):
    class Meta:
        model = Technology

class PageInfoType(DjangoObjectType):
    class Meta:
        model = PageInfo
        

class Query(graphene.ObjectType):
    page_info = graphene.Field(PageInfoType, id=graphene.Int())
    know_technologies = graphene.Field(KnowTechsType, id=graphene.Int())

    def resolve_page_info(self, info, id):
        try:
            return PageInfo.objects.get(id=1)
        except PageInfo.DoesNotExist:
            return None

    def resolve_know_technologies(self, info, id):
        try:
            return KnowTechs.objects.get(id=1)
        except KnowTechs.DoesNotExist:
            return None
    

    
   
schema = graphene.Schema(query=Query)