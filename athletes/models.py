from django.db import models

class Sport(models.Model):
	name = models.CharField(max_length=20)

class League(models.Model):
	name = models.CharField(max_length=20)
	sport = models.ForeignKey(Sport)

class Team(models.Model):
	name = models.CharField(max_length=20)
	sport = models.ForeignKey(Sport)
	league = models.ForeignKey(League)

class Athlete(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	age = models.PositiveIntegerField()
	gender = models.CharField(max_length=10)
	website = models.URLField()
	sport = models.ForeignKey(Sport)
	league = models.ForeignKey(League)
	team = models.ForeignKey(Team)




