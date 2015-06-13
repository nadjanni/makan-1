from django.db import models

# Create your models here.

class Club(models.Model):
  club_name = models.CharField(max_length = 200)
  create_date = models.DateTimeField('date created')

class Eater(models.Model):
  member_club = models.ForeignKey(Club)
  name = models.CharField(max_length = 200)
  create_date = models.DateTimeField('date created')

class Location(models.Model):
  location_name = models.CharField(max_length = 200)
  create_date = models.DateTimeField('date created')

class Experience(models.Model):
  reviewer = models.ForeignKey(Eater)
  notes = models.CharField(max_length = 500)
  venue = models.ForeignKey(Location)
  appreciates = models.IntegerField(default = 0)
  experience_date = models.DateTimeField('date of experience')
  create_date = models.DateTimeField('date created')

