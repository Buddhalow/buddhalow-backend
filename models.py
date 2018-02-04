import datetime

from django.db import models

from buddhalow.util import generate_id


class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s %s' % (self.id, self.name)


class Facility(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s %s' % (self.id, self.name)


class Sport(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s %s' % (self.id, self.name)


class Dimension(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default=generate_id)
    name = models.CharField(max_length=255)
    description = models.TextField()
    time = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.name


class Experience(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default=generate_id)
    name = models.CharField(max_length=255)
    description = models.TextField()
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Opportunity(models.Model):
    id = models.CharField(max_length=255, primary_key=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    probability = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    status = models.ForeignKey(Status, default=100, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.name

    def save(self, commit=True, *args, **kwargs):
        if not self.id:
          self.id = generate_id(23)
        
        super(Opportunity, self).save(*args, **kwargs)
        opportunity_state = OpportunityState(
          opportunity=self, 
          description=self,
          name=self.name,
          probability=self.probability,
          status=self.status,
          dimension=self.dimension
        )
        opportunity_state.save()


class OpportunityState(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    probability = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.datetime.now)
    status = models.ForeignKey(Status, default=100, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class Aqtivity(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default=generate_id)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    aqtivity = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='parent_aqtivity_id')
    time = models.DateTimeField(default=datetime.datetime.now)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return '%s at %s on %s' % (self.sport, self.facility, self.time)
