from django.shortcuts import HttpResponse

def home(request):
	return HttpResponse("This is the home page")



def new_athlete(request):
	return HttpResponse("This is a new athlete page")

def athlete_index(request):
	return HttpResponse("This is the index page")
	
def athlete_detail(request, athlete_id):
	return HttpResponse("This is detailed")



def new_team(request):
	return HttpResponse("This is a new team page")

def team_index(request):
	return HttpResponse("This is the index page")

def team_detail(request, team_id):
	return HttpResponse("This is detailed")



def new_league(request):
	return HttpResponse("This is a new league page")

def league_index(request):
	return HttpResponse("This is the index page")

def league_detail(request, league_id):
	return HttpResponse("This is detailed")



def new_sport(request):
	return HttpResponse("This is a new sport page")

def sport_index(request):
	return HttpResponse("This is the index page")

def sport_detail(request, sport_id):
	return HttpResponse("This is detailed")

