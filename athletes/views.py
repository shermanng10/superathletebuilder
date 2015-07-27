from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Athlete, League, Sport, Team
from app_forms.athlete_forms import AthleteForm
from app_forms.team_forms import TeamForm


def home(request):
	return HttpResponse("This is the home page")


def new_athlete(request):
	if request.method == 'POST':
		form = AthleteForm(request.POST)
		if form.is_valid():
			athlete = form.save(commit=False)
			athlete.first_name = form.cleaned_data['first_name']
			athlete.last_name = form.cleaned_data['last_name']
			athlete.age = form.cleaned_data['age']
			athlete.gender = form.cleaned_data['gender']
			athlete.website = form.cleaned_data['website']
			athlete.sport = form.cleaned_data['sport']
			athlete.league = form.cleaned_data['league']
			athlete.team = form.cleaned_data['team']
			athlete.save()

			return HttpResponseRedirect('/athletes/')
	else:
		form = AthleteForm()

	return render(request, 'athletes/new.html', {'form': form})


class AthleteIndexView(generic.ListView):
	model = Athlete
	template_name = 'athletes/index.html'
	paginate_by = 10
	
class AthleteDetailView(generic.DetailView):
	model = Athlete
	template_name = 'athletes/detail.html'


def new_team(request):
	if request.method == 'POST':
		form = TeamForm(request.POST)
		if form.is_valid():
			team = form.save(commit=False)
			team.name = form.cleaned_data['team']
			team.save()
			return HttpResponseRedirect('/teams/')
	else:
		form = TeamForm()

	return render(request, 'teams/new.html', {'form': form})

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
