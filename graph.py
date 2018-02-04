from graphene_django import DjangoObjectType

import graphene

from buddhalow.models import Experience, Dimension, Sport, Opportunity, Aqtivity


class ExperienceObjectType(DjangoObjectType):
    class Meta:
        model = Experience


class DimensionObjectType(DjangoObjectType):
    class Meta:
        model = Dimension


class SportObjectType(DjangoObjectType):
    class Meta:
        model = Sport


class OpportunityObjectType(DjangoObjectType):
    class Meta:
        model = Opportunity


class AqtivityObjectType(DjangoObjectType):
    class Meta:
        model = Aqtivity


class Query(graphene.ObjectType):
    all_opportunities = graphene.List(OpportunityObjectType)
    all_sports = graphene.List(SportObjectType)
    all_dimensions = graphene.List(DimensionObjectType)
    all_experiences = graphene.List(ExperienceObjectType)
    all_aqtivities = graphene.List(AqtivityObjectType)
   
    def resolve_all_opportunities(self, info, **kwargs):
        return Opportunity.objects.all()
  
    def resolve_all_sports(self, info, **kwargs):
        return Sport.objects.all()

    def resolve_all_dimensions(self, info, **kwargs):
        return Dimension.objects.all()
      
    def resolve_all_experiences(self, info, **kwargs):
        return Experience.objects.all()

    def resolve_all_aqtivities(self, info, **kwargs):
        return Aqtivities.objects.all()

class StartPageQuery(graphene.ObjectType):
  opportunities = graphene.List(OpportunityObjectType)
  
  def resolve_opportunities(self, info, **kwargs):
        return Opportunity.objects.all().order_by('-time')[:5]

      
schema = graphene.Schema(query=Query)
