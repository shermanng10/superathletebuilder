from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Athlete, League, Sport, Team
from app_forms.athlete_forms import AthleteForm
from app_forms.team_forms import TeamForm
from app_forms.league_forms import LeagueForm
from app_forms.sport_forms import SportForm


def home(request):
	return render(request, 'home.html')


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
			team.name = form.cleaned_data['name']
			team.sport = form.cleaned_data['sport']
			team.league = form.cleaned_data['league']
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
	if request.method == 'POST':
		form = LeagueForm(request.POST)
		if form.is_valid():
			league = form.save(commit=False)
			league.name = form.cleaned_data['name']
			league.sport = form.cleaned_date['sport']
			league.save()
			return HttpResponseRedirect('/leagues/')
	else:
		form = LeagueForm()

	return render(request, 'leagues/new.html', {'form': form})
	

class LeagueIndexView(generic.ListView):
	model = League
	template_name = 'leagues/index.html'
	paginate_by = 5

class LeagueDetailView(generic.DetailView):
	model = League
	template_name = 'leagues/detail.html'



def new_sport(request):
	if request.method == 'POST':
		form = SportForm(request.POST)
		if form.is_valid():
			sport = form.save(commit=False)
			sport.name = form.cleaned_data['name']
			sport.save()
			return HttpResponseRedirect('/sports/')
	else:
		form = SportForm()

	return render(request, 'sports/new.html', {'form': form})


class SportIndexView(generic.ListView):
	model = Sport
	template_name = 'sports/index.html'
	paginate_by = 5

class SportDetailView(generic.DetailView):
	model = Sport
	template_name = 'sports/detail.html'
