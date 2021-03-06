from django.shortcuts import HttpResponse, render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from .models import Athlete, League, Sport, Team
from app_forms.athlete_forms import AthleteForm
from app_forms.team_forms import TeamForm
from app_forms.league_forms import LeagueForm
from app_forms.sport_forms import SportForm
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse_lazy

def home(request):
	return render(request, 'home.html')

class NewAthleteView(CreateView):
	model = Athlete
	form_class = AthleteForm
	template_name = 'athletes/new.html'

	def form_valid(self, form):
		form.save()
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

class AthleteIndexView(generic.ListView):
	model = Athlete
	template_name = 'athletes/index.html'
	paginate_by = 5

class EditAthleteView(UpdateView):
	model = Athlete
	form_class = AthleteForm
	template_name = 'athletes/edit.html'

	def dispatch(self, *args, **kwargs):
		self.item_id = kwargs['pk']
		return super(EditAthleteView, self).dispatch(*args, **kwargs)

	def form_valid(self, form):
		athlete = form.save()
		return HttpResponseRedirect("/athletes/" + str(athlete.id))
	
class AthleteDetailView(generic.DetailView):
	model = Athlete
	template_name = 'athletes/detail.html'

class AthleteDelete(DeleteView):
	model = Athlete
	success_url = reverse_lazy('athlete_index')
	template_name = 'athletes/delete_athlete.html'


class NewTeamView(CreateView):
	model = Team
	form_class = TeamForm
	template_name = 'teams/new.html'

	def form_valid(self, form):
		form.save()
		team = form.save(commit=False)
		team.name = form.cleaned_data['name']
		team.sport = form.cleaned_data['sport']
		team.league = form.cleaned_data['league']
		team.save()
		return HttpResponseRedirect('/teams/')
	

class TeamIndexView(generic.ListView):
	model = Team
	template_name = 'teams/index.html'
	paginate_by = 5
	
class TeamDetailView(generic.DetailView):
	model = Team
	template_name = 'teams/detail.html'


class NewLeagueView(CreateView):
	model = League
	form_class = LeagueForm
	template_name = 'leagues/new.html'

	def form_valid(self, form):
		form.save()
		league = form.save(commit=False)
		league.name = form.cleaned_data['name']
		league.sport = form.cleaned_data['sport']
		league.save()
		return HttpResponseRedirect('/leagues/')
	
class LeagueDetailView(generic.DetailView):
	model = League
	template_name = 'leagues/league_detail.html'


class LeagueIndexView(generic.ListView):
	model = League
	template_name = 'leagues/index.html'
	paginate_by = 5



class NewSportView(CreateView):
	model = Sport
	form_class = SportForm
	template_name = 'sports/new.html'

	def form_valid(self, form):
		form.save()
		sport = form.save(commit=False)
		sport.name = form.cleaned_data['name']
		sport.save()
		return HttpResponseRedirect('/sports/')
	

class SportIndexView(generic.ListView):
	model = Sport
	template_name = 'sports/index.html'
	paginate_by = 5

class SportDetailView(generic.DetailView):
	model = Sport
	template_name = 'sports/detail.html'
