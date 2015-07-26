from django.shortcuts import HttpResponse
from .models import Athlete, League, Sport, Team
from django.views import generic

def home(request):
	return HttpResponse("This is the home page")


def new_athlete(request):
	return HttpResponse("This is a new athlete page")

class AthleteIndexView(generic.ListView):
	model = Athlete
	template_name = 'athletes/index.html'
	paginate_by = 10
	
class AthleteDetailView(generic.DetailView):
	model = Athlete
	template_name = 'athletes/detail.html'


def new_team(request):
	return HttpResponse("This is a new team page")

class TeamIndexView(generic.ListView):
	model = Team
	template_name = 'teams/index.html'
	paginate_by = 5
	
class TeamDetailView(generic.DetailView):
	model = Team
	template_name = 'teams/detail.html'


def new_league(request):
	return HttpResponse("This is a new league page")

class LeagueIndexView(generic.ListView):
	model = League
	template_name = 'leagues/index.html'
	paginate_by = 5

class LeagueDetailView(generic.DetailView):
	model = League
	template_name = 'leagues/detail.html'



def new_sport(request):
	return HttpResponse("This is a new sport page")

class SportIndexView(generic.ListView):
	model = Sport
	template_name = 'sports/index.html'
	paginate_by = 5

class SportDetailView(generic.DetailView):
	model = Sport
	template_name = 'sports/detail.html'
