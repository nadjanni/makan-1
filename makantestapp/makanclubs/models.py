from django.db import models

from django.utils import timezone

# Create your models here.

class Club(models.Model):
  club_name = models.CharField(max_length = 200)
  create_date = models.DateTimeField('date created', default=timezone.now())
  def __unicode__(self):
    return self.club_name

class Eater(models.Model):
  name = models.CharField(max_length = 200)
  create_date = models.DateTimeField('date created', default=timezone.now())
  def __unicode__(self):
    return self.name

class Location(models.Model):
  location_name = models.CharField(max_length = 200)
  create_date = models.DateTimeField('date created', default=timezone.now())
  def __unicode__(self):
    return self.location_name

class Experience(models.Model):
  reviewer = models.ForeignKey(Eater)
  notes = models.CharField(max_length = 500)
  venue = models.ForeignKey(Location)
  appreciates = models.IntegerField(default = 0)
  experience_date = models.DateTimeField('date of experience')
  create_date = models.DateTimeField('date created', default=timezone.now())
  def __unicode__(self):
    return 'Experience of ' + str(self.reviewer) + ' at ' + str(self.venue)

class Membership(models.Model):
  eater = models.ForeignKey(Eater)
  club = models.ForeignKey(Club)
  def __unicode__(self):
    return 'Membership of ' + str(self.eater), 'at', str(self.club)

