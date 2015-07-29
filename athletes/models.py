from django.db import models
from django.utils import timezone
from django.utils.encoding import force_bytes

class Sport(models.Model):
	name = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return force_bytes(self.name)

class League(models.Model):
	name = models.CharField(max_length=20)
	sport = models.ForeignKey(Sport)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return force_bytes(self.name)
	
class Team(models.Model):
	name = models.CharField(max_length=20)
	sport = models.ForeignKey(Sport)
	league = models.ForeignKey(League)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return force_bytes(self.name)

class Athlete(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	age = models.PositiveIntegerField()
	gender = models.CharField(max_length=10)
	website = models.URLField()
	sport = models.ForeignKey(Sport)
	league = models.ForeignKey(League, blank=True, null=True)
	team = models.ForeignKey(Team, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return force_bytes('%s %s' % (self.first_name, self.last_name))






