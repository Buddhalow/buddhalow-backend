from django.contrib import admin

from .models import Aqtivity, Sport, Experience, Facility, Status, Dimension, Opportunity, OpportunityState

class AqtivityInline(admin.StackedInline):
    model = Aqtivity


class OpportunityStateInline(admin.StackedInline):
    model = OpportunityState
    ordering = ('-time',)


@admin.register(Aqtivity)
class AqtivityAdmin(admin.ModelAdmin):
    inlines = [AqtivityInline,]


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    model = Status


@admin.register(Dimension)
class DimensionAdmin(admin.ModelAdmin):
    model = Dimension


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    model = Opportunity
    inlines = [OpportunityStateInline, ]

    
@admin.register(OpportunityState)
class OpportunityStateAdmin(admin.ModelAdmin):
    model = OpportunityState
