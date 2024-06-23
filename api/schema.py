import graphene
from graphene_django import DjangoObjectType
from .models import PageInfo, Social, KnowTechs, Technology, HighlightProjects, Project, WorkExperience, Section
from .converters import *


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project

class KnowTechsType(DjangoObjectType):
    class Meta:
        model = KnowTechs

class HighlightsType(DjangoObjectType):
    class Meta:
        model = HighlightProjects


class SocialType(DjangoObjectType):
    class Meta:
        model = Social

class TechnologiesType(DjangoObjectType):
    class Meta:
        model = Technology

class PageInfoType(DjangoObjectType):
    class Meta:
        model = PageInfo

class WorkExperienceType(DjangoObjectType):
    class Meta:
        model = WorkExperience

class SectionType(DjangoObjectType):
    class Meta:
        model = Section
        

class Query(graphene.ObjectType):
    page_info = graphene.Field(PageInfoType, id=graphene.Int())
    know_technologies = graphene.Field(KnowTechsType, id=graphene.Int())
    highlight_projects = graphene.Field(HighlightsType, id=graphene.Int())
    all_work_experience = graphene.List(WorkExperienceType)
    all_projects = graphene.List(ProjectType)
    project_by_slug = graphene.Field(ProjectType, slug=graphene.String())



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
        
    def resolve_highlight_projects(self, info, id):
        try:
            return HighlightProjects.objects.get(id=id)
        except HighlightProjects.DoesNotExist:
            return None
        
    def resolve_project_by_slug(self, info, slug):
        try:
            return Project.objects.get(slug=slug)
        except Project.DoesNotExist:
            return None
    
    def resolve_all_work_experience(self, info):
        return WorkExperience.objects.all()
    
    def resolve_all_projects(self, info):
        return Project.objects.all()
    
   
schema = graphene.Schema(query=Query)